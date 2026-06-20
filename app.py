import streamlit as st
from PyPDF2 import PdfReader

st.title("📚 AI Study Buddy")

uploaded_file = st.file_uploader(
    "Upload your PDF Notes",
    type="pdf"
)

if uploaded_file:

    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        if page.extract_text():
            text += page.extract_text()

    st.success("PDF Uploaded Successfully ✅")

    st.subheader("Preview")

    st.write(text[:2000])
    if st.button("Generate Summary"):
        st.write(text[:500])

    question = st.text_input(
        "Ask something from notes:"
    )

    if question:

        if question.lower() in text.lower():

            st.success(
                "Answer may exist in notes ✅"
            )

        else:

            st.warning(
                "Not found in notes"
            )