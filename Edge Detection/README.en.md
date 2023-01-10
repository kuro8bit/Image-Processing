# Edge Detection

English | [日本語](README.md)

---------------------------------------

### Libraries
- Numpy
- OpenCV
- Time

### Filters
- [Difference](#diff)
- [Prewitt](#prewitt)
- [Roberts](#roberts)
- [Sobel](#sobel)
- [Laplacian 4](#lap4)
- [Laplacian 8](#lap8)

Execution time of each filter: around 10 seconds

To apply the filters, considering each index on the filter

<div align="center">
  
|$mask(-1,-1)$|$mask(-1,0)$|$mask(-1,1)$| 
|--|--|--|
|$mask( 0,-1)$|$mask( 0,0)$|$mask( 0,1)$| 
|$mask( 1,-1)$|$mask( 1,0)$|$mask( 1,1)$| 
  
</div>


For Filters that has one direction filter, each final pixel `f(x,y)`

```math
f(x,y) = \sum_{u=-1}^{1}\sum_{v=-1}^{1} mask(u,v) \cdot f(x+u,y+v)
```

For Filters that has horizontal and vertical direction filter, each final pixel `f(x,y)`
```math
g_H(x,y) = \sum_{u=-1}^{1}\sum_{v=-1}^{1} mask_H(u,v) \cdot f(x+u,y+v)
```
```math
g_V(x,y) = \sum_{u=-1}^{1}\sum_{v=-1}^{1} mask_V(u,v) \cdot f(x+u,y+v)
```
```math
f(x,y) = \sqrt{g_H(x,y)^2 + g_V(x,y)^2}
```
-------------------------------------

### Difference<a id='diff'></a>

<div align="center">
<table>
<tr><th>Horizontal</th><th>Vertical</th></tr>
<tr><td>

| 0| 0| 0|
|--|--|--|
| 0|-1| 1|
| 0| 0| 0|

</td><td>

| 0| 0| 0| 
|--|--|--|
| 0|-1| 0|
| 0| 1| 0|

</td></tr> </table>
</div>

<table>
<tr><th>Input</th><th>Difference Filter</th></tr>
<tr><td>

<img src="images/input.png" alt="Input" width="100%" />

</td><td>
<img src="images/output-diff.png" alt="Difference" width="100%" />

</td></tr> </table>

-------------------------------------

### Prewitt<a id='prewitt'></a>

<div align="center">
<table>
<tr><th>Horizontal</th><th>Vertical</th></tr>
<tr><td>

|-1| 0| 1|
|--|--|--|
|-1| 0| 1|
|-1| 0| 1|

</td><td>

|-1|-1|-1| 
|--|--|--|
| 0| 0| 0|
| 1| 1| 1|

</td></tr> </table>
</div>

<table>
<tr><th>Input</th><th>Prewitt Filter</th></tr>
<tr><td>

<img src="images/input.png" alt="Input" width="100%" />

</td><td>
<img src="images/output-prewitt.png" alt="Prewitt" width="100%" />

</td></tr> </table>

-------------------------------------

### Roberts<a id='roberts'></a>

<div align="center">
<table>
<tr><th>Horizontal</th><th>Vertical</th></tr>
<tr><td>

| 0| 0| 0|
|--|--|--|
| 0| 0| 1|
| 0|-1| 0|

</td><td>

| 0| 0| 0| 
|--|--|--|
| 0| 1| 0|
| 0| 0|-1|

</td></tr> </table>
</div>


<table>
<tr><th>Input</th><th>Roberts Filter</th></tr>
<tr><td>

<img src="images/input.png" alt="Input" width="100%" />

</td><td>
<img src="images/output-roberts.png" alt="Roberts" width="100%" />

</td></tr> </table>

-------------------------------------

### Sobel<a id='sobel'></a>

<div align="center">
<table>
<tr><th>Horizontal</th><th>Vertical</th></tr>
<tr><td>

|-1| 0| 1|
|--|--|--|
|-2| 0| 2|
|-1| 0| 1|

</td><td>

|-1|-2|-1| 
|--|--|--|
| 0| 0| 0|
| 1| 2| 1|

</td></tr> </table>
</div>

<table>
<tr><th>Input</th><th>Sobel Filter</th></tr>
<tr><td>

<img src="images/input.png" alt="Input" width="100%" />

</td><td>
<img src="images/output-sobel.png" alt="Sobel" width="100%" />

</td></tr> </table>

-------------------------------------

### Laplacian 4<a id='lap4'></a>

<div align="center">
  
| 0| 1| 0|
|--|--|--|
| 1|-4| 1|
| 0| 1| 0|
  
</div>

<table>
<tr><th>Input</th><th>Laplacian 4 Filter</th></tr>
<tr><td>

<img src="images/input.png" alt="Input" width="100%" />

</td><td>
<img src="images/output-laplacian4.png" alt="Prewitt" width="100%" />

</td></tr> </table>

-------------------------------------

### Laplacian 8<a id='lap8'></a>

<div align="center">
  
| 1| 1| 1| 
|--|--|--|
| 1|-8| 1|
| 1| 1| 1|
  
</div>

<table>
<tr><th>Input</th><th>Laplacian 8 Filter</th></tr>
<tr><td>

<img src="images/input.png" alt="Input" width="100%" />

</td><td>
<img src="images/output-laplacian8.png" alt="Laplacian 8" width="100%" />

</td></tr> </table>
