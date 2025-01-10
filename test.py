import streamlit as st #this library is used for creating UI
import os #for environment variable management
from utils import *

def main():
    st.set_page_config(page_title="PDF summarizer")

    st.title("PDF Summarizing App")
    st.write("Summarize your pdf files in just a few seconds.")
    st.divider()

    pdf=st.file_uploader("Upload your pdf document",type="pdf")

    submit =st.button("Generate Summary")

    os.environ["OPEN_AI_KEY"]="XXXXXXXXXXXXX"
    # os.environ["OPEN_AI_KEY"] = os.getenv("XXXXXXXXXXXXXXXXXXXXXX")


    if submit:
        response=summarizer(pdf)
        st.subheader("Summary of File:")
        st.write(response)


if __name__=="__main__":
    main()
