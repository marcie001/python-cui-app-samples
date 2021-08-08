# About

[Python スタートブック](https://gihyo.jp/book/2018/978-4-7741-9643-5) を読み終わって、復習として簡単なCUIアプリを作成するときの例。

## contacts.py

アドレス帳のような対話的なアプリです。

実行方法

```
python contacts.py data.txt
```

## Raspberry PiでLチカ

https://www.raspberrypi.org/documentation/usage/gpio/python/README.md

## weather.py

指定した町の現在の天気を表示するアプリです。

事前準備

```
python -m pip install requests
```

実行方法。 `--city` を指定しないと実行したマシンの地域の天気を表示します。

```
python weather.py --city 札幌
```
