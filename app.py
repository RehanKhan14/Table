import streamlit as st
import pandas as pd

# App title
st.title("Calculator and Table Generator")

# Tabs for Calculator and Table
tab1, tab2 = st.tabs(["Calculator", "Table Generator"])

# Calculator Tab
with tab1:
    st.header("Simple Calculator")
    
    # Input fields for numbers
    num1 = st.number_input("Enter the first number", value=0.0)
    num2 = st.number_input("Enter the second number", value=0.0)
    
    # Dropdown for selecting operation
    operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])
    
    # Perform calculation
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    
    # Display result
    st.write("Result:", result)

# Table Generator Tab
with tab2:
    st.header("Multiplication Table Generator")
    
    # Input fields for the range of the multiplication table
    num = st.number_input("Enter the number for the multiplication table", min_value=1, value=5)
    rows = st.number_input("Enter the number of rows", min_value=1, value=10)
    
    # Generate multiplication table
    data = {
        "Multiplier": [i for i in range(1, rows + 1)],
        "Result": [num * i for i in range(1, rows + 1)]
    }
    df = pd.DataFrame(data)
    
    # Display the table
    st.write(f"Multiplication Table for {num}:")
    st.dataframe(df)

    # Option to download table as CSV
    csv = df.to_csv(index=False)
    st.download_button(label="Download Multiplication Table as CSV", data=csv, file_name=f"{num}_multiplication_table.csv", mime="text/csv")
