import re

def structure_menu(texts):
    menu = []

    for t in texts:
        match = re.search(r'(.+?)\s+(\d+)', t)

        if match:
            item = match.group(1)
            price = match.group(2)

            menu.append({
                "item": item,
                "price": price,
                "category": "Unknown"
            })

    return menu
