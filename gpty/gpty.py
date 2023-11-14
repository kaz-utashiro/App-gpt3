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

def create_parser(package_version):

    spec = [
        (("prompts",),
         {"nargs": "*", "type": str, 
          "help": "input prompts for GPT or '-' to read from stdin"}),
        (("-I", "--itemize",),
         {"type": str, "metavar": "MESSAGE", 
          "help": "itemize other prompts after this message"}),
        (("-e", "--engine",),
         {"type": str, "default": "gpt-3.5-turbo",
          "help": "OpenAI GPT engine (default: gpt-3.5-turbo)"}),
        (("-m", "--max-tokens",),
         {"type": int, "default": 2000, 
          "help": "maximum number of tokens in the response (default: 2000)"}),
        (("-t", "--temperature",),
         {"type": float, "default": 0.5, 
          "help": "sampling temperature for randomness (default: 0.5)"}),
        (("-d", "--debug",),
         {"action": "store_true", 
          "help": "show the request and response in JSON (default: False)"}),
        (("-k", "--key",),
         {"type": str, "default": None, 
          "help": "OpenAI API key"}),
        (("-q", "--squeeze",),
         {"action": "store_true", 
          "help": "squeeze two or more newlines into one"}),
        (("-v", "--version",),
         {"action": "version", 
          "version": f"%(prog)s {package_version}"}),
        (("-s", "--system",),
         {"action": "append", "type": str, "metavar": "MESSAGE", 
          "help": "set system message (can be used multiple times)"}),
    ]

    parser = argparse.ArgumentParser(description="OpenAI GPT API command line wrapper")

    for args, kwargs in spec:
        parser.add_argument(*args, **kwargs)

    return parser

def cli():

    package_version = version("tecolicom-gpty")

    parser = create_parser(package_version)

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
