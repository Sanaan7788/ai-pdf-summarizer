import streamlit as st #this library is used for creating UI
import os #for environment variable management

def main():
    st.set_page_config(page_title="PDF summarizer")

    st.title("PDF Summariing App")
    st.write("Summarize your pdf files in just a few seconds.")
    st.divider()

    pdf=st.file_uploader("Upload your pdf document",type="pdf")

    submit =st.button("Generate Summary")

    if __name__=="__main__":
        main()
