# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tHhFus-vgwvT90Sbs43dc8NxXzY7eXOZ
"""

import streamlit as st
import openai
import json

# Set your OpenAI API key
openai.api_key = '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'

def generate_suggestions(resume_text, job_profile):
    # Start the chat with the introduction of the assistant and the text from the file
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"I have this resume: {resume_text}. I am applying for a {job_profile} role. Can you suggest improvements?"},
    ]

    # Generate the suggestions
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    # Return the assistant's reply
    return response['choices'][0]['message']['content']

def main():
    # Streamlit app title
    st.title("Resume Analysis and Job Matching App")

    # File upload widget
    uploaded_file = st.file_uploader("Upload your resume", type=["txt"])
    job_profile = st.text_input("Enter the job profile")

    if uploaded_file is not None and job_profile:
        # Read the content of the uploaded file
        resume_text = uploaded_file.read().decode("utf-8")

        # Display the content of the uploaded file
        st.subheader("Uploaded Resume:")
        st.write(resume_text)

        # Analyze resume button
        if st.button("Analyze Resume"):
            suggestions = generate_suggestions(resume_text, job_profile)

            # Display the analysis results
            st.subheader("Analysis Results:")
            st.write(f"Suggestions: {suggestions}")

if __name__ == "__main__":
    main()
