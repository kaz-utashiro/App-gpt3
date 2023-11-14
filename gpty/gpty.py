#!/usr/bin/env python3

"""
OpenAI GPT API Command Line Wrapper

Usage:
gpty [prompts] [options]

"""

from importlib.metadata import version
import argparse
import os
import sys
import re
import json
import click_spinner
import openai

def debug_print(message, file=sys.stderr):
    print(message, file=file)

package_name = "tecolicom-gpty"

def create_parser():

    def args(**kwargs): return kwargs
    spec = [
        (("prompts",),
         "input prompts for GPT or '-' to read from stdin", args(
             nargs   = "*",
             type    = str,
         )),
        (("-s", "--system",),
         "set system message (can be used multiple times)", args(
             action  = "append",
             type    = str,
             metavar = "MESSAGE",
         )),
        (("-I", "--itemize",),
         "itemize other prompts after this message", args(
             type    = str,
             metavar = "MESSAGE",
         )),
        (("-e", "--engine",),
         "OpenAI GPT engine", args(
             type    = str,
             default = "gpt-3.5-turbo",
         )),
        (("-m", "--max-tokens",),
         "maximum number of tokens in the response", args(
             type    = int,
             default = 2000,
         )),
        (("-t", "--temperature",),
         "sampling temperature for randomness", args(
             type    = float,
             default = 0.5,
         )),
        (("-k", "--key",),
         "OpenAI API key", args(
             type    = str,
         )),
        (("-q", "--squeeze",),
         "squeeze two or more newlines into one", args(
             action  = "store_true",
         )),
        (("-d", "--debug",),
         "show the request and response in JSON", args(
             action  = "store_true",
         )),
        (("-v", "--version",),
         "show version", args(
             action  = "version",
             version = f"%(prog)s {version(package_name)}",
         )),
    ]

    parser = argparse.ArgumentParser(
        description="OpenAI GPT API command line wrapper",
    )

    for args, help_message, kwargs in spec:
        if "default" in kwargs:
            help_message += f" (default: {kwargs['default']})"
        parser.add_argument(*args, help=help_message, **kwargs)

    return parser

def cli():

    parser = create_parser()
    args = parser.parse_args()

    api_key = args.key or os.environ.get("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("Set OPENAI_API_KEY or use --key option.")
    openai.api_key = api_key

    prompt_parts = []
    for p in args.prompts:
        if p == "-":
            prompt_parts.append(sys.stdin.read())
        else:
            if args.itemize:
                prompt_parts.append('* ' + p)
            else:
                prompt_parts.append(p)

    if args.itemize:
        prompt_parts.insert(0, args.itemize)

    prompt = "\n".join(prompt_parts)

    if args.system:
        messages = [ {"role": "system", "content": sys_message} for sys_message in args.system ]
    else:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]
    messages.append({"role": "user", "content": prompt})

    request_params = {
        "model": args.engine,
        "messages": messages,
        "max_tokens": args.max_tokens,
        "n": 1,
        "stop": None,
        "temperature": args.temperature,
        "timeout": 60,
    }

    if args.debug:
        debug_print("\nRequest Parameters:")
        debug_print(json.dumps(request_params, indent=2, ensure_ascii=False))

    with click_spinner.spinner():
        response = openai.ChatCompletion.create(**request_params)

    if args.debug:
        debug_print("\nFull JSON Response:")
        debug_print(json.dumps(response, indent=2, ensure_ascii=False))

    generated_text = response.choices[0].message['content'].strip()

    if args.squeeze:
        generated_text = re.sub(r'\n\n+', '\n', generated_text)

    print(generated_text)

if __name__ == "__main__":
    cli()
