import streamlit as st
import pandas as pd
from database import create_table, add_expense, get_expenses, get_total
from datetime import date

# Initialize DB
create_table()

st.title("Simple Expense Tracker")

menu = ["Add Expense", "View Expenses"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- ADD EXPENSE ----------------
if choice == "Add Expense":
    st.subheader("Add New Expense")

    amount = st.number_input("Amount", min_value=0.0)
    category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
    description = st.text_input("Description")
    expense_date = st.date_input("Date", date.today())

    if st.button("Add"):
        add_expense(amount, category, description, str(expense_date))
        st.success("Expense Added!")

# ---------------- VIEW EXPENSE ----------------
elif choice == "View Expenses":
    st.subheader("All Expenses")

    data = get_expenses()

    if data:
        df = pd.DataFrame(data, columns=["ID", "Amount", "Category", "Description", "Date"])
        st.dataframe(df)

        total = get_total()
        st.write(f"### Total Spent: ₹ {total if total else 0}")

        st.subheader("Category Breakdown")
        category_sum = df.groupby("Category")["Amount"].sum()
        st.bar_chart(category_sum)

    else:
        st.warning("No expenses yet.")
