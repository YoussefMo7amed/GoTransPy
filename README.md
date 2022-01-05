# GoTransPy

### Version 0.0.1

A free and unlimited python CLI for google translate based on [google_trans_new](https://github.com/lushan88a/google_trans_new).  
It's very easy to use and solve the problem that the old api which use tk value cannot be used.
This interface is for academic use only, please do not use it for commercial use.

---

# Prerequisites

- **Python >=3.6**
- **requests**
- **six**

---

# Basic Usage

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

# License

[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/YoussefMo7amed/GoTransPy/main/LICENSE)
Copyright (c) 2022 Youssef Mohamed.
