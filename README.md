# GoTransPy

![alt text](./GoTransPy.png)

You can translate what you want using your terminal instead of wasting your memory opening a browser.
A free and unlimited python CLI for google translate based on [google_trans_new](https://github.com/lushan88a/google_trans_new).  
It's very easy to use and solve the problem that the old api which use tk value cannot be used.

---

## Prerequisites

- **Python >=3.6**
  - _You can install python form [here](https://www.python.org/downloads/)_
- **requests**

```pip
pip install requests
```

- **six**

```pip
pip install six
```

- _if you don't have pip you can follow [these steps](https://pip.pypa.io/en/stable/installation/)_

---

## Basic Usage

### Auto detection translation (**\*Arabic** is the default targeted langauge\*)

```bash
$ python main.py "hello world"
مرحبا بالعالم
```

### Target a language by adding "-t" flag

```bash
$ python main.py "hello world" -t de
Hallo Welt
```

### Change source language by adding "-s" flag

```bash
$ python main.py "Auto" -s de -t en
Automobile
```

### Help tag

```bash
$ python main.py -h
 positional arguments:
  text                  text that will be translated.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program version number and exit
  -s SOURCE, --source SOURCE
                        the source language.
  -t TARGET, --target TARGET
                        the target language.
```

---

## License

Copyright (c) 2022 Youssef Mohamed.

[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/YoussefMo7amed/GoTransPy/main/LICENSE)
![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=flat)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FYoussefMo7amed%2FGoTransPy&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
