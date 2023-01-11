# prorobo_work

このプログラムは確率ロボティクスの課題のために作成されたリポジトリです

## ソースコード

### compare1.py
このプログラムでは改良前と改良後の実験前含めた６回の分布の比較を行っている。
ベータ分布を用いて比較を行っている。

![事前・事後分布の比較](https://github.com/piropann/prorobo_work/blob/a31668c6a5c50c37fdb85bfe2bbef12e82c6cd0f/image/Figure_2.png)


### compare2.py
このプログラムでは改良前と改良後の事後分布の比較を行っている。
ベータ分布を用いて比較を行っている。

![事後分布の比較](https://github.com/piropann/prorobo_work/blob/a31668c6a5c50c37fdb85bfe2bbef12e82c6cd0f/image/Figure_3.png)

### compare.py
試行回数を1,5,10,20,100回に変更して、改良前と改良後の事後分布の比較を行っている。
プログラムには、二項分布を使用し今回は改良前の完走率を６０％、改良後の完走率を９０％として比較を行っている。

![事後分布の比較](https://github.com/piropann/prorobo_work/blob/a31668c6a5c50c37fdb85bfe2bbef12e82c6cd0f/image/Figure_1.png)

## 計算方法など
今回はドキュメントの内容を表すためにベータ分布と二項分布を使用して表している。

### ベータ分布

'''math
f(x|a,b) = η(x^{a-1})(1-x)^{b-1}
'''
ηは正規化定数

### 二項分布


## 実行環境
* Ubuntu 20.04
* Python 3.8

## ライセンス
このソフトウェアパッケージは、MITライセンスの下、再配布および使用が許可されています。

