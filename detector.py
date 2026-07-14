import cv2


class QualityInspector:
    def __init__(self, threshold_area=500):
        self.threshold_area = threshold_area

    def inspect(self, image):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        _, thresh = cv2.threshold(
            blurred,
            120,
            255,
            cv2.THRESH_BINARY_INV
        )

        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        defects = 0

        output = image.copy()

        for contour in contours:

            area = cv2.contourArea(contour)

            if area > self.threshold_area:

                defects += 1

                x, y, w, h = cv2.boundingRect(contour)

                cv2.rectangle(
                    output,
                    (x, y),
                    (x + w, y + h),
                    (0, 0, 255),
                    2
                )

        status = "PASS"

        if defects > 0:
            status = "FAIL"

        return output, status, defects
