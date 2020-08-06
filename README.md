研究室内音声合成用ラッパー(wrapper)
						2018/05/14	akai
						2014/04/25	komatani
						2012/01/20	komatani
						2011/12/06	komatani
						2011/12/01	komatani
						2011/10/31	komatani

* 使用法等は研究室内wikiを参照．

* aitalk.rb のサーバ側で使っている関数：AITalk_SaveWave()
  この詳細は研究室内wikiに置いているマニュアル参照．


[ChangeLog]
* 2018/05/14 版での変更点
・aitalk.rb, voicetext.rb:
	     ruby 2.4.0以降のバージョンに対応
・aitalk.py, voicetext.py:
	     aitalk.rb, voicetext.rbをPythonに移植
	     Python2.xとPython3.xの両方に対応
* 2014/04/25 版での変更点
・voicetext.rb:
	     サーバ側プログラムを変更（クライアントでjavaやそのライブラリは不要；
	     voicetextsrv.plを作成し，aitalkと同様に通信するよう変更）．
・aitalk.rb, voicetext.rb:
	     デフォルトのホストを 10.0.1.200 から 133.1.32.48 に変更．
	     ruby 2.0.0に対応

* 2012/01/20 版での変更点
・aitalk.rb:
	     サーバプログラム（aitalksrv.pl）を変更し，通信手順も一度の 
	     http.get で済むよう変更．回文デモでの連続要求時の不具合修正のため．
* 2011/12/06 版での変更点
・aitalk.rb:
	     --txtdirect に対応．

* 2011/12/01 版での変更点
・aitalk.rb: 
	     --rate, --pitch, --volume に対応．
・aitalk.rb, voicetext.rb:
	     デフォルトのホストを localhost から 10.0.1.200 に変更．
