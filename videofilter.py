import cv2
import numpy as np

def makeYellow(frame):
	(b, g, r) = cv2.split(frame)

	b = b.astype(float)
	g = g.astype(float)
	r = r.astype(float)

	b *= 1.2
	#r *= 1.1
	#g *= 1.1

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

cap = cv2.VideoCapture('django.mp4')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('yellowdjango.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))
while cap.isOpened():
	ret, frame = cap.read()

	if not ret:
		print("Can't receive VideoCapture. Exiting...")
		break

	img = makeYellow(frame)
	out.write(img)
	'''
	cv2.imshow('VideoCapture', img)
	if cv2.waitKey(1) == ord('q'):
		break'''

cap.release()
out.release()
cv2.destroyAllWindows()