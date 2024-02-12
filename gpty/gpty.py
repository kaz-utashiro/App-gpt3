#!/usr/bin/env python3

"""
OpenAI GPT API Command Line Wrapper

Usage:
gpty [prompts] [options]

"""

import typer
from typing import List, Optional
import os
import sys
import re
import json
from importlib.metadata import version
import click_spinner
import pprint
from openai import OpenAI

app = typer.Typer(add_completion=False)

package_name = "tecolicom-gpty"

def debug_print(message, file=sys.stderr):
    print(message, file=file)

def vers(ctx: typer.Context, value: bool):
    if not value or ctx.resilient_parsing:
        return
    typer.echo(f"{ctx.info_name} {version(package_name)}")
    raise typer.Exit()

aliases = {
    "3": "gpt-3.5-turbo",
    "4": "gpt-4-1106-preview",
}

@app.command()
def main(
    prompts:     List[str] = typer.Argument(...,                        help="Input prompts for GPT or '-' to read from stdin"),
    system:      List[str] = typer.Option([], "--system", "-s",         help="Set system message (can be used multiple times)"),
    itemize:     Optional[str] = typer.Option(None, "--itemize", "-I",  help="Itemize other prompts after this message"),
    engine:      str = typer.Option("gpt-3.5-turbo", "--engine", "-e",  help="OpenAI GPT engine"),
    max_tokens:  int = typer.Option(2000, "--max-tokens", "-m",         help="Maximum number of tokens in the response"),
    temperature: float = typer.Option(0.5, "--temperature", "-t",       help="Sampling temperature for randomness"),
    key:         Optional[str] = typer.Option(None, "--key", "-k",      help="OpenAI API key"),
    squeeze:     bool = typer.Option(False, "--squeeze", "-q",          help="Squeeze two or more newlines into one"),
    debug:       bool = typer.Option(False, "--debug", "-d",            help="Show the request and response in JSON"),
    version:     bool = typer.Option(False, "--version", callback=vers, help="Show version")
):
    """
    OpenAI GPT API command line wrapper.
    """
    api_key = key or os.environ.get("OPENAI_API_KEY")
    if api_key is None:
        raise typer.Exit("Set OPENAI_API_KEY or use --key option.")

    client = OpenAI(
        # This is the default and can be omitted
        api_key = os.environ.get("OPENAI_API_KEY"),
    )

    while engine in aliases:
        engine = aliases[engine]

    prompt_parts = []
    for p in prompts:
        if p == "-":
            prompt_parts.append(sys.stdin.read())
        else:
            if itemize:
                prompt_parts.append('* ' + p)
            else:
                prompt_parts.append(p)

    if itemize:
        prompt_parts.insert(0, itemize)

    prompt = "\n".join(prompt_parts)

    if system:
        messages = [{"role": "system", "content": sys_message} for sys_message in system]
    else:
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
    messages.append({"role": "user", "content": prompt})

    request_params = {
        "model": engine,
        "messages": messages,
        "max_tokens": max_tokens,
        "n": 1,
        "stop": None,
        "temperature": temperature,
        "timeout": 60,
    }

    if debug:
        debug_print("\nRequest Parameters:")
        debug_print(json.dumps(request_params, indent=2, ensure_ascii=False))

    with click_spinner.spinner():
        response = client.chat.completions.create(**request_params)

    if debug:
        pprint.pprint(response, indent=2)

    generated_text = response.choices[0].message.content

    if squeeze:
        generated_text = re.sub(r'\n\n+', '\n', generated_text)

    print(generated_text)

if __name__ == "__main__":
    app()
