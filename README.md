研究室内専用音声合成用ラッパー(wrapper)
---

* 使用法等は研究室内wikiを参照．

* aitalk.rb のサーバ側で使っている関数：AITalk_SaveWave()
  この詳細は研究室内wikiに置いているマニュアル参照．


## ChangeLog
#### 2020/08/06
* github に掲載．これ以降のupdateはHistory参照のこと．

#### 2018/05/14 版での変更点 (akai)
* aitalk.rb, voicetext.rb:  
	     ruby 2.4.0以降のバージョンに対応
* aitalk.py, voicetext.py:  
	     aitalk.rb, voicetext.rbをPythonに移植  
	     Python2.xとPython3.xの両方に対応
#### 2014/04/25 版での変更点 (komatani)
* voicetext.rb:  
	     サーバ側プログラムを変更（クライアントでjavaやそのライブラリは不要；  
	     voicetextsrv.plを作成し，aitalkと同様に通信するよう変更）．
* aitalk.rb, voicetext.rb:  
	     デフォルトのホストを 10.0.1.200 から xxx.x.xx.xx に変更．  
	     ruby 2.0.0に対応

#### 2012/01/20 版での変更点 (komatani)  
以下省略
