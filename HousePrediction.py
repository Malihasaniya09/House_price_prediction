import streamlit as st

# Title
st.title("🏡House Price Estimator")

st.markdown("""
This tool gives an approximate estimate of house pricing in Hyderabad based on:
- **Area in sqft**
- **Bedrooms**
- **Parking spaces**
- **Washrooms**

**Note**: The calculation is based on current average market rates.
""")

# Input Fields
area = st.number_input("Enter Area (in sqft):", min_value=200, max_value=10000, step=50)
bedrooms = st.number_input("Number of Bedrooms:", min_value=0, max_value=10, step=1)
parking = st.number_input("Number of Parking Lots:", min_value=0, max_value=5, step=1)
washrooms = st.number_input("Number of Washrooms:", min_value=0, max_value=10, step=1)

# Prediction Formula
def predict_price(area, bedrooms, parking, washrooms):
    price = (area * 7000) + (bedrooms * 700000) + (parking * 250000) + (washrooms * 250000)
    return price

# Predict Button
if st.button("Predict Price"):
    predicted_price = predict_price(area, bedrooms, parking, washrooms)
    st.success(f"Estimated House Price in Hyderabad: ₹{predicted_price:,.0f}")
