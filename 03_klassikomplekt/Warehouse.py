class Product:
    """Represents an individual item in the warehouse."""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - Price: {self.price}€, Qty: {self.quantity}"

class Warehouse:
    """The storage class that manages Product instances."""
    def __init__(self, location):
        self.location = location
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)
        print(f"Added {product.name} to the {self.location} warehouse.")

    def show_inventory(self):
        print(f"\n--- Inventory for {self.location} ---")
        if not self.inventory:
            print("Warehouse is empty.")
        for item in self.inventory:
            print(item)
        print("---------------------------------")

# Example warehouse

def function():
    
    #Create warehouse
    my_warehouse = Warehouse("Tallinn Hub")
    
    #Creates 3 products
    item1 = Product("Laptop", 1200, 5)
    item2 = Product("Mouse", 25, 50)
    item3 = Product("Monitor", 300, 10)
    
    #Adds 3 products
    my_warehouse.add_product(item1)
    my_warehouse.add_product(item2)
    my_warehouse.add_product(item3)

    # Display inventory
    my_warehouse.show_inventory()

if __name__ == "__main__":
    function()