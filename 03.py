class ShoppingCart:
    def __init__(self):
        # Dictionary to store items and their prices
        self.items = {}

    def add_item(self, item, price, quantity=1):
        """Add items to the shopping cart."""
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"{quantity} {item}(s) added to the cart.")

    def remove_item(self, item, quantity=1):
        """Remove items from the shopping cart."""
        if item in self.items:
            if self.items[item] >= quantity:
                self.items[item] -= quantity
                print(f"{quantity} {item}(s) removed from the cart.")
                if self.items[item] == 0:
                    del self.items[item]
            else:
                print(f"Insufficient quantity of {item} in the cart.")
        else:
            print(f"{item} not found in the cart.")

    def calculate_total_price(self, prices):
        """Calculate the total price of items in the shopping cart."""
        total_price = 0
        for item, quantity in self.items.items():
            if item in prices:
                total_price += prices[item] * quantity
            else:
                print(f"Price for {item} not found. Please set the price.")
        return total_price

# Example usage:
shopping_cart = ShoppingCart()

# Add items to the cart
shopping_cart.add_item("Apple", price=2.0, quantity=3)
shopping_cart.add_item("Banana", price=1.0, quantity=2)

# Display the items in the cart
print("Current items in the cart:")
for item, quantity in shopping_cart.items.items():
    print(f"{quantity} {item}(s)")

# Remove items from the cart
shopping_cart.remove_item("Apple", quantity=2)

# Display the updated items in the cart
print("Updated items in the cart:")
for item, quantity in shopping_cart.items.items():
    print(f"{quantity} {item}(s)")

# Calculate and display the total price
item_prices = {"Apple": 2.0, "Banana": 1.0}
total_price = shopping_cart.calculate_total_price(item_prices)
print(f"Total price of items in the cart: ${total_price}")
