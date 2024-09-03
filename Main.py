import streamlit as st
import requests

st.title("😂 Joke Generator 😂")
st.subheader("Click the button below to get a random joke!")

# Function to fetch a joke from an API
def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    joke = response.json()
    return f"{joke['setup']} - {joke['punchline']}"

# Button to generate a new joke
if st.button('Generate Joke'):
    joke = get_joke()
    st.write(f"**Joke:** {joke}")
else:
    st.write("Click the button to generate a joke!")

# Add some additional humor
st.write("Feeling down? Here's a random joke to brighten your day! 😂")

# Adding an Easter egg
if st.button("What's the best programming language?"):
    st.write("Python, of course!!! 🐍")