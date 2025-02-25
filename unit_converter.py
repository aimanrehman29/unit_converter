import streamlit as st
import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        rate = data["rates"].get(to_currency, None)
        if rate:
            return amount * rate
        else:
            return "Invalid currency code!"
    except:
        return "Error fetching exchange rate!"

def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371,
        "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversions = {
        ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
        ("Celsius", "Kelvin"): lambda x: x + 273.15,
        ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
        ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
        ("Kelvin", "Celsius"): lambda x: x - 273.15,
        ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32
    }
    return conversions.get((from_unit, to_unit), lambda x: x)(value)

def convert_speed(value, from_unit, to_unit):
    speed_units = {
        "Meters per Second": 1, "Kilometers per Hour": 3.6, "Miles per Hour": 2.23694,
        "Feet per Second": 3.28084
    }
    return value * (speed_units[to_unit] / speed_units[from_unit])

st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("🌟 Pro Unit Converter")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Length", "Weight", "Temperature", "Speed", "Currency"])

with tab1:
    st.subheader("📏 Length Converter")
    value = st.number_input("Enter value:", min_value=0.0, format="%.6f", key="length_value")
    from_unit = st.selectbox("From:", ["Meters", "Kilometers", "Miles", "Yards", "Feet", "Inches"], key="length_from")
    to_unit = st.selectbox("To:", ["Meters", "Kilometers", "Miles", "Yards", "Feet", "Inches"], key="length_to")
    if st.button("Convert Length"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")

with tab2:
    st.subheader("⚖️ Weight Converter")
    value = st.number_input("Enter value:", min_value=0.0, format="%.6f", key="weight_value")
    from_unit = st.selectbox("From:", ["Kilograms", "Grams", "Pounds", "Ounces"], key="weight_from")
    to_unit = st.selectbox("To:", ["Kilograms", "Grams", "Pounds", "Ounces"], key="weight_to")
    if st.button("Convert Weight"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")

with tab3:
    st.subheader("🌡️ Temperature Converter")
    value = st.number_input("Enter temperature:", format="%.2f", key="temp_value")
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_from")
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_to")
    if st.button("Convert Temperature"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")

with tab4:
    st.subheader("🚀 Speed Converter")
    value = st.number_input("Enter speed:", min_value=0.0, format="%.6f", key="speed_value")
    from_unit = st.selectbox("From:", ["Meters per Second", "Kilometers per Hour", "Miles per Hour", "Feet per Second"], key="speed_from")
    to_unit = st.selectbox("To:", ["Meters per Second", "Kilometers per Hour", "Miles per Hour", "Feet per Second"], key="speed_to")
    if st.button("Convert Speed"):
        result = convert_speed(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")

with tab5:
    st.subheader("💰 Currency Converter (Live Rates)")
    value = st.number_input("Enter amount:", min_value=0.0, format="%.2f", key="currency_value")
    from_currency = st.text_input("From Currency (e.g., USD, EUR, GBP):", "USD", key="currency_from").upper()
    to_currency = st.text_input("To Currency (e.g., EUR, GBP, INR):", "EUR", key="currency_to").upper()
    if st.button("Convert Currency"):
        result = convert_currency(value, from_currency, to_currency)
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"{value} {from_currency} = {result:.2f} {to_currency}")

st.markdown("🔹 Created by Aiman Rehman")
