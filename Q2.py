import streamlit as st
import google.generativeai as genai

# Set your OpenAI API key
genai.api_key = 'AIzaSyDp0JYpPYEk5lz--Uik5-enwM_epCbzfMM'

def analyze_sentiment(text):
    # Generate the sentiment analysis prompt
    response = genai.Completion.create(
        model="text-davinci-003",  # GPT-3 model
        prompt=f"Classify the sentiment of the following text: '{text}'",
        max_tokens=10
    )
    
    # Return the sentiment extracted from the response
    return response.choices[0].text.strip()

def main():
    st.title("Sentiment Analysis App")
    
    # User input for text
    user_input = st.text_area("Enter text to analyze:")

    if st.button("Analyze Sentiment"):
        if user_input:
            sentiment = analyze_sentiment(user_input)
            st.write(f"Sentiment: {sentiment}")
        else:
            st.write("Please enter some text!")

if __name__ == "__main__":
    main()

