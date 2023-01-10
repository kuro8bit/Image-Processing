# 幾何変換

[English](README.en.md) | [日本語](README.md)

---------------------------------------

- [平行移動](#translation)
- [回転](#rotation)
- [拡大縮小](#scaling)
- [せん断写像](#shearing)
- [アフィン変換](#affine) 

## 関数

### 平行移動<a id='translation'></a>

``(u,v)``が変換後の画素と``(x,y)``が元の画素とすると、平行移動の関数は

![png](images/translation.png)

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


![png](images/output_7_0.png)


### 回転 (度°)<a id='rotation'></a>

``(u,v)``が変換後の画素と``(x,y)``が元の画素とすると、画素``(0,0)``を中心に回転する関数は

![png](images/rotation.png)

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


![png](images/output_9_0.png)


### 拡大縮小<a id='scaling'></a>

``(u,v)``が変換後の画素と``(x,y)``が元の画素とすると、拡大縮小の関数は

![png](images/scale.png)

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


![png](images/output_11_0.png)


### せん断写像<a id='shearing'></a>

``(u,v)``が変換後の画素と``(x,y)``が元の画素とすると、せん断写像の関数は

![png](images/shear.png)

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


![png](images/output_13_0.png)


### アフィン変換<a id='affine'></a>

``(u,v)``が変換後の画素と``(x,y)``が元の画素とすると、アフィン変換の関数は

![png](images/affine.png)

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

![png](images/output_15_0.png)

