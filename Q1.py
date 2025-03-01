import streamlit as st
def generate_resume(name, skills, experience, education):
    resume = f"""
    Resume: {name}

    Skills:
    {skills}

    Experience:
    {experience}

    Education:
    {education}
    """
    return resume
def app():
    st.title("Resume Generator")
    name = st.text_input("Full Name")
    skills = st.text_area("Skills (comma separated)")
    experience = st.text_area("Work Experience (comma separated)")
    education = st.text_area("Education (comma separated)")
    if st.button("Generate Resume"):
        if name and skills and experience and education:
            resume = generate_resume(name, skills, experience, education)
            st.text(resume)
            st.download_button(
                label="Download Resume as Text",
                data=resume,
                file_name="generated_resume.txt",
                mime="text/plain"
            )
        else:
            st.error("Please fill in all fields to generate a resume.")

if __name__ == "__main__":
    app()
