# OpenAI API Command Line Wrapper

GPT API を操作するためのシンプルなコマンドラインインタフェース

## USAGE

gpty [options] prompts

## PROMPTS

オプション以外の引数は GPT の入力プロンプトとして解釈される。
引数が `-` だった場合、標準入力から読み込まれる。
各プロンプトは、改行文字で連結されて API に送られる。

## OPTIONS

### -s, --system *message*

システムメッセージを指定する。
繰り返すことで、複数のメッセージを指定することが可能。

### -I, --itemize *message*

与えられたメッセージをプロンプトの先頭に置き、他のプロンプトは先頭に `* ` を挿入して箇条書きにする。
`-` は標準入力から読み込まれるが、これについては箇条書きの処理は行われない。
例えば、次のように使うことができる。

    gpty -I 'Correct the following text according to the next conditions:' \
            'Lower case letters should be capitalized' \
            'Numbers should be Greek numerals' \
            - < data.txt

これは、次のように指示するのと同じである。

    gpty 'Correct the following text according to the next conditions:' \
         '* Lower case letters should be capitalized' \
         '* Numbers should be Greek numerals' \
         - < data.txt

大した違いではないように見えるかもしれないが、
日本語だとプロンプトのフレーズの中に空白が含まれないので、
引用符を使う必要がなくコマンド行から入力しやすい。

### -e, --engine *name*

使用する OpenAI GPT エンジン (default: gpt-3.5-turbo)

### -e, --engine *alias*

エンジン名には、以下の別名が定義されている:

    3: gpt-3.5-turbo
	4: gpt-4

これらは `-e3`、`-e4` のように使うことができる。

### -m, --max-tokens *number*

レスポンスに含まれる最大トークン数 (default: 2000)

### -t, --temperature *number*

`temperature` 値 (default: 0.5)

### -k, --key *string*

OpenAI API キー

### -q, --squeeze

2文字以上連続する改行文字を1つにまとめる (default: False)

### -d, --debug

リクエストとレスポンスの内容を JSON 形式で表示する (default: False)

### -v, --version

バージョン番号を表示して終了する

## NOTE

OpenAI の API キーは `--key` オプションか、環境変数 `OPENAI_API_KEY` として設定する。

## OTHER TOOS

### shell_gpt
  - https://github.com/TheR1D/shell_gpt
  - `sgtp` コマンドとして使える
  - `-s` オプションが便利
  - 結果をキャッシュしてくれるので、繰り返し実行するのに便利
  - 優れたツールなので、これで困らなければぜひ使うべき
  - プロンプトを標準入力から与えられないため、使い勝手が悪いことがある

### gpt3
  - https://github.com/CrazyPython/gpt3-cli
  - curl を呼び出すシンプルなシェルスクリプト

### gptee
  - https://github.com/zurawiki/gptee
  - RUST で書かれた cli ツール
  - インストールしたがエラーで動かない
  - 最初 gptee という名前にしようかと思ったが、探したらあったので別の名前にした
  - 2023.11 月に最新版をインストールしたら動いた

### llm
  - https://llm.datasette.io/en/stable/
  - https://github.com/simonw/llm
  - `llm prompt -s system-prompt < prompt-text` のように使えるのでこれでいいかも

## INSTALL

```
pip install git+https://github.com/tecolicom/App-gpty.git
```

## SEE ALSO

L<App::Greple::xlate>, L<App::Greple::xlate::gpt3>

L<https://github.com/openai/openai-python>

## AUTHOR

Kazumasa Utashiro

## LICENSE

MIT

## COPYRIGHT

The following copyright notice applies to all the files provided in
this distribution, including binary files, unless explicitly noted
otherwise.

Copyright © Kazumasa Utashiro
