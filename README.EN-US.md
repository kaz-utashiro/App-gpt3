This document is automatically generated from README.md written in Japanese

# OpenAI API Command Line Wrapper

A simple command line interface for working with the GPT API.

## USAGE

gpty [options] prompts

## PROMPTS

Non-optional arguments are interpreted as GPT input prompts. If the argument is `-`, it is read from the standard input. Each prompt is concatenated with a newline character and sent to API.

## OPTIONS

### -s, --system *message* Specifies a system message.

Specifies a system message. Multiple messages can be specified by repeating.

### -I, --itemize *message*

Put the given message at the top of the prompt, and bullet other prompts by inserting `* ` at the top. The `-` is read from standard input, but no bullet processing is performed on it. For example, you can use

    gpty -I 'Correct the following text according to the next conditions:' \
            'Lower case letters should be capitalized' \
            'Numbers should be Greek numerals' \
            - < data.txt

This is equivalent to the following instruction

    gpty 'Correct the following text according to the next conditions:' \
         '* Lower case letters should be capitalized' \
         '* Numbers should be Greek numerals' \
         - < data.txt

It may not seem like much of a difference, but in Japanese, the prompt phrase does not include spaces, so it is easier to type from the command line without the need to use quotation marks.

### -e, --engine *name*.

使用する OpenAI GPT エンジン (default: gpt-4o-mini)

### -e, --engine *alias*

The following aliases are defined for the engine name: ### -e, --engine *alias

    3: gpt-3.5-turbo
    4: gpt-4o-mini

These can be used like `-e3` and `-e4`.

### -m, --max-tokens *number*.

Maximum number of tokens in response (default: 2000).

### -t, --temperature *number*

The `temperature` value (default: 0.5).

### -k, --key *string*

OpenAI API key.

### -q, --squeeze

combine two or more consecutive newline characters into one (default: false)

### -d, --debug

Display request and response contents in JSON format (default: False)

### -v, --version

Print version number and exit.

## NOTE

The OpenAI API key is set by the `--key` option or the environment variable `OPENAI_API_KEY`.

## OTHER TOOS

### shell_gpt

- https://github.com/TheR1D/shell_gpt
- Can be used as a `sgtp` command.
- `-s` option is useful
- It caches the results, which is useful for repeated runs
- It is an excellent tool, and if you don't have trouble with it, you should definitely use it!
- Cannot be given as a prompt from stdin, so it is not always easy to use.

### gpt3

- https://github.com/CrazyPython/gpt3-cli
- Simple shell script that calls curl

### gptee

- https://github.com/zurawiki/gptee
- cli tool written in RUST
- I installed it, but it doesn't work with errors.
- At first I thought about naming it gptee, but when I looked for it, I found it, so I named it something else.
- I installed the latest version on Nov 2023 and it works!

### llm

- https://llm.datasette.io/en/stable/
- https://github.com/simonw/llm
- I can use it like `llm prompt -s system-prompt < prompt-text` so maybe this will work.

## INSTALL

```
pip install git+https://github.com/tecolicom/App-gpty.git
```

## SEE ALSO

### App::Greple::xlate

- https://metacpan.org/dist/App-Greple-xlate
- https://github.com/kaz-utashiro/App-Greple-xlate

### App::gpty

- https://github.com/tecolicom/App-gpty

### openai-python

- https://github.com/openai/openai-python

## AUTHOR

Kazumasa Utashiro

## LICENSE

MIT

## COPYRIGHT

The following copyright notice applies to all the files provided in
this distribution, including binary files, unless explicitly noted
otherwise.

Copyright © 2023-2024 Kazumasa Utashiro
