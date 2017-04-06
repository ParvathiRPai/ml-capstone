# %load prepare-image.py
import cv2
import numpy as np

def cropCordinates(image):
    height, width = image.shape[:2]

    new_size = min(height, width)
    cropped = None

    if new_size == height:
        start_row, start_col = int(0), int(0 + (width - new_size) / 2)

        end_row, end_col = int(height), int(width - (width - new_size) / 2)

        return (start_row, start_col, end_row, end_col)
    else:
        start_row, start_col = int(0 + (height - new_size) / 2), int(0)

        end_row, end_col = int(height - (height - new_size) / 2), int(width)

        return (start_row, start_col, end_row, end_col)

def crop(image):
    start_row, start_col, end_row, end_col = cropCordinates(image)

    return image[start_row:end_row , start_col:end_col]

def convertTo32by32(image):
    cropped = crop(image)
    resized = cv2.resize(cropped, (32, 32), interpolation = cv2.INTER_AREA)

    return resized

def swapChannel(image):
    return np.swapaxes(np.swapaxes(image, 0, 2),1,2)

def prepareImage(image, greyscale=False, preview=False):
    result = convertTo32by32(image)

    if greyscale:
        result = cv2.cvtColor(result, cv2.COLOR_BGRA2GRAY)
    else:
        resul = swapChannel(result)

    if preview:
        cv2.imshow("Preview", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

    return result
