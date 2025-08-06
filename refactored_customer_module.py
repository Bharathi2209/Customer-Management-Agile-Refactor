# refactored_customer_module.py

import json
from typing import List, Optional

class Customer:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {"name": self.name, "email": self.email, "phone": self.phone}

    @staticmethod
    def from_dict(data):
        return Customer(data["name"], data["email"], data["phone"])

    def __str__(self):
        return f"{self.name} | {self.email} | {self.phone}"


class CustomerRepository:
    def __init__(self, filename: str = "customers.json"):
        self.filename = filename
        self.customers: List[Customer] = []
        self.load_from_file()

    def add_customer(self, customer: Customer) -> str:
        if self.get_customer(customer.email) is None:
            self.customers.append(customer)
            self.save_to_file()
            return "✅ Customer added successfully!"
        return "⚠️ Customer with this email already exists."

    def get_customer(self, email: str) -> Optional[Customer]:
        return next((c for c in self.customers if c.email == email), None)

    def delete_customer(self, email: str) -> str:
        original_count = len(self.customers)
        self.customers = [c for c in self.customers if c.email != email]
        if len(self.customers) < original_count:
            self.save_to_file()
            return "🗑️ Customer deleted successfully."
        return "❌ Customer not found."

    def list_customers(self) -> List[Customer]:
        return self.customers

    def save_to_file(self):
        with open(self.filename, "w") as f:
            json.dump([c.to_dict() for c in self.customers], f, indent=2)

    def load_from_file(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.customers = [Customer.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.customers = []
