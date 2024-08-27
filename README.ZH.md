This document is automatically generated from README.md written in Japanese

# OpenAI API 命令行包装器

使用 GPT API 的简单命令行界面。

## 使用方法

gpty [options] 提示。

## PROMPTS

非选项参数被解释为 GPT 输入提示。如果参数为 `-`，则从标准输入读取。每个提示符都与换行符连接，并发送至 API。

### OPTIONS.

### -s, --system *message*.

指定系统信息。可通过重复指定多个信息。

### -I, --itemize *message*.

将给定的信息放在提示符的顶部，而其他提示符则通过在顶部插入 `* ` 来分项。 从标准输入中读取 `-`，但不对其进行弹出处理。例如，你可以使用

    gpty -I '根据以下条件更正以下文本：' \
            小写字母应大写' \
            数字应为希腊数字
            - < data.txt

这相当于指令如下。

    gpty '根据下一个条件更正以下文本：' （'* 小写字母应大写
         小写字母应大写
         数字应为希腊字母
         - < data.txt

看似差别不大，但在日语中，提示短语不包含空格，因此从命令行键入更方便，无需使用引号。

### -e, --engine *name*.

使用的 OpenAI GPT 引擎（默认：gpt-4o-mini）

### -e, --engine *alias*.

为引擎名称定义了以下别名： ### -e, --engine *alias

    3: gpt-3.5-turbo
    4: GPT-4O-MINI

这些别名可用作 `-e3`、`-e4`。

### -m, --max-tokens *number*.

响应中的最大标记数（默认值：2000）。

### -t, --temperature *number*.

温度值（默认值：0.5）。

### -k, --key *string*

OpenAI API 密钥。

### -q, --squeeze

将两个或多个连续换行符合并为一个（默认值：False）

### -d, --debug

以 JSON 格式显示请求和响应内容（默认值：false）

### -v, --version

显示版本号并退出。

### 注意

OpenAI API 密钥由 `--key` 选项或环境变量 `OPENAI_API_KEY` 设置。

## 其他操作系统。

### shell_gpt

- https://github.com/TheR1D/shell_gpt
- 可用作 `sgtp` 命令。
- s "选项很有用。
- 对重复运行很有用，因为它会缓存结果
- 这是一个非常好的工具，如果使用起来没有问题，就一定要使用它！
- 由于不能从 stdin 中发出提示，因此使用起来可能比较麻烦

### gpt3

- https://github.com/CrazyPython/gpt3-cli
- 调用 curl 的简单 shell 脚本

### gptee

- https://github.com/zurawiki/gptee
- 用 RUST 编写的 cli 工具。
- 已安装，但无法正常工作，且有错误。
- 起初我想把它命名为 gptee，但当我寻找它时却发现了它，于是我给它取了个别的名字。
- 安装 2023 年 11 月的最新版本后，它就能正常工作了。

### llm

- https://llm.datasette.io/en/stable/
- https://github.com/simonw/llm
- 它可以像 `llm prompt -s system-prompt < prompt-text` 那样使用，所以这可能行得通。

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
