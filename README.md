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

## 計算方法
今回はドキュメントの内容を表すためにベータ分布と二項分布を使用して表している。

### ベータ分布
ベータ分布とはαとβの２つの結果数を用いた確率からなる連続的確率分布です。
ベータ分布の事前分布は一様であり、二項分布を追加していくような分布になるため今回は使用した。

```math
f(x|a,b) = η(x^{a-1})(1-x)^{b-1}
```

ηは正規化定数

a,b はそれぞれの結果数


### 二項分布
二項分布とは、独立した試行をｎ回行ったときの成功数を表す離散的確率分布です。

```math
P(x) = \begin{pmatrix}
n \
x
\end{pmatrix}
p^x (1-p)^{n-x}
```
p = 成功確率

n = 回数

## プログラムと計算より

今回のC君の実験では、プログラムcompare.pyより20回ほど実験を行えば完走率はほとんど間違ってないのではないかと考えられる。また、今回は改良前と改良後の完走率はかなり差があるものとしていたので、もし、完走率が近いものを比べる際は実験回数を５０回や１００回に増やさなければならないと考える。

## 実行環境
* Ubuntu 20.04
* Python 3.8

## ライセンス
このソフトウェアパッケージは、MITライセンスの下、再配布および使用が許可されています。

