# Author Pei-Chen Tsai

import os, sys, re, codecs, io
import urllib
import urllib.request, urllib.error
import urllib.parse
import argparse
import logging
import platform
import sqlite3
from HMTXCLR import clrTx
from os.path import expanduser
from pprint import pprint
from bs4 import BeautifulSoup,NavigableString

global DB
global args
global ARGUDB
global tPage
global mProun
global wordDb
global cursor
global ScreenI
global parser

mProun = []
ARGUDB        = []
ScreenI = []
tPage         = 'https://dictionary.goo.ne.jp/srch/all/'
INSFOLDER = ''
bWindows = False

def strip_tags(html, invalid_tags):
    stripSoup = BeautifulSoup(html)

    for tag in stripSoup.findAll(True):
        if tag.name in invalid_tags:
            s = ""

            for c in tag.contents:
                if not isinstance(c, NavigableString):
                    c = strip_tags(str(c,'utf8'), invalid_tags)
                s += str(c,'utf8')

            tag.replaceWith(s)
    return stripSoup

def repeatStr(string_to_expand, length):
	return (string_to_expand * ((length/len(string_to_expand))+1))[:length]

def htmlParser(tPage):
    print(tPage)
    resp = urllib.request.urlopen(url=tPage)
    if resp.code == 200 :
        data = resp.read()
        resp.close()
    elif resp.code == 404 :
        print("page do not exist")
        exit()
    else :
        print("can not open page")
        exit()

    soup = BeautifulSoup(data)

    print("beautifulSoup result")
    my_titles = soup.findAll('p',{'class','title'})
    my_texts = soup.findAll('p',{'class','text'})

    result = []

    for a in range(len(my_titles)):
        result.append(my_titles[a].get_text().strip())
        result.append(' ')
        result.append(my_texts[a].get_text().strip())
        result.append(' ')
    #    result += my_titles[a]
    #    result += my_texts[a]
    #    print(my_titles[a].get_text().strip())
    #    print(my_texts[a].get_text().strip())

#    ul = soup.findAll('ul',{'class','content_list idiom lsize'})
   

#    result += soup.findAll('li',{'class':['lh-22 mh-22 ml-50 mt-12 mb-12','lh-22 mh-22 ml-50 mt-12 mb-12 last']});
    
    return result

#[]== maybe textwrapper, it's better than this hardcode

def prettyPrint(resultString):
    if bWindows :
        os.system('cls')
    else:
        os.system('clear')

    #for tag in ARGUDB:
    #    resultString = re.sub(r''+tag,'\n'+tag+'\n    ',resultString)
    print('search target:'+tPage)
    for line in resultString:
        print(line)

def loadArgumentDb():
    global wordDb
    global cursor
    home = expanduser('~')
