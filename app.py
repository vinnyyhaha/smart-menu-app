import cv2
from image_processing import enhance_image
from ocr_module import extract_text
from cleaning import clean_text
from structuring import structure_menu
from export import export_to_excel

def run_pipeline(image_path):
    img = cv2.imread(image_path)

    enhanced = enhance_image(img)
    texts = extract_text(enhanced)
    cleaned = clean_text(texts)
    structured = structure_menu(cleaned)

    export_to_excel(structured)

    print("Done! Check output.xlsx")

run_pipeline("menu.jpg")
