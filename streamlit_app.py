# streamlit_app.py

import streamlit as st
from refactored_customer_module import Customer, CustomerRepository

# Load the repo (JSON-based)
repo = CustomerRepository()

st.title("👤 Customer Management System")
st.markdown("Agile Refactored with Streamlit 🌐")

# Sidebar Navigation
menu = st.sidebar.radio("Navigate", ["➕ Add", "📄 View All", "🔍 Search", "🗑️ Delete"])

# Add Customer
if menu == "➕ Add":
    st.subheader("Add New Customer")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")

    if st.button("Add Customer"):
        if name and email and phone:
            customer = Customer(name, email, phone)
            msg = repo.add_customer(customer)
            st.success(msg)
        else:
            st.warning("Please fill all fields.")

# View All Customers
elif menu == "📄 View All":
    st.subheader("All Customers")
    customers = repo.list_customers()
    if customers:
        data = [{"Name": c.name, "Email": c.email, "Phone": c.phone} for c in customers]
        st.dataframe(data)
    else:
        st.info("No customers found.")

# Search
elif menu == "🔍 Search":
    st.subheader("Search Customer by Email")
    search_email = st.text_input("Enter Email")
    if st.button("Search"):
        customer = repo.get_customer(search_email)
        if customer:
            st.success(f"✅ Found: {customer.name} | {customer.phone}")
        else:
            st.error("❌ Customer not found.")

# Delete
elif menu == "🗑️ Delete":
    st.subheader("Delete Customer by Email")
    del_email = st.text_input("Enter Email to Delete")
    if st.button("Delete"):
        result = repo.delete_customer(del_email)
        st.warning(result)
