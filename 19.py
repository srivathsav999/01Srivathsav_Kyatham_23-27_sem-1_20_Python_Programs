class Ingredient:
    def __init__(self, name):
        self.name = name


class Recipe:
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return f"{self.title}\nIngredients: {', '.join(ingredient.name for ingredient in self.ingredients)}\nInstructions: {self.instructions}"


class User:
    def __init__(self, username):
        self.username = username
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def search_by_ingredient(self, ingredient_name):
        matching_recipes = []
        for recipe in self.recipes:
            ingredients = [ingredient.name.lower() for ingredient in recipe.ingredients]
            if ingredient_name.lower() in ingredients:
                matching_recipes.append(recipe)

        return matching_recipes


# Example usage:

# Create ingredients
ingredient1 = Ingredient(name="Chicken")
ingredient2 = Ingredient(name="Rice")
ingredient3 = Ingredient(name="Tomatoes")

# Create recipes
recipe1 = Recipe(title="Chicken Curry", ingredients=[ingredient1, ingredient2, ingredient3], instructions="Cook and enjoy!")
recipe2 = Recipe(title="Vegetable Stir Fry", ingredients=[ingredient2, ingredient3], instructions="Saute and serve.")

# Create a user and add recipes
user1 = User(username="Alice")
user1.add_recipe(recipe1)
user1.add_recipe(recipe2)

# Search for recipes by ingredient
ingredient_to_search = "rice"
matching_recipes = user1.search_by_ingredient(ingredient_to_search)

if matching_recipes:
    print(f"Recipes containing {ingredient_to_search}:")
    for recipe in matching_recipes:
        print(recipe)
else:
    print(f"No recipes found containing {ingredient_to_search}.")
