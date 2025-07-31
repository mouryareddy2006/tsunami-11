import streamlit as st
import pandas as pd
import numpy as np

st.title('mourya codesss')

# Dice Roller
if st.button('Roll Dice'):
    dice_roll = np.random.randint(1, 7)
    st.write(f'You rolled a: {dice_roll}')
    
# Random Number Generator
if st.button('Generate Random Number'):
    random_number = np.random.randint(0, 101)
    st.write(f'Random number between 0 and 100: {random_number}')

# Interactive Bar Chart
if st.button('Show Bar Chart'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.bar_chart(chart_data)

# Simple Calculator
st.subheader("Simple Calculator")
num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    st.write(f"Result: {result}")
