import cv2
import os

from detector import QualityInspector


IMAGE_PATH = "images/defective_part.jpg"
OUTPUT_PATH = "output/result.jpg"


def main():

    if not os.path.exists(IMAGE_PATH):
        print("Image not found.")
        return

    image = cv2.imread(IMAGE_PATH)

    inspector = QualityInspector()

    result, status, defects = inspector.inspect(image)

    cv2.putText(
        result,
        f"Status: {status}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0) if status == "PASS" else (0, 0, 255),
        2,
    )

    cv2.imwrite(OUTPUT_PATH, result)

    print("=" * 40)
    print("Automated Quality Inspection")
    print("=" * 40)
    print(f"Inspection Status : {status}")
    print(f"Defects Detected  : {defects}")
    print(f"Saved Result      : {OUTPUT_PATH}")

    cv2.imshow("Inspection Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
