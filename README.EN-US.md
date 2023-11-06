This document is automatically generated from README.md written in Japanese

# OpenAI API Command Line Wrapper

Simple command line interface to manipulate the GPT API

## USAGE

gpty [options] prompts

## PROMPTS

Non-optional arguments are interpreted as GPT input prompts. If the argument is `-`, it is read from the standard input. Each prompt is concatenated with a newline character and sent to the API.

## OPTIONS

### -I, --itemize *message*

The given message is placed at the top of the prompt, and other prompts are bulleted by inserting `* ` at the top. The `-` is read from the standard input, but no bullet processing is performed on it. For example, you can use the following.

    gpty -I 'Correct the following text according to the next conditions:' \
            'Lower case letters should be capitalized' \
            'Numbers should be Greek numerals' \
            - < data.txt

This is equivalent to instructing the user to

    gpty 'Correct the following text according to the next conditions:' \
         '* Lower case letters should be capitalized' \
         '* Numbers should be Greek numerals' \
         - < data.txt

It may not seem like much of a difference, but in Japanese, the prompt phrase does not contain spaces, so it is easier to type from the command line without the need to use quotation marks.

### -e, --engine *name*

The OpenAI GPT engine to use (default: gpt-3.5-turbo)

### -m, --max-tokens *number*

Maximum number of tokens in response (default: 2000)

### -t, --temperature *number*

The `temperature` value (default: 0.5)

### -k, --key *string*

OpenAI API keys

### -s, --squeeze

Combine two or more consecutive newline characters into one (default: False)

### -d, --debug

Display request and response contents in JSON format (default: False)

### -v, --version

Display version number and exit

## NOTE

The OpenAI API key is set by the `--key` option or the environment variable `OPENAI_API_KEY`.

## OTHER TOOS

### shell_gpt
  - https://github.com/TheR1D/shell_gpt
  - It can be used as `sgtp` command.
  - The `-s` option is useful.
  - It caches the results, which is useful for repeated runs
  - It is an excellent tool, and if you don't have trouble with it, you should definitely use it
  - Not always easy to use because prompts cannot be given via stdin

### gpt3
  - https://github.com/CrazyPython/gpt3-cli
  - Simple shell script that calls curl

### gptee
  - https://github.com/zurawiki/gptee
  - cli tool written in RUST
  - Installed but did not work with error
  - At first I was going to name it gptee, but when I looked for it, I found it and decided to use a different name.

## INSTALL

```
pip install git+https://github.com/kaz-utashiro/App-gpty.git
```

## AUTHOR

Kazumasa Utashiro

## LICENSE

MIT

## COPYRIGHT

The following copyright notice applies to all the files provided in
this distribution, including binary files, unless explicitly noted
otherwise.

Copyright © Kazumasa Utashiro
