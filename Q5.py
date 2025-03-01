import streamlit as st
import google.generativeai as genai  
genai.api_key = 'AIzaSyDp0JYpPYEk5lz--Uik5-enwM_epCbzfMM'
def generate_chatbot_response(user_input, topic):
    try:
        prompt = f"Topic: {topic}\nUser Response: {user_input}\n\nEvaluate the user's answer and give feedback."
        response = genai.Completion.create(
            engine="text-davinci-003", 
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
def main():
    st.title('AI Interview Preparation Chatbot')
    topic = st.selectbox('Select a Topic', ['Python', 'Machine Learning', 'Data Science'])
    if topic == 'Python':
        question = "What is the difference between a list and a tuple in Python?"
    elif topic == 'Machine Learning':
        question = "Can you explain the difference between supervised and unsupervised learning?"
    else:
        question = "What is the difference between structured and unstructured data?"

    st.subheader(f"Interview Question: {question}")
    user_input = st.text_area("Your Answer", "")
    
    if user_input:
        st.button('Submit Answer') 
        feedback = generate_chatbot_response(user_input, topic)
        st.subheader("Feedback")
        st.write(feedback)

if __name__ == "__main__":
    main()
