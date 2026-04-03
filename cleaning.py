import re

def clean_text(texts):
    cleaned = []

    for t in texts:
        t = t.strip()
        t = re.sub(r'[^a-zA-Z0-9 ₹.]', ' ', t)

        if len(t) > 2:
            cleaned.append(t)

    return cleaned
