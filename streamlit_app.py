import os, streamlit as st
from resend import Resend

# Provide the Resend API key
client = Resend(api_key=os.environ["RESEND_API_KEY"])

# Set up the Streamlit app
st.title("Send Email")
email_from = st.text_input("From:", "")
email_to = st.text_input("To:", "")
email_subject = st.text_input("Subject:", "")
email_body = st.text_input("Body:", "")

# Send email using Resend
if st.button("Submit"):
    if not email_from or not email_to or not email_subject or not email_body:
        st.error('All fields are required. Please provide the missing information...')
    else:
        client.send_email(
            to=email_to, 
            sender=email_from, 
            subject=email_subject, 
            text=email_body
            )
        st.success(f"Email sent!")
