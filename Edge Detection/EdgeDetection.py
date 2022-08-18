import numpy as np
import cv2
import time

# input image filepath
filepath = 'images/input.png'

# Edge Detection Class
class edge:

    # available filters (some with horizontal(_h) and vertical(_v) direction)
    filters = {
        'diff_h' : np.array(([0, 0, 0],
                                         [0,-1, 1],
                                         [0, 0, 0])),

        'diff_v' : np.array(([0, 0, 0],
                                         [0,-1, 0],
                                         [0, 1, 0])),

        'prewitt_h' : np.array([[-1,0,1],
                                                [-1,0,1],
                                                [-1,0,1]]),

        'prewitt_v' : np.array([[-1,-1,-1],
                                                [0,0,0],
                                                [1,1,1]]),

        'roberts_h' : np.array([[0,0,0],
                                                [0,0,1],
                                                [0,-1,0]]),

        'roberts_v' : np.array([[0,0,0],
                                                [0,1,0],
                                                [0,0,-1]]),

        'sobel_h' : np.array([[-1,0,1],
                                            [-2,0,2],
                                            [-1,0,1]]),

        'sobel_v' : np.array([[-1,-2,-1],
                                            [0,0,0],
                                            [1,2,1]]),

        'laplacian4' : np.array([[0, 1, 0],
                                                [1,-4, 1],
                                                [0,  1, 0]]),

        'laplacian8' : np.array([[1, 1, 1],
                                                [1,-8, 1],
                                                [1, 1, 1]]),
    }

    def detection(img, filtername):

        # get Horizontal/Vertical mask of filter or Laplacian
        mask1 = edge.filters[filtername] if(filtername.startswith('laplacian')) else edge.filters[filtername + '_h']
        mask2 = np.zeros((3,3)) if(filtername.startswith('laplacian')) else edge.filters[filtername + '_v']

        M,N = img.shape[:2] # image size
        imgf = np.zeros((M,N), dtype=np.uint8) # output image

        for x in range(0,M):
            for y in range(0,N):
                x0, y0 = max(x-1, 0), max(y-1,0) # image start row/col indexes
                xf, yf = min(x+1, M-1), min(y+1, N-1) # image final row/col indexes
                u0, v0 = 0 if(x>0) else 1, 0 if(y>0) else 1 # mask start row/col indexes
                uf, vf = 2 if(x<M-1) else 1, 2 if(y<N-1) else 1 # mask final row/col indexes

                # multiply mask to image
                tmp1 = np.multiply(img[x0:xf+1, y0:yf+1],  mask1[u0:uf+1,v0:vf+1])
                tmp2 = np.multiply(img[x0:xf+1, y0:yf+1],  mask2[u0:uf+1,v0:vf+1])

                # sum of all values
                g1 = np.sum(tmp1)
                g2 = np.sum(tmp2)

                # square root (g1^2 + g2^2)
                g = int(np.sqrt(g1*g1+g2*g2))

                # set value g in output image g E [0,255]
                imgf[x,y] = max(min(g, 255), 0)

        return imgf


# read input image as grayscale
img = cv2.imread(filepath, 0)

# display input image
cv2.namedWindow('Input Image')
cv2.imshow('Input Image', img)

# list of all available filters
filters = ['diff', 'prewitt', 'roberts', 'sobel', 'laplacian4', 'laplacian8']

for flt in filters:
    t0 = time.time() # start time
    img1 = edge.detection(img, flt) # calculate edges
    t1 = time.time() # end time

    # display output image of current filter
    title = flt + ' (time: {:.2f}s)'.format(t1-t0)
    cv2.namedWindow(title)
    cv2.imshow(title, img1)

    # save output image
    cv2.imwrite('images/output-' + flt + '.png', img1)

cv2.waitKey()
cv2.destroyAllWindows()
