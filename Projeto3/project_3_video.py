# Standard imports
import cv2
import numpy as np
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'dados.mp4')

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(filename)
# cap = sk.vread(filename)

# Check if camera opened successfully
if (not cap.isOpened()):
    print("Error opening video stream or file")


# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
thickness = cv2.LINE_AA

# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:

        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        im_gauss = cv2.GaussianBlur(gray_image, (5, 5), 0)
        ret, thresh = cv2.threshold(im_gauss, 247, 255, 0)

        # get contours
        contours, _ = cv2.findContours(
            thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        count = 1

        for contour in contours:

            area = cv2.contourArea(contour)
            if area >= 1000 and area <= 3000:
                rect = cv2.minAreaRect(contour)
                box = cv2.boxPoints(rect)
                box = np.int0(box)

                x, y, w, h = cv2.boundingRect(contour)

                src_pts = box.astype("float32")
                # corrdinate of the points in box points after the rectangle has been
                # straightened
                dst_pts = np.array([[0, h-1],
                                    [0, 0],
                                    [w-1, 0],
                                    [w-1, h-1]], dtype="float32")

                # the perspective transformation matrix
                M = cv2.getPerspectiveTransform(src_pts, dst_pts)

                # directly warp the rotated rectangle to get the straightened rectangle
                dado = cv2.warpPerspective(gray_image, M, (w, h))
                # dado = gray_image[y:y+h, x:x+w]
                dado = cv2.resize(dado, None, fx=3, fy=3,
                                  interpolation=cv2.INTER_CUBIC)

                # Detect blobs.
                keypoints = detector.detect(dado)

                for marker in keypoints:
                    xd, yd = np.int(marker.pt[0]), np.int(marker.pt[1])
                    pos = np.int(marker.size / 2)
                    cv2.circle(dado, (xd, yd), 3, 255, -1)

                # Get text siza
                text = str(len(keypoints))
                size = cv2.getTextSize(text, font, font_scale, thickness)
                text_width = size[0][0]
                text_height = size[0][1]
                cv2.putText(frame, text, (int(x+(w/2)-(text_width/2)), int(y+(h/2) +
                                                                           (text_height/2))), font, font_scale, (0, 0, 255), 2, thickness)
                # cv2.polylines(frame, [box],  True,  (0, 123, 123),  1)
                cv2.imshow('dado'+str(count), dado)
                count += 1

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
