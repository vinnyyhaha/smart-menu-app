from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def extract_text(image):
    result = ocr.ocr(image)

    texts = []
    for line in result:
        for word in line:
            texts.append(word[1][0])

    return texts
