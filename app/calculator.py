def calculate_total(price, quantity):
    try:
        p = float(price)
        q = int(quantity)
        if p < 0 or q < 0:
            raise ValueError("Values cannot be negative")
        return p * q
    except ValueError:
        return None
def main():
    print("--- Shopping Bill Calculator ---")
    print("1. Calculate Total Bill")
    print("2. Exit")
    
    choice = input("Enter choice (1-2): ")
    if choice == '1':
        price = input("Enter item price: ")
        quantity = input("Enter quantity: ")
        total = calculate_total(price, quantity)
        if total is not None:
            print(f"Total Bill: ${total:.2f}")
        else:
            print("Invalid input values entered.")
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
