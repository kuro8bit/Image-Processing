## エッジ検出

[English](README.en.md) | [日本語](README.md)

---------------------------------------

既存の関数を使わずプログラミングしたエッジ検出

`.py` and `.ipynb` version

### ライブラリー
- Numpy
- OpenCV
- Time

## 方法
- Difference
- Prewitt
- Roberts
- Sobel
- Laplacian 4
- Laplacian 8

各フィルターの実行時間：約10秒

## テスト

入力画像

<img src="images/input.png" alt="input image" style="width:200px;"/>

出力画像

<p float="up">
  <p float="left">
    <img src="images/output-diff.png" alt="Difference" width="200" />
    <img src="images/output-prewitt.png" alt="Prewitt" width="200" />
    <img src="images/output-roberts.png" alt="Roberts" width="200" />
  </p>
  <p float="left">
    <img src="images/output-sobel.png" alt="Sobel" width="200" />
    <img src="images/output-laplacian4.png" alt="Laplacian 4" width="200" /> 
    <img src="images/output-laplacian8.png" alt="Laplacian 8" width="200" />
  </p>
</p>
