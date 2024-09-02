"""
Passt die Mengenangaben in einem Rezept an die Anzahl der Personen an.
"""

import json


def load_recipe(recipe_json):
    """Lädt ein Rezept aus einem JSON-String und gibt es als Dictionary zurück."""
    return json.loads(recipe_json)


def adjust_recipe(recipe, num_people):
    """Passt die Mengenangaben des Rezepts an eine neue Anzahl von Personen an."""
    factor = num_people / recipe['servings']
    adjusted_ingredients = {
        ingredient: amount * factor
        for ingredient, amount in recipe['ingredients'].items()
    }
    return {
        "title": recipe['title'],
        "ingredients": adjusted_ingredients,
        "servings": num_people
    }


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'

    # Rezept laden
    recipe = load_recipe(recipe_json)

    # Rezept für eine neue Anzahl an Personen anpassen
    adjusted_recipe = adjust_recipe(recipe, 2)

    # Angepasstes Rezept anzeigen
    print("Angepasstes Rezept:", json.dumps(adjusted_recipe, indent=4))
