import streamlit as st
import google.generativeai as genai

# Configure Generative AI (Ensure API key is set securely)
#Give your correct GEMINI API KEY
genai.configure(api_key="AIzaSyDp0JYpPYEk5lz--Uik5-enwM_epCbzfMM")

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

# Code Review Section
st.title("Code Review ")
st.subheader("Code Review")

code = st.text_area("Enter your programming code to rectify the error:")

if st.button("Code Review"):
    if code.strip():
        response = model.generate_content(f"""
        Rectify the following code:
        {code}

        1. **Code Review** - Provide an overall assessment.
        2. **Error Explanation** - Highlight mistakes and why they occur.
        3. **Fixing Issues** - Suggest changes and where to apply them.
        4. **Corrected Code** - Provide a fully corrected version.
        5. **Optimization Tips** - Suggest ways to improve efficiency.

        Format the response in an easy-to-understand manner with **bold key points**.
        """)
        st.write(response.text)
    else:
        st.warning("Please enter some code before submitting.")

st.page_link("pages/app_code_review2.py", label="Help Desk")
