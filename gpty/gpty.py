#!/usr/bin/env python3

"""
OpenAI GPT API Command Line Wrapper

Usage:
gpty [prompts] [options]

"""

import openai
import argparse
import os
import sys
import json
import click_spinner

def debug_print(message, file=sys.stderr):
    print(message, file=file)

def cli():
    parser = argparse.ArgumentParser(description="OpenAI GPT API command line wrapper")

    parser.add_argument("prompts", nargs="*",
                        type=str,
                        help="Input prompts for GPT or '-' to read from stdin")
    parser.add_argument("-I", "--itemize",
                        type=str, metavar="MESSAGE",
                        help="Itemize other prompts after this message")
    parser.add_argument("-e", "--engine",
                        type=str, default="gpt-3.5-turbo",
                        help="OpenAI GPT engine (default: gpt-3.5-turbo)")
    parser.add_argument("-m", "--max-tokens",
                        type=int, default=2000,
                        help="Maximum number of tokens in the response (default: 2000)")
    parser.add_argument("-t", "--temperature",
                        type=float, default=0.5,
                        help="Sampling temperature for randomness (default: 0.5)")
    parser.add_argument("-d", "--debug",
                        action="store_true",
                        help="Show the request and response in JSON (default: False)")
    parser.add_argument("-k", "--key", type=str, default=None,
                        help="OpenAI API key")

    args = parser.parse_args()

    api_key = args.key or os.environ.get("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("Please set the environment variable OPENAI_API_KEY or provide the API key using the --key option.")
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

    request_params = {
        "model": args.engine,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
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
    print(generated_text)

if __name__ == "__main__":
    cli()
