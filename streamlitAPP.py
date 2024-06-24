import traceback
from src.mcq_generator.utils import read_file
import streamlit as st
from src.mcq_generator.MCQGenerator import generate_evaluate_chain


# Create a title for the app
st.title("MCQs Creator Application with LangChain 🦜⛓️")

# Create a form using st.form
with st.form("user_inputs"):
    # File Upload
    uploaded_file = st.file_uploader("Upload a PDF or txt file")

    # Input Fields
    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=50)

    # Subject
    subject = st.text_input("Insert Subject", max_chars=20)

    # Quiz Tone
    tone = st.text_input("Complexity Level Of Questions", max_chars=20, placeholder="Simple")

    # Add Button
    button = st.form_submit_button("Create MCQs")

    # Check if the button is clicked and all fields have input
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Loading..."):
            try:
                text = read_file(uploaded_file)
                response = generate_evaluate_chain(
                    {
                        "text": text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone": tone
                    }
                )
                
                # Displaying the MCQs in a more attractive way
                if "quiz" in response:
                    st.success("MCQs Generated Successfully!")
                    st.markdown(response["quiz"])
                else:
                    st.error("No MCQs found in the response. Please check the input and try again.")

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error(f"Error: {e}")
