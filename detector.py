import cv2
import numpy as np


class QualityInspector:
    def __init__(self, min_defect_area=150):
        self.min_defect_area = min_defect_area

    def preprocess(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        thresh = cv2.adaptiveThreshold(
            blurred,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV,
            11,
            2,
        )

        kernel = np.ones((3, 3), np.uint8)

        opening = cv2.morphologyEx(
            thresh,
            cv2.MORPH_OPEN,
            kernel,
            iterations=2,
        )

        cleaned = cv2.morphologyEx(
            opening,
            cv2.MORPH_CLOSE,
            kernel,
            iterations=2,
        )

        return cleaned

    def detect_defects(self, image):

        processed = self.preprocess(image)

        contours, _ = cv2.findContours(
            processed,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        output = image.copy()

        defects = []

        for contour in contours:

            area = cv2.contourArea(contour)

            if area < self.min_defect_area:
                continue

            x, y, w, h = cv2.boundingRect(contour)

            defects.append((x, y, w, h))

            cv2.rectangle(
                output,
                (x, y),
                (x + w, y + h),
                (0, 0, 255),
                2,
            )

        return output, defects

    def inspect(self, image):

        result, defects = self.detect_defects(image)

        status = "PASS"

        if len(defects) > 0:
            status = "FAIL"

        return result, status, len(defects)
