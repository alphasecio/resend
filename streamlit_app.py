import streamlit as st
from resend import Resend

# Set up the Streamlit app
with st.sidebar:
    resend_api_key = st.text_input("Resend API Key")
st.subheader("Send Email")
email_from = st.text_input("From", "")
email_to = st.text_input("To", "")
email_subject = st.text_input("Subject", "")
email_body = st.text_area("Body", "", height=200)

# Send email using Resend
if st.button("Submit"):
    if not resend_api_key or not email_from or not email_to or not email_subject or not email_body:
        st.error('Please provide the missing fields.')
    else:
        try:
            with st.spinner():
                client = Resend(api_key=resend_api_key)
                client.send_email(
                    to=email_to, 
                    sender=email_from, 
                    subject=email_subject, 
                    text=email_body
                    )
                st.success(f"Email sent to {email_to} successfully!")
        except Exception as e:
            st.exception(f"An error occurred: {e}")
