import cv2
import os

from detector import QualityInspector

IMAGE_PATH = "images/defective_part.jpg"
OUTPUT_FOLDER = "output"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "inspection_result.jpg")


def main():

    if not os.path.exists(IMAGE_PATH):
        print("Input image not found.")
        return

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    image = cv2.imread(IMAGE_PATH)

    inspector = QualityInspector()

    result, status, defects = inspector.inspect(image)

    color = (0, 255, 0)

    if status == "FAIL":
        color = (0, 0, 255)

    cv2.putText(
        result,
        f"Inspection: {status}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        2,
    )

    cv2.putText(
        result,
        f"Defects: {defects}",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2,
    )

    cv2.imwrite(OUTPUT_FILE, result)

    print("=" * 45)
    print("AUTOMATED QUALITY INSPECTION")
    print("=" * 45)
    print(f"Inspection Status : {status}")
    print(f"Defects Found     : {defects}")
    print(f"Output Saved      : {OUTPUT_FILE}")
    print("=" * 45)

    cv2.imshow("Inspection Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
