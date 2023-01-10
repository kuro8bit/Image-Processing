
# Geometric Transformations

English | [日本語](README.md)

---------------------------------------

- [Translation](#translation)
- [Rotation](#rotation)
- [Scaling](#scaling)
- [Shearing](#shearing)
- [Affine Transformation](#affine) 

## Functions

### Translation<a id='translation'></a>

Considering that ``(u,v)`` is the new image pixel and ``(x,y)`` the old image pixel, translation is


![Translate Function](images/func_translation_0.png#gh-dark-mode-only)
![Translate Function](images/func_translation.png#gh-light-mode-only) 

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

![input](images/input_0.png#gh-dark-mode-only) ![translation](images/output_1_0.png#gh-dark-mode-only)
![input](images/input.png#gh-light-mode-only) ![translation](images/output_1.png#gh-light-mode-only)

### Rotation (in degrees)<a id='rotation'></a>

Considering that ``(u,v)`` is the new image pixel and ``(x,y)`` the old image pixel, the image rotates around the pixel ``(0,0)``

![Rotate Function](images/func_rotation_0.png#gh-dark-mode-only)
![Rotate Function](images/func_rotation.png#gh-light-mode-only) 

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

### Scaling<a id='scaling'></a>

Considering that ``(u,v)`` is the new image pixel and ``(x,y)`` the old image pixel, scaling is


![Scale Function](images/func_scale_0.png#gh-dark-mode-only)
![Scale Function](images/func_scale.png#gh-light-mode-only) 

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

### Shearing<a id='shearing'></a>

Considering that ``(u,v)`` is the new image pixel and ``(x,y)`` the old image pixel, shearing is


![Shear Function](images/func_shear_0.png#gh-dark-mode-only)
![Shear Function](images/func_shear.png#gh-light-mode-only) 

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

![input](images/input_0.png#gh-dark-mode-only) ![shear](images/output_4_0.png#gh-dark-mode-only)
![input](images/input.png#gh-light-mode-only) ![shear](images/output_4.png#gh-light-mode-only)

### Affine Transformation<a id='affine'></a>

Considering that ``(u,v)`` is the new image pixel and ``(x,y)`` the old image pixel, affine transformation is


![Affine Transformation](images/func_affine_0.png#gh-dark-mode-only)
![Affine Transformation](images/func_affine.png#gh-light-mode-only) 

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
