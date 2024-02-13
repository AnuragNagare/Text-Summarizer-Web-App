import streamlit as st
from transformers import pipeline

# Function for abstractive summarization
def abstractive_summarizer(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    return summary[0]['summary_text']

def main():
    st.title("Text Summarizer Web App")
    
    # Text input box for user input
    user_input = st.text_area("Enter the text you want to summarize:")

    # Summarize button
    if st.button("Summarize"):
        if user_input:
            # Perform summarization
            summary_result = abstractive_summarizer(user_input)

            # Display the summarized text
            st.subheader("Generated Summary:")
            st.write(summary_result)
        else:
            st.warning("Please enter some text to summarize.")

if __name__ == "__main__":
    main()
