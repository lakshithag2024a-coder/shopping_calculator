def calculate_total(price, quantity):
    try:
        p = float(price)
        q = int(quantity)
        if p < 0 or q < 0:
            raise ValueError()
        return p * q
    except ValueError:
        return None

def calculate_discounted_total(price, quantity, discount_percentage):
    try:
        base_total = calculate_total(price, quantity)
        if base_total is None:
            return None
        disc = float(discount_percentage)
        if disc < 0 or disc > 100:
            raise ValueError()
        return base_total * (1 - (disc / 100))
    except ValueError:
        return None

def main():
    print("--- Shopping Bill Calculator v2 ---")
    print("1. Calculate Total Bill")
    print("2. Calculate Bill with Discount")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    if choice == '1':
        price = input("Enter item price: ")
        quantity = input("Enter quantity: ")
        total = calculate_total(price, quantity)
        print(f"Total Bill: ${total:.2f}" if total is not None else "Invalid Input.")
    elif choice == '2':
        price = input("Enter item price: ")
        quantity = input("Enter quantity: ")
        discount = input("Enter discount percentage (0-100): ")
        total = calculate_discounted_total(price, quantity, discount)
        print(f"Discounted Bill: ${total:.2f}" if total is not None else "Invalid Input.")
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
