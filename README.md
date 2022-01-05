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
$ python main.js "hello world"
مرحبا بالعالم
```

### Target a language by adding "-t" flag

```bash
$ python main.js "hello world" -t de
Hallo Welt
```

### Change source language by adding "-s" flag

```bash
$ python main.js "Auto" -s de -t en
Automobile
```

### Help tag

```bash
$ python main.js -h
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

GoTransPy is licensed under the MIT License. 
Copyright (c) 2022 [Youssef Mohamed](https://github.com/YoussefMo7amed).

The terms are as follows:
```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
