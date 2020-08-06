#!/usr/bin/ruby -w

require 'getoptlong'
require 'cgi'		# for CGI.escape
require 'kconv'		# for .toeuc
require 'net/http'

opts = GetoptLong.new(
                      [ "--help", GetoptLong::NO_ARGUMENT ],
                      [ "--host", GetoptLong::REQUIRED_ARGUMENT ],
                      [ "--speaker", GetoptLong::REQUIRED_ARGUMENT ],
                      [ "--output", GetoptLong::REQUIRED_ARGUMENT ]
)

def printusage()
  puts "Usage: ruby voicetext.rb [--help] [--host host] [--speaker sp] [-o output] text"
  puts "   or  ruby voicetext.rb [--help] [--host host] [--speaker sp] [-o output] < textfile (first line only)"
  puts "Options:"
  puts "  --help           display this help"
  puts "  --host arg       specify TTS server (default: 100.86.6.34)"
  puts "  --speaker spid   specify speaker ID (default: 302)"
  puts "  --output arg     specify output filename (default: output.wav)"
  exit(0)
end

MyOpts = Hash.new()
opts.each do |opt, arg|
  MyOpts[opt] = arg
end

printusage() if MyOpts['--help']

host = (MyOpts['--host'] ? MyOpts['--host'] : '100.86.6.34')
outputfilename = (MyOpts['--output'] ? MyOpts['--output'] : 'output.wav')
spid = (MyOpts['--speaker'] ? MyOpts['--speaker'] : '302')

text = (ARGV[0] ? ARGV[0] : STDIN.gets())
text = CGI.escape(text.toeuc)

#system("java ttstest --host #{host} --outputfilename #{outputfilename} --enc #{text}")

http = Net::HTTP.start(host)
f = File.open(outputfilename, "wb")
f.print http.get("/cgi-bin/voicetext/voicetextsrv.pl?text=#{text}&speaker=#{spid}").body
