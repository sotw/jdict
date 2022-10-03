## Python3 Japanese Dictionary

#### Introduction

こんにちは！

This simple utility branch out from my big snowball project hmdict. It's a really easy to use Japanese Dictionary web crawler. If you were a linux console user, this might be handy for you.

#### How to install

Need python3 and bs4 (beautifual soup 4)

1. git clone

2. install.sh

I will create a invisible .edict under your home folder

and place bashscript under $home/bin/sh

#### How to use

```bash
jdict [word]
```

```bash
usage: jdict.py [-h] [-v] [-d DATABASE] [-q SQL3DB] [-s] [-f] [query ...]

A Japanese Dictionary Utility

positional arguments:
  query

options:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose mode
  -d DATABASE, --database DATABASE
  -q SQL3DB, --sqlite3 SQL3DB
  -s, --statistic       Some statistic
  -f, --flushdatabase   Flush databaseme statistic
```

#### New Feature : auto record how many times you consult a word

```bash
jdict -s
======================================================================================
|                                         Word|Count|    Note A|    Note B|    Note C|
|                            　　　　　　おはよう|    5|      None|      None|      None|
|                                     　　　挨拶|    4|      None|      None|      None|
|                                        　哀愁|    4|      None|      None|      None|
|                                      孔明の罠|    4|      None|      None|      None|
|                                      　異世界|    3|      None|      None|      None|
|                                       おじさん|    2|      None|      None|      None|
======================================================================================
```

#### New Feature : delete records

```bash
jdict -f
Gone in the wind...
```

