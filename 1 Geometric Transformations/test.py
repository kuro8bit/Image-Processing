from geometric_transformations import *

import cv2 as cv # read image cv.imread()
import matplotlib.pyplot as plt # plot image


def show_image(img, title="Image"):
    fig = plt.figure()
    if(img.ndim == 2):
        plt.gray()
    plt.title(title)
    plt.xticks([0,img.shape[1]]), plt.yticks([0,img.shape[0]])
    plt.imshow(img)
    plt.show()


### ******* TESTS ******** ###
image = cv.imread("input.png",0)
show_image(image,"Input Image")

# Translation
dx,dy = 25,15
img = translate(image,dx,dy)
show_image(img, ("Translation dx="+str(dx)+", dy="+str(dy)) )

# Rotation
ang = 45
img = rotate(image,ang)
show_image(img, ("Rotation "+ str(ang) + " degrees") )

# Scaling
sx,sy=2,3
img = scale(image,sx,sy)
show_image(img, ("Scale sx="+str(sx)+", sy="+str(sy)) )

# Shearing
shx,shy = 0.75,-0.25
img = shear(image,shx,shy)
show_image(img, ("Shearing shx="+str(shx)+", shy="+str(shy)) )

# Rotate around image center
ang = 45
rad = ang*math.pi/180
row,col = image.shape[:2]
tx = (1-math.cos(rad))*row/2 - math.sin(rad)*col/2
ty = math.sin(rad)*row/2 + (1-math.cos(rad))*col/2

m = np.array(([math.cos(rad),-math.sin(rad),ty],
              [math.sin(rad), math.cos(rad),tx]))
img = affine(image, m)
show_image(img, ("Rotation "+ str(ang)+" degrees around image center") )
