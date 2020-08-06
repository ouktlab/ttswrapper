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
	parser.add_argument("--txtdirect", action="store_true")
	parser.add_argument("--voice", default="anzu")
	parser.add_argument("--host", default="133.1.32.48")
	parser.add_argument("--output", default="output.wav")
	parser.add_argument("--rate", type=float, default=1.0)
	parser.add_argument("--pitch", type=float, default=1.0)
	parser.add_argument("--volume", type=float, default=1.0)
	parser.add_argument("text", nargs='?')
	return parser.parse_args()

def printusage():
	print("Usage: ruby aitalk.rb [--help] [--voice (akari|anzu|kaho|koutarou|nagisa|nanako|seiji)] [--host host] [-o output] [--rate rate] [--pitch pitch] [--volume volume] [--txtdirect] text")
	print("   or  ruby aitalk.rb [--help] [--voice (akari|anzu|kaho|koutarou|nagisa|nanako|seiji)] [--host host] [-o output] [--rate rate] [--pitch pitch] [--volume volume] [--txtdirect] < textfile (first line only)")
	print("Options:")
	print("  --help           display this help")
	print("  --voice arg      specify voice (default: anzu)")
	print("  --host arg       specify TTS server (default: 133.1.32.48)")
	print("  --output arg     specify output filename (default: output.wav)")
	print("  --rate arg       specify speaking rate (speed) (default: 1.0; between 0.5 and 2.0)")
	print("  --pitch arg      specify pitch (default: 1.0; between 0.5 and 2.0)")
	print("  --volume arg     specify volume (default: 1.0; >0.0)")
	print("  --txtdirect      use the intermediate language of AITalk (See manuals for details)")
	sys.exit()

def toUnicode(encodedStr):   # for Python2
    '''
    :return: an unicode-str.
    '''
    try:   # if Python2s
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


voiceDB = ['akari','anzu','kaho','koutarou','nagisa','nanako','seiji']


if __name__ == "__main__":

	args = parse()
	if args.help:
		printusage()
	
	host = args.host
	outputfilename = args.output
	voice = args.voice
	if voice not in voiceDB:
		sys.exit("ERROR: Unknown voice: %s\n" % voice)
	rate = args.rate
	pitch = args.pitch
	volume = args.volume
	txtdirectmode = 1 if args.txtdirect else 0

	if args.text:
		text = args.text
	else:
		try:   # for Python3
			text = sys.stdin.buffer.readline()
		except:   # for Python2
			text = sys.stdin.readline()
	text = toUnicode(text).encode('euc_jp')
	text = quote_plus(text, safe='')
	
	url = "http://%s/cgi-bin/aitalk/aitalksrv.pl?voice=%s&text=%s&rate=%f&pitch=%f&volume=%f&txtdirect=%d" % (host, voice, text, rate, pitch, volume, txtdirectmode)
	res = urlopen(url)
	body = res.read()

	with open(outputfilename, "wb") as f:
		f.write(body)
