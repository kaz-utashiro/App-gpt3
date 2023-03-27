(This document is automatically generated from README.md written in Japanese)

# OpenAI GPT API Command Line Wrapper

Command line interface to easily manipulate the GPT API from the command line. Various parameters can be specified and the generated text can be retrieved in the output.

## Usage:

gpty [options] [prompts]

## Arguments

### prompt

Non-optional arguments are interpreted as GPT input prompts. `-` is read from the standard input. Each prompt is concatenated with a newline character and sent to the API.

## Options

### -e, --engine

The OpenAI GPT engine to use (default: gpt-3.5-turbo)

### -m, --max-tokens

maximum number of tokens in the response (default: 100)

### -t, --temperature

The `temperature` value (default: 0.5)

### -d, --debug

Display request and response contents in JSON format (default: False)

### -k, --key

OpenAI API keys

## Note

The OpenAI API key is set by the `--key` option or the environment variable `OPENAI_API_KEY`.

## Other Toos:

- shell_gpt
  - https://github.com/TheR1D/shell_gpt
  - It can be used as `sgtp` command.
  - The `-s` option is useful.
  - It's a great tool and if you don't have trouble with it, you should definitely use it.
  - Can be a little annoying since the prompt is not given via stdin

- gpt3
  - https://github.com/CrazyPython/gpt3-cli
  - Simple shell script that calls curl

- gptee
  - https://github.com/zurawiki/gptee
  - cli tool written in RUST
  - Installed but did not work with error
  - At first I was going to name it gptee, but when I looked for it, I found it and decided to use a different name.
