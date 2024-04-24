# Taste Trekker
## Overview
Your Personal Travel Planner Good at Finding Local Food and Excellent Restaurants.  
App webpage: https://510lab5-h6zqccxtpvlfxolaukcxew.streamlit.app/

Contains 2 parts:
- Generate template for AI's answer.(Prompt engineering)
- User input interface in web app.

## Getting Started
- Get an API key in Google
- Create a streamlit app using Gemini API
- Add prompts to "train the answering way"

## Lessons Learned
- To get specific information from user to help with prompt engineering, try to add in this way in prompt:
    ```
    Travel season: {season}
    Duration of the trip: {duration} days
    Number of people: {people}
    Travel style: {style}
    Transportation: {transport}
    ```
- To make sure the AI considering the users' input as constrains, you can give some requirement like this ``` Have a summary of user request and plan the trip accordingly.```

## Question
- I try to ask Gemini give ```URL for the restaurant``` but found most of the URL are fake. Is there any good way to avoid this?
- I also tried to ask Gemini help me ```PIN the destinations in Google map``` but failed. How can I do that? I think the destinations' name is real but how to PIN them in map?

Todo
- Fix the questions above. As I think most of the name is real so it can be solved.