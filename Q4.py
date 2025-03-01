import streamlit as st
def fix_typo_in_code(code):
    fixed_code = code.replace("pritn", "print")
    return fixed_code
def main():
    st.title("Automated Code Debugging Helper")
    code_input = st.text_area("Enter your Python code here:", height=300)
    if st.button("Check Code"):
        if code_input.strip(): 
            corrected_code = fix_typo_in_code(code_input)
            st.subheader("Original Code")
            st.code(code_input, language="python")

            st.subheader("Corrected Code")
            st.code(corrected_code, language="python")
        else:
            st.warning("Please enter some Python code to check.")

if __name__ == "__main__":
    main()
