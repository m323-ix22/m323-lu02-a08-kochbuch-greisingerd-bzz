'''
Passt die Mengenangaben in einem Rezept an die Anzahl der Personen an.
'''

import json

def load_recipe(recipe_str):
    '''Lädt ein Rezept aus einem JSON-String und gibt es als Dictionary zurück.'''
    return json.loads(recipe_str)

def adjust_recipe(recipe_dict, num_people):
    '''Passt die Mengenangaben des Rezepts an eine neue Anzahl von Personen an.'''
    factor = num_people / recipe_dict['servings']
    adjusted_ingredients = {
        ingredient: amount * factor
        for ingredient, amount in recipe_dict['ingredients'].items()
    }
    return {
        'title': recipe_dict['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_people
    }

if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json_str = (
        '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
        '"Minced Meat": 500}, "servings": 4}'
    )

    # Rezept laden
    loaded_recipe = load_recipe(recipe_json_str)

    # Rezept für eine neue Anzahl an Personen anpassen
    adjusted_recipe = adjust_recipe(loaded_recipe, 2)

    # Angepasstes Rezept anzeigen
    print('Angepasstes Rezept:', json.dumps(adjusted_recipe, indent=4))
