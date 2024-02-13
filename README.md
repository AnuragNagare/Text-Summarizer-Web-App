# Text-Summarizer-Web-App

This repository contains a simple web app built using Streamlit and the Hugging Face Transformers library for abstractive summarization of text.

How to Use

Run the Web App:

Execute the main script: python app.py
Open the provided link in your browser.

Usage:
Enter the text you want to summarize in the input box.
Click the "Summarize" button to generate the summary.

Code Overview
Libraries Used:
Streamlit
Hugging Face Transformers

Functionality:
The abstractive_summarizer function uses the Hugging Face Transformers library to perform abstractive summarization on the input text.
The web app provides a text area for the user to input the text they want to summarize.
Upon clicking the "Summarize" button, the app calls the summarization function and displays the generated summary.

Parameters for Summarization:
max_length: Maximum length of the summary.
min_length: Minimum length of the summary.
length_penalty: Parameter controlling the length of the summary.
num_beams: Number of beams for beam search during summarization.
early_stopping: Whether to stop the search when at least num_beams sentences are finished per batch.



https://github.com/AnuragNagare/Text-Summarizer-Web-App/assets/85473989/5422189f-4cf8-4e85-aa14-351779632959

