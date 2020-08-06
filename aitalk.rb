#!/usr/bin/ruby -w

require 'getoptlong'
require 'net/http'
#Net::HTTP.version_1_2
require 'cgi'	# for CGI.escape()
require 'kconv'	# for .toeuc

opts = GetoptLong.new(
                      [ "--help", GetoptLong::NO_ARGUMENT ],
                      [ "--txtdirect", GetoptLong::NO_ARGUMENT ],
                      [ "--voice", GetoptLong::REQUIRED_ARGUMENT ],
                      [ "--host", GetoptLong::REQUIRED_ARGUMENT ],
                      [ "--output", GetoptLong::REQUIRED_ARGUMENT ],
                      [ "--rate", GetoptLong::REQUIRED_ARGUMENT ],
                      [ "--pitch", GetoptLong::REQUIRED_ARGUMENT ],
                      [ "--volume", GetoptLong::REQUIRED_ARGUMENT ]
)

def printusage()
  puts "Usage: ruby aitalk.rb [--help] [--voice (refer to voiceDB)] [--host host] [-o output] [--rate rate] [--pitch pitch] [--volume volume] [--txtdirect] text"
  puts "   or  ruby aitalk.rb [--help] [--voice (refer to voiceDB)] [--host host] [-o output] [--rate rate] [--pitch pitch] [--volume volume] [--txtdirect] < textfile (first line only)"
  puts "Options:"
  puts "  --help           display this help"
  puts "  --voice arg      specify voice (default: anzu)"
  puts "  --host arg       specify TTS server (default: 100.86.6.34)"
  puts "  --output arg     specify output filename (default: output.wav)"
  puts "  --rate arg       specify speaking rate (speed) (default: 1.0; between 0.5 and 2.0)"
  puts "  --pitch arg      specify pitch (default: 1.0; between 0.5 and 2.0)"
  puts "  --volume arg     specify volume (default: 1.0; >0.0)"
  puts "  --txtdirect      use the intermediate language of AITalk (See manuals for details)"
  exit(0)
end

#voiceDB = Array['akari','anzu','kaho','koutarou','nagisa','nanako','seiji'] # for the old server
voiceDB = Array['akari','anzu','koutarou','maki','maki_emo','miyabi_west','nozomi','nozomi_emo','seiji']

MyOpts = Hash.new()
opts.each do |opt, arg|
  MyOpts[opt] = arg
end

printusage() if MyOpts['--help']

host = (MyOpts['--host'] ? MyOpts['--host'] : '100.86.6.34')
outputfilename = (MyOpts['--output'] ? MyOpts['--output'] : 'output.wav')
voice = (MyOpts['--voice'] ? MyOpts['--voice'] : 'anzu')
unless voiceDB.include?(voice) then
  print "ERROR: Unknown voice: #{voice}\n"
  exit(0)
end
rate = (MyOpts['--rate'] ? MyOpts['--rate'] : 1.0)
pitch = (MyOpts['--pitch'] ? MyOpts['--pitch'] : 1.0)
volume = (MyOpts['--volume'] ? MyOpts['--volume'] : 1.0)
txtdirectmode = (MyOpts['--txtdirect'] ? 1 : 0)

text = (ARGV[0] ? ARGV[0] : STDIN.gets())
text = CGI.escape(text.toeuc)

http = Net::HTTP.start(host)
f = File.open(outputfilename, "wb")
f.print http.get("/cgi-bin/aitalk/aitalksrv.pl?voice=#{voice}&text=#{text}&rate=#{rate}&pitch=#{pitch}&volume=#{volume}&txtdirect=#{txtdirectmode}").body
