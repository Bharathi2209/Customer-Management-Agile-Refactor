# test_customer.py

import unittest
import os
import json
from refactored_customer_module import Customer, CustomerRepository

class TestCustomerRepository(unittest.TestCase):
    def setUp(self):
        # Use a test file to avoid modifying real data
        self.test_file = "test_customers.json"
        self.repo = CustomerRepository(filename=self.test_file)
        self.repo.customers = []  # Clear in-memory list
        self.repo.save_to_file()

    def tearDown(self):
        # Remove the test file after tests
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_customer(self):
        customer = Customer("John Doe", "john@example.com", "1234567890")
        result = self.repo.add_customer(customer)
        self.assertEqual(result, "✅ Customer added successfully!")
        self.assertEqual(len(self.repo.customers), 1)

    def test_duplicate_customer(self):
        customer = Customer("John Doe", "john@example.com", "1234567890")
        self.repo.add_customer(customer)
        result = self.repo.add_customer(customer)
        self.assertEqual(result, "⚠️ Customer with this email already exists.")
        self.assertEqual(len(self.repo.customers), 1)

    def test_get_customer(self):
        customer = Customer("Alice", "alice@example.com", "1112223333")
        self.repo.add_customer(customer)
        found = self.repo.get_customer("alice@example.com")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Alice")

    def test_delete_customer(self):
        customer = Customer("Bob", "bob@example.com", "9998887777")
        self.repo.add_customer(customer)
        result = self.repo.delete_customer("bob@example.com")
        self.assertEqual(result, "🗑️ Customer deleted successfully.")
        self.assertEqual(len(self.repo.customers), 0)

    def test_delete_nonexistent_customer(self):
        result = self.repo.delete_customer("notfound@example.com")
        self.assertEqual(result, "❌ Customer not found.")

    def test_list_customers(self):
        c1 = Customer("John", "john@example.com", "123")
        c2 = Customer("Jane", "jane@example.com", "456")
        self.repo.add_customer(c1)
        self.repo.add_customer(c2)
        customers = self.repo.list_customers()
        self.assertEqual(len(customers), 2)
        self.assertEqual(customers[0].name, "John")
        self.assertEqual(customers[1].name, "Jane")


if __name__ == '__main__':
    unittest.main()
