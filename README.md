# OpenAI GPT API Command Line Wrapper

コマンドラインから簡単にGPT APIを操作するためのコマンドラインインタフェース。
様々なパラメータを指定し、生成されたテキストを出力で取得することができる。

## Usage:

gpty [options] [prompts]

## Arguments

### prompt

オプション以外の引数はGPTの入力プロンプトとして解釈される。
`-` は標準入力から読み込まれる。
各プロンプトは、改行文字で連結されて API に送られる。

## Options

### -e, --engine

使用する OpenAI GPT エンジン (default: gpt-3.5-turbo)

### -m, --max-tokens

レスポンスに含まれる最大トークン数 (default: 100)

### -t, --temperature

`temperature` 値 (default: 0.5)

### -d, --debug

リクエストとレスポンスの内容を JSON 形式で表示する (default: False)

### -k, --key

OpenAI API キー

## Note

OpenAI の API キーは `--key` オプションか、環境変数 `OPENAI_API_KEY` として設定する。

## Other Toos:

- shell_gpt
  - https://github.com/TheR1D/shell_gpt
  - `sgtp` コマンドとして使える
  - `-s` オプションが便利
  - 素晴らしいツールなので、これで困らなければぜひ使うべき
  - プロンプトを標準入力から与えらられないため、少し困ることがある

- gpt3
  - https://github.com/CrazyPython/gpt3-cli
  - curl を呼び出すシンプルなシェルスクリプト

- gptee
  - https://github.com/zurawiki/gptee
  - RUST で書かれた cli ツール
  - インストールしたがエラーで動かない
  - 最初 gptee という名前にしようかと思ったが、探したらあったので別の名前にした
