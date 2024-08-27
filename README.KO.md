This document is automatically generated from README.md written in Japanese

# OpenAI API Command Line Wrapper

GPT API를 조작하기 위한 간단한 명령어 라인 인터페이스

## USAGE

gpty [options] prompts

## PROMPTS

옵션 이외의 인수는 GPT의 입력 프롬프트로 해석된다. 인수가 `-`인 경우 표준 입력에서 읽혀진다. 각 프롬프트는 줄 바꿈 문자로 연결하여 API로 보낸다.

## OPTIONS

### -s, --system *message*

시스템 메시지를 지정한다. 반복하여 여러 개의 메시지를 지정할 수 있다.

### -## -I, --itemize *message*

주어진 메시지를 프롬프트의 맨 앞에 배치하고, 다른 프롬프트는 앞에 `*`를 삽입하여 글머리 기호로 만든다. `-`는 표준 입력에서 읽혀지지만, 이에 대해서는 글머리 기호 처리가 이루어지지 않는다. 예를 들어, 다음과 같이 사용할 수 있다.

    gpty -I '다음 조건에 따라 다음 텍스트를 수정합니다:' \ '소문자는 대문자로' \ '숫자는 그리스 숫자로' \ '다음 조건에 따라 다음 텍스트를 수정합니다' \ '소문자는 대문자로' \ '숫자는 그리스 숫자이어야 합니다. - < data.txt

이것은 다음과 같이 지시하는 것과 같다.

    gpty '다음 조건에 따라 다음 텍스트를 수정한다:' \ '* 소문자는 대문자로 표기해야 한다' \ '* 숫자는 그리스 숫자로 표기해야 한다' \ - < data.txt

별 차이가 없어 보이지만, 일본어는 프롬프트 문구 안에 공백이 포함되지 않기 때문에 따옴표를 사용할 필요가 없어 명령줄에서 입력하기 쉽다.

### -e, --engine *name*

使用する OpenAI GPT エンジン (default: gpt-4o-mini)

### -e, --engine *alias*

엔진 이름에는 다음과 같은 별칭이 정의되어 있다.

    3: gpt-3.5-turbo 4: gpt-4o-mini

이들은 `-e3`, `-e4`와 같이 사용할 수 있다.

### -m, --max-tokens *number*

응답에 포함될 최대 토큰 수 (default: 2000)

### -t, --temperature *number*

`temperature` 값 (default: 0.5)

### -## -k, --key *string*

OpenAI API 키

### -q, --squeeze

2자 이상 연속된 줄바꿈 문자를 하나로 묶음 (default: False)

### -d, --debug

요청과 응답의 내용을 JSON 형식으로 표시 (default: False)

### -v, --version

버전 번호를 표시하고 종료한다.

## NOTE

OpenAI의 API 키는 `--key` 옵션 또는 환경 변수 `OPENAI_API_KEY`로 설정한다.

## OTHER TOOS

### shell_gpt - https://github.com/TheR1D/shell_gpt - `sgtp` 명령어로 사용 가능 - `-s` 옵션이 편리함 - 결과를 캐싱해 주기 때문에 반복 실행에 편리함 - 훌륭한 도구이므로, 이것으로 문제가 없다면 꼭! 사용해야 할 것 - 표준 입력에서 프롬프트를 제공하지 않기 때문에 사용성이 떨어질 수 있다.

### gpt3 - https://github.com/CrazyPython/gpt3-cli - curl을 호출하는 간단한 셸 스크립트

### gptee - https://github.com/zurawiki/gptee - RUST로 작성된 cli 도구 - 설치했으나 오류로 작동하지 않음 - 처음엔 gptee라는 이름으로 하려고 했는데, 찾아보니 있어서 다른 이름으로 변경 - 2023.11월에 최신 버전을 설치하니 동작함 - 2023.11에 최신 버전을

### llm - https://llm.datasette.io/en/stable/ - https://github.com/simonw/llm - `llm prompt -s system-prompt < prompt-text`처럼 사용할 수 있으므로 이것도 괜찮을 것 같다.

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
