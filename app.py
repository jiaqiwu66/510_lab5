import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def generate_content(user_request, season, duration, people, style, transport):
    prompt = f"""
    You are an expert at planning overseas trips.
    Your are good at finding local food and excellent restaurants.

    Please take the user's request and plan a comprehensive trip for them.
    Have a summary of user request and plan the trip accordingly.
    Give resturant reservation information and local food recommendations for each day

    Travel season: {season}
    Duration of the trip: {duration} days
    Number of people: {people}
    Travel style: {style}
    Transportation: {transport}

    User's request:
    {user_request}
    """

    response = model.generate_content(prompt)
    return response.text

st.title(" 🏖️Taste Trekker")
st.subheader("Your Personal Travel Planner Good at Finding Local Food and Excellent Restaurants")

# User Inputs
user_request = st.text_area("Enter your travel request (destination, activities, etc.):")
season = st.selectbox("Select the travel season:", options=["Spring", "Summer", "Autumn", "Winter"])
duration = st.slider("Choose the duration of the trip (days):", min_value=1, max_value=30)
people = st.number_input("Enter the number of people traveling:", min_value=1, max_value=50)
style = st.selectbox("Select the travel style:", options=["Romantic", "Fulfilling", "Relaxed", "Excited"])
transport = st.selectbox("Choose your preferred transportation:", options=["Car", "Public Transport", "Bicycle", "Plane"])

if st.button("Generate Travel Plan"):
    reply = generate_content(user_request, season, duration, people, style, transport)
    st.write(reply)