#    print(home+args.database)
    if os.path.isfile(home+args.database) is True:
        f = codecs.open(home+args.database,encoding='UTF-8',mode='r')
        if f is not None:
            for line in f:
                if line != '\n' and line[0] != '#':
                    line = line.rstrip('\n')
                    global ARGUDB
                    ARGUDB.append(line)
            f.close()
        else:
            DB.error('db file open fail')
    else :
        print('database doesn\'t existed')
    wordDb = sqlite3.connect(home+args.sql3db)
    cursor = wordDb.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS WOI
    (WORD TEXT PRIMARY KEY NOT NULL UNIQUE,
    REFCOUNT INT,
    NOTE_A TEXT,
    NOTE_B TEXT,
    NOTE_C TEXT
    );''')
    wordDb.commit()

def SQLStuff():
    global wordDb
    global cursor
    global tPage

    tPage = tPage.replace('/m0u/','')
    patterns = tPage.split("all/")
    if len(patterns) > 1:
#        print(urllib.parse.unquote(patterns[1]))
        targetPattern = urllib.parse.unquote(patterns[1])
#        targetPattern = patterns[1].replace('%20',' ')
        cursor.execute(f"SELECT * FROM WOI WHERE WORD=\"{targetPattern}\"")
        rows = cursor.fetchall()
        rowsCnt = len(rows)
#        print(f"rows:{rowsCnt}")
        if rowsCnt == 0:
            cursor.execute(f"INSERT OR REPLACE INTO WOI(WORD,REFCOUNT) values(\"{targetPattern}\",1)")
            wordDb.commit()
        else:
            cursor.execute(f"UPDATE WOI SET REFCOUNT=REFCOUNT+1 WHERE WORD=\"{targetPattern}\"")
            wordDb.commit()
        
        cursor.execute(f"SELECT * FROM WOI WHERE WORD=\"{targetPattern}\"")
        for row in cursor.fetchall():
            print(f"This pattern : \"{row[0]}\" has been consulted {row[1]} times!")

def SQLFlush():
    global wordDb
    global cursor
    cursor.execute(f"DELETE FROM WOI")
    wordDb.commit()
    print("Gone in the wind...")

def SQLDump():
    global wordDb
    global cursor
    global ScreenI
    rec_word = ""
    rec_cnt = 0
    rec_note_a = ""
    rec_note_b = ""
    rec_note_c = ""

    cursor.execute(f"SELECT * FROM WOI")
    rows = cursor.fetchall()
    for row in rows:
        ScreenI.append({'word':row[0], 'refcnt':str(row[1]), 'note_a':str(row[2]), 'note_b':str(row[3]), 'note_c':str(row[4])})

    if len(rows) > 0:
        for x in range(85):
            print("=",end='')
        print("=")
        print("|"+clrTx("                                         Word","CYAN")+"|"+clrTx("Count","CYAN")+ \
        "|"+clrTx("    Note A","CYAN")+"|"+clrTx("    Note B","CYAN")+ \
        "|"+clrTx("    Note C","CYAN")+"|")
        for item in ScreenI:
            target_str = f"|{item['word']:>45}|{item['refcnt']:>5}|{item['note_a']:>10}|{item['note_b']:>10}|{item['note_c']:>10}|" 
            print(clrTx(target_str,"WHITE"))
        for x in range(85):
            print("=",end='')
        print("=")

def main():
    global tPage
    global args
    global parser
    if args.statistic:
        SQLDump()
    elif args.flushdb:
        SQLFlush()
    elif not tPage or len(tPage) == 38:
        parser.print_help()
        exit(1)
    else:
        resultString = htmlParser(tPage)
        prettyPrint(resultString)
        SQLStuff()

def setup_logging(level):
	global DB
	DB = logging.getLogger('jdict') #replace
	DB.setLevel(level)
	handler = logging.StreamHandler(sys.stdout)
	handler.setFormatter(logging.Formatter('%(module)s %(levelname)s %(funcName)s| %(message)s'))
	DB.addHandler(handler)

def verify():
    global tPage
    global args
    global parser
    parser = argparse.ArgumentParser(description='A Japanese Dictionary Utility')
    parser.add_argument('-v', '--verbose', dest='verbose', action = 'store_true', default=False, help='Verbose mode')
    parser.add_argument('-d', '--database', dest='database', action = 'store', default='/.jdict/jdict.db')
    parser.add_argument('-q', '--sqlite3', dest='sql3db', action = 'store', default='/.jdict/jdict.db3')
    parser.add_argument('-s', '--statistic', dest='statistic', action = 'store_true', default=False, help='Some statistic')
    parser.add_argument('-f', '--flushdatabase', dest='flushdb', action = 'store_true', default=False, help='Flush database') 
    parser.add_argument('query', nargs='*', default=None)
    args = parser.parse_args()
    if len(args.query) != 0:
        query_string = ' '.join(args.query)
        query_string = urllib.parse.quote(query_string)
        tPage = tPage+query_string+'/m0u/'
#    tPage = tPage+' '.join(args.query)
    log_level = logging.INFO
    if args.verbose:
        log_level = logging.DEBUG

if __name__ == '__main__':
    verify()
    loadArgumentDb()
    main()
    
