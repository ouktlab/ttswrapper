#!/usr/bin/env python
# coding: utf-8

import argparse
import sys

try:
	from urllib.request import Request, urlopen   # for Python3
except:
	from urllib2 import Request, urlopen   # for Python2

try:
	from urllib.parse import quote_plus   # for Python3
except:
	from urllib import quote_plus  # for Python2


def parse():
	parser = argparse.ArgumentParser(add_help=False)
	parser.add_argument("--help", action="store_true")
	parser.add_argument("--host", default="100.86.6.34")
	parser.add_argument("--speaker", default="302")
	parser.add_argument("--output", default="output.wav")
	parser.add_argument("text", nargs='?')
	return parser.parse_args()

def printusage():
	print("Usage: ruby voicetext.py [--help] [--host host] [--speaker spid] [-o output] text")
	print("   or  ruby voicetext.py [--help] [--host host] [--speaker spid] [-o output] < textfile (first line only)")
	print("Options:")
	print("  --help           display this help")
	print("  --host arg       specify TTS server (default: 100.86.6.34)")
	print("  --speaker spid   specify speaker ID (default: 302; available: 303, 307, 103(english))")
	print("  --output arg     specify output filename (default: output.wav)")
	sys.exit()

def toUnicode(encodedStr):   # for Python2
    '''
    :return: an unicode-str.
    '''
    try: # if Python2
    	if isinstance(encodedStr, unicode):
        	return encodedStr
    except: # if Python3
    	if isinstance(encodedStr, str):
    		return encodedStr

    for charset in [u'utf-8', u'euc-jp', u'shift-jis', u'cp932', u'iso2022-jp']:
        try:
            return encodedStr.decode(charset)
        except:
            pass


if __name__ == "__main__":

	args = parse()
	if args.help:
		printusage()
	
	host = args.host
	outputfilename = args.output
	spid = args.speaker

	if args.text:
		text = args.text
	else:
		try:   # for Python3
			text = sys.stdin.buffer.readline()
		except:   # for Python2
			text = sys.stdin.readline()
	text = toUnicode(text).encode('euc_jp')
	text = quote_plus(text, safe='')
	
	url = "http://%s/cgi-bin/voicetext/voicetextsrv.pl?text=%s&speaker=%s" % (host, text, spid)
	res = urlopen(url)
	body = res.read()

	with open(outputfilename, "wb") as f:
		f.write(body)

