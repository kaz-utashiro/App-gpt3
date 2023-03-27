OpenAI GPT API Command Line Wrapper

This Python script allows you to easily interact with the GPT API from the command line.
You can provide various parameters as command-line options and get the generated text in the output.

Usage:
gpty [prompts] [options]

Arguments:
prompts: A list of input prompts for GPT, separated by spaces. If '-' is present, it will read from stdin.
The prompts will be concatenated with newline characters.

Options:
-e, --engine: The OpenAI GPT engine to use (default: gpt-3.5-turbo)
-m, --max-tokens: Maximum number of tokens in the response (default: 100)
-t, --temperature: Sampling temperature for randomness (default: 0.5)
-d, --debug: Show the full response and request parameters in JSON format, with Unicode characters preserved (default: False)
-k, --key: OpenAI API key (optional, overrides OPENAI_API_KEY environment variable)

Note:
    To use this script, you need to have the 'openai' library installed. You can install it using pip:
    pip install openai

    The API key can be provided using the --key option or set as the OPENAI_API_KEY environment variable.
