A Japanese Dictionary with AI

#Generative ai #Console English dictionary #web crawler

#### Introduction

This simple utility is actully my very second pet project back to 2008. It's a really easy to use Japanese Dictionary web crawler. If you were a linux console or windows wsl user, this might be handy for you.

At 2023, now I combined with AI usage.

Currently you can use this simple utiliy to generate your own close test

#### How to install

Need python3 and bs4 (beautifual soup 4) and openai

1. git clone

2. install.sh

I will create a invisible .edict under your home folder

and place bashscript under $home/bin/sh

###### [optional]

If you want to use ai, you need to buy a openai key to use

google "open ai key"

Once you have the key,

1. echo "my open ai key" > .oaikey

2. mv .oaikey ~/.jdict

Note: you don't need to have openai key to use basic feature.

#### How to use

Under console ( recommand wsl/ubuntu )

You can get a help file like the following:

```bash
> jdict
usage: jdict.py [-h] [-v] [-d DATABASE] [-q SQL3DB] [-s] [-l] [-f] [-m] [-a] [-i] [-k OAIKEY] [query ...]

A Japanese Dictionary Utility

positional arguments:
  query

options:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose mode
  -d DATABASE, --database DATABASE
  -q SQL3DB, --sqlite3 SQL3DB
  -s, --statistic       Some statistic
  -l, --listmark        list all marked history
  -f, --flushdatabase   Flush database
  -m, --marklastword    mark last consulted
  -a, --ai              Doing AI base on consulted history
  -i, --queryai         Using AI to do somthing amazing
  -k OAIKEY, --openaikey OAIKEY
```

#### Feature: consult the japanese dictionary

```bash
> jdict 挨拶
あい‐さつ【挨拶】

［名］(スル)《「挨」は押す、「拶」は迫る意で、本来、禅家で門下の僧に押し問答して、その悟りの深浅を試すこと》    １ 人に会ったときや別れるときなどに取り交わす礼にかなった動作や言葉。「—を交わす...

挨拶(あいさつ)切(き)・る

縁を切る。関係を断つ。「—・ると取り交はせしその文を反古(ほうぐ)にし」〈浄・天の網島〉

あいさつ‐にん【挨拶人】

仲裁人。「大郭にして囲職の女郎は、上職の—」〈色道大鏡・二〉

挨拶(あいさつ)は時(とき)の氏神(うじがみ)

争いごとが起きた時、その仲裁をしてくれる人は氏神様のようにありがたいのだから、その調停には従うべきであること。仲裁は時の 氏神。

あいさつ【挨拶】

1〔会釈〕a greeting；〔敬礼〕(a) salutation；〔軍人の〕a saluteあいさつを交わすexchange greetings／〔頭を下げて〕bow to each oth...

あいさつ【挨拶】

greeting《ご機嫌伺いなどの》;respects《敬意を示して》;address, speech《会合などでの》

あいさつをかわす【挨拶を交わす】

exchange greetings

あいさつじょう【挨拶状】

〔暑中見舞いなどの〕a greeting card移転のあいさつ状a notice of one's new address

あいさつ【挨拶】

[意味] 会などで他の人を前に社交的な対応として述べる言葉。また、人と会ったときや別れるときなどに交わす言葉や動作など、自分と相手との間に関係があることを示そうとする言語行動をいう。[英] a ...
This pattern : "挨拶" has been consulted 1 times!
```

#### Feature: show consulting history

```bash
> jdict -s
=======================================================================================
|                                          Word|Count|    Note A|    Note B|    Note C|
|                                            犬|    1|         M|      None|      None|
|                                            猫|    1|         M|      None|      None|
|                                    ハムスター|    1|         M|      None|      None|
|                                          挨拶|    1|      None|      None|      None|
=======================================================================================
```

#### Feature : mark the last word

Note: this utility will record the fail consulting string, so if you found a result is good enough for you. You can leave a mark for it, just like the **favorites list**.

```bash
> jdict -m

=======================================================================================
|                                          Word|Count|    Note A|    Note B|    Note C|
|                                            犬|    1|         M|      None|      None|
|                                            猫|    1|         M|      None|      None|
|                                    ハムスター|    1|         M|      None|      None|
|                                          挨拶|    1|         M|      None|      None|
=======================================================================================
```

#### #### Feature: dump the list of marked words

```bash
> jdict -l
=======================================================================================
|                                          Word|Count|    Note A|    Note B|    Note C|
|                                            犬|    1|         M|      None|      None|
|                                            猫|    1|         M|      None|      None|
|                                    ハムスター|    1|         M|      None|      None|
|                                          挨拶|    1|         M|      None|      None|
=======================================================================================
```

#### Feature: Use generative AI to generate the close test with the list of marked words

This will take a while depending on the response time of OPEN AI. and you probably will get different result every time. 

```textile
>jdict -a
ASK: Could you generate a close test by using 犬,猫,ハムスター,挨拶?
もちろんです！以下にクローズドテストを作成します：

1. 私は＿＿＿が好きです。
2. ＿＿＿は犬よりも小さいです。
3. 朝、私は＿＿＿に「おはよう」と言います。
4. 知らない人に会ったとき、＿＿＿をするのは礼儀です。

正解は以下の通りです：

1. 犬、猫、ハムスター
2. ハムスター
3. 犬、猫、ハムスター
4. 挨拶
```

#### Feature empty the history

This simple utility is designed for reading a document once a time currently.

So you might want to empty the record at ceratin point.

```bash
> jdict -f
Gone in the wind...
```

To do:

More generic ai feature. It's amazing.
