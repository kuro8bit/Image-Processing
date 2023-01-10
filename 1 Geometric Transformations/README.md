# 幾何変換

[English](README.en.md) | 日本語

---------------------------------------

- [平行移動](#translation)
- [回転](#rotation)
- [拡大縮小](#scaling)
- [せん断写像](#shearing)
- [アフィン変換](#affine) 

## 関数

### 平行移動<a id='translation'></a>

``(u,v)``が変換後の画素と``(x,y)``が元の画素とすると、平行移動の関数は

```math
\begin{pmatrix}
x\\
y\\
1
\end{pmatrix}
=
\begin{pmatrix}
1 & 0 & -dx\\
0 & 1 & -dy\\
0 & 0 & 1
\end{pmatrix}
\cdot
\begin{pmatrix}
u\\
v\\
1
\end{pmatrix}
```

```python
def translate(img,dx,dy):
    row,col = img.shape[:2]

    # resulting image
    img_f = np.zeros(img.shape)

    # translate
    for u in range(col):
        for v in range(row):
            x = u - dx
            y = v - dy
            if(0<=x<col and 0<=y<row):
                img_f[v,u] = img[y,x]

    return img_f
```

![input](images/input_0.png#gh-dark-mode-only) ![translate](images/output_1_0.png#gh-dark-mode-only)
![input](images/input.png#gh-light-mode-only) ![translate](images/output_1.png#gh-light-mode-only)

### 回転 (度°)<a id='rotation'></a>

``(u,v)``が変換後の画素と``(x,y)``が元の画素とすると、画素``(0,0)``を中心に回転する関数は

```math
\begin{pmatrix}
x\\
y\\
1
\end{pmatrix}
=
\begin{pmatrix}
\cos{\theta} & -\sin{\theta} & 0\\
\sin{\theta} & \cos{\theta} & 0\\
0 & 0 & 1
\end{pmatrix}
\cdot
\begin{pmatrix}
u\\
v\\
1
\end{pmatrix}
```

```python
def rotate(img,ang):
    row,col = img.shape[:2]
    rad = ang*math.pi/180

    # resulting image
    img_f = np.zeros(img.shape)

    # rotate
    for u in range(col):
        for v in range(row):
            x = round(u*math.cos(rad)-v*math.sin(rad))
            y = round(u*math.sin(rad)+v*math.cos(rad))
            if(0<=x<col and 0<=y<row):
                img_f[v,u] = img[y,x]    
    return img_f
```

![input](images/input_0.png#gh-dark-mode-only) ![rotation](images/output_2_0.png#gh-dark-mode-only)
![input](images/input.png#gh-light-mode-only) ![rotation](images/output_2.png#gh-light-mode-only)


### 拡大縮小<a id='scaling'></a>

``(u,v)``が変換後の画素と``(x,y)``が元の画素とすると、拡大縮小の関数は

```math
\begin{pmatrix}
x\\
y\\
1
\end{pmatrix}
=
\begin{pmatrix}
1/S_x & 0 & 0\\
0 & 1/S_y & 0\\
0 & 0 & 1
\end{pmatrix}
\cdot
\begin{pmatrix}
u\\
v\\
1
\end{pmatrix}
```

```python
def scale(img,sx,sy):
    row,col = img.shape[:2]
    M,N = int(round(sy*row)), int(round(sx*col)) # new shape

    # resulting image
    if(img.ndim==3):
        img_f = np.zeros([M,N,3]) # for colored images
    else:
        img_f = np.zeros([M,N]) # for images in grayscale

    # scale
    for u in range(N):
        for v in range(M):
            x = round(u/sx)
            y = round(v/sy)
            if(0<=x<col and 0<=y<row):
                img_f[v,u] = img[y,x]

    return img_f
```

![input](images/input_0.png#gh-dark-mode-only) ![scale](images/output_3_0.png#gh-dark-mode-only)
![input](images/input.png#gh-light-mode-only) ![scale](images/output_3.png#gh-light-mode-only)

### せん断写像<a id='shearing'></a>

``(u,v)``が変換後の画素と``(x,y)``が元の画素とすると、せん断写像の関数は

```math
\begin{pmatrix}
x\\
y\\
1
\end{pmatrix}
=
\begin{pmatrix}
1 & -sh_x & 0\\
-sh_y & 1 & 0\\
0 & 0 & 1
\end{pmatrix}
\cdot
\begin{pmatrix}
u\\
v\\
1
\end{pmatrix}
```

```python
def shear(img,shx,shy):
    row,col = img.shape[:2]

    # resulting image
    img_f = np.zeros(img.shape)

    # shear
    for u in range(col):
        for v in range(row):
            x = round(u - v*shx)
            y = round(v - u*shy)
            if(0<=x<col and 0<=y<row):
                img_f[v,u] = img[y,x]

    return img_f
```

![input](images/input_0.png#gh-dark-mode-only) ![shearing](images/output_4_0.png#gh-dark-mode-only)
![input](images/input.png#gh-light-mode-only) ![shearing](images/output_4.png#gh-light-mode-only)

### アフィン変換<a id='affine'></a>

``(u,v)``が変換後の画素と``(x,y)``が元の画素とすると、アフィン変換の関数は
```math
\begin{pmatrix}
x\\
y\\
1
\end{pmatrix}
=
\begin{pmatrix}
t_{11} & t_{21} & t_{31}\\
t_{12} & t_{22} & t_{32}\\
0 & 0 & 1
\end{pmatrix}
\cdot
\begin{pmatrix}
u\\
v\\
1
\end{pmatrix}
```

```python
def affine(img,m):
    row,col = img.shape[:2]

    # resulting image
    img_f = np.zeros(img.shape)

    # affine transformation
    for u in range(col):
        for v in range(row):            
            x = int(round( t[0,0]*u + t[0,1]*v + t[0,2] ))
            y = int(round( t[1,0]*u + t[1,1]*v + t[1,2] ))
            if(0<=x<col and 0<=y<row):
                img_f[v,u] = img[y,x]

    return img_f
```

![input](images/input_0.png#gh-dark-mode-only) ![affine](images/output_5_0.png#gh-dark-mode-only)
![input](images/input.png#gh-light-mode-only) ![affine](images/output_5.png#gh-light-mode-only)
