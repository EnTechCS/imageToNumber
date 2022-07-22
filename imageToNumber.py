# Upsampling is required for accurate recognition. Resizing two-times will make the image readable.

# Erosion operation is a morphological operation helps to remove the boundary of the pixels. Erosion remove the strokes on the digit, make it easier to detect.

# Thresholding (Binary and Inverse Binary) helps to reveal the features.

# Bitwise-not is an arithmetic operation highly useful for extracting part of the image.

import cv2
import pytesseract
import time

pathImage = "imageTest.jpg"
pathImageSave = "date.txt"
img_lst = [pathImage]

for i, img_nm in enumerate(img_lst):
    img = cv2.imread(img_nm)
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (h, w) = gry.shape[:2]
    if i == 0:
        thr = gry
    else:
        gry = cv2.resize(gry, (w * 2, h * 2))
        erd = cv2.erode(gry, None, iterations=1)
        if i == len(img_lst)-1:
            thr = cv2.threshold(
                erd, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        else:
            thr = cv2.threshold(
                erd, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    bnt = cv2.bitwise_not(thr)
    txt = pytesseract.image_to_string(bnt, config="--psm 6 digits")
    file = open(pathImageSave, 'w')
    file.write(txt)
    file.close()
    print("".join([t for t in txt if t.isalnum()]))
    print("Ending process in 10s")
    time.sleep(10)
    print("Ending process")
    time.sleep(3)
    # cv2.imshow("bnt", bnt)
    # cv2.waitKey(0)
