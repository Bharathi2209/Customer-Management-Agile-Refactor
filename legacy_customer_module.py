# legacy_customer_module.py

customers = []

def add_customer(name, email, phone):
    customer = {
        'name': name,
        'email': email,
        'phone': phone
    }
    customers.append(customer)
    print("Customer added successfully!")

def get_customer(email):
    for c in customers:
        if c['email'] == email:
            print("Customer Found:", c)
            return c
    print("Customer not found.")
    return None

def delete_customer(email):
    global customers
    customers = [c for c in customers if c['email'] != email]
    print("Customer deleted if existed.")

def list_customers():
    print("Customer List:")
    for c in customers:
        print(c)

# Sample run block
if __name__ == "__main__":
    add_customer("John Doe", "john@example.com", "1234567890")
    add_customer("Jane Smith", "jane@example.com", "9876543210")

    get_customer("john@example.com")
    delete_customer("jane@example.com")
    list_customers()
