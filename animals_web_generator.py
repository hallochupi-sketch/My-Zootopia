import json
from pathlib import Path


DATA_FILE = Path("animals_data.json")
TEMPLATE_FILE = Path("animals_template.html")
OUTPUT_FILE = Path("animals.html")


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Step 4-style HTML for a single animal"""
    name = animal_obj.get("name", "")
    chars = animal_obj.get("characteristics") or {}
    locations = animal_obj.get("locations") or []

    diet = chars.get("diet")
    type_ = chars.get("type")
    location = locations[0] if locations else None

    # Only build the lines that exist
    lines = []
    if diet:
        lines.append(f'<strong>Diet:</strong> {diet}<br/>')
    if location:
        lines.append(f'<strong>Location:</strong> {location}<br/>')
    if type_:
        lines.append(f'<strong>Type:</strong> {type_}<br/>')

    # If an animal has no info at all, skip it
    if not lines:
        return ""

    output = ''
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'
    for line in lines:
        output += f'      {line}\n'
    output += '  </p>\n'
    output += '</li>\n'

    return output


def build_animals_html(data):
    """Builds the concatenated HTML for all animals"""
    output = ''
    for animal in data:
        output += serialize_animal(animal)
    return output


def main():
    # Step 1: load JSON
    animals_data = load_data(DATA_FILE)

    # Step 2–4: read template, inject HTML, write animals.html
    template = TEMPLATE_FILE.read_text(encoding="utf-8")

    animals_html = build_animals_html(animals_data)

    new_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    OUTPUT_FILE.write_text(new_html, encoding="utf-8")


if __name__ == "__main__":
    main()
