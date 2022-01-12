import cv2
import numpy as np

#Reading Image
img = cv2.imread("selfie.jpg")


#Maximising one layer
h, w, d = img.shape
blue = np.full((h, w), 200, dtype = 'uint8')
print(blue.shape, img.shape)

def makeYellow(frame):
	(b, g, r) = cv2.split(frame)

	g = g.astype(float)
	r = r.astype(float)

	r *= 1.1
	g *= 1.1

	b = b.astype(int)
	g = g.astype(int)
	r = r.astype(int)
	b = np.clip(b, 0, 255)
	g = np.clip(g, 0, 255)
	r = np.clip(r, 0, 255)

	b = b.astype(np.uint8)
	g = g.astype(np.uint8)
	r = r.astype(np.uint8)

	return cv2.merge([b, g, r])

'''
#Splitting, Mixing and Mergin
(b, g, r) = cv2.split(img)
b = b.astype(float)
g = g.astype(float)
r = r.astype(float)

#b *= 1.3
g *= 1.3
r *= 1.3

b = b.astype(int)
g = g.astype(int)
r = r.astype(int)
b = np.clip(b, 0, 255)
g = np.clip(g, 0, 255)
r = np.clip(r, 0, 255)

print(np.amax(b))
print(np.amax(g))
print(np.amax(r))

b = b.astype(np.uint8)
g = g.astype(np.uint8)
r = r.astype(np.uint8)
newImage = cv2.merge([b, g, r])
'''

newImage = makeYellow(img)

cv2.imshow("Yellow Image", newImage)
key = cv2.waitKey(0)
if key == ord('q'):
	cv2.destroyAllWindows()