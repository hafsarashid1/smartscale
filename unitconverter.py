import streamlit as st

st.title("⚖ Smartscale")

st.markdown("### Converts Length, Weight, And Time Instantly")
st. write ("Welcome to the unit converter app!") 
st.write("Select a category", "enter a value and get the converted result in no time", )

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, units):
    if category == "Length":
        if units == "Kilometers to miles":
            return value * 0.621371
        elif units == "Miles to kilometers":
            return value / 0.621371
    elif category == "Weight":
        if units == "Pounds to kilograms":
            return value / 2.20462
        elif units == "Kilograms to pounds":
            return value * 2.20462
    elif category == "Time":
        if units == "seconds to minutes":
            return value / 60
        elif units == "minutes to seconds":
            return value * 60
        elif units == "minutes to hours":
            return value / 60
        elif units == "hours to minutes":
            return value * 60
        elif units == "hours to days":
            return value / 24
        elif units == "days to hours":
            return value * 24


if category == "Length":
    units = st.selectbox("📏Select a unit", ["Kilometers to miles", "Miles to kilometers"])
elif category  == "Weight":
    units = st.selectbox("📏Select a unit", ["Pounds to kilograms", "Kilograms to pounds"])
elif category == "Time":
    units = st.selectbox("📏Select a unit", ["seconds to minutes", "minutes to seconds", "minutes to hours", "hours to minutes", "hours to days", "days to hours"])
value = st.number_input("Enter a value", min_value=0.0)
if st.button("Convert"):
    result = convert_units(category, value, units)
    st.success(f"the result is {result: .2f}")
    