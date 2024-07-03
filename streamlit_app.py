import resend
import streamlit as st

# Set up the Streamlit app
with st.sidebar:
    resend_api_key = st.text_input("Resend API Key", type="password")
st.subheader("Send Email")
email_from = st.text_input("From", "")
email_to = st.text_input("To", "")
email_subject = st.text_input("Subject", "")
email_body = st.text_area("Body", "", height=200)

# Send email using Resend
if st.button("Submit"):
    if not resend_api_key.strip() or not email_from.strip() or not email_to.strip() or not email_subject.strip() or not email_body.strip():
        st.error('Please provide the missing fields.')
    else:
        try:
            with st.spinner():
                resend.api_key = resend_api_key       
                email = resend.Emails.send({
                    "from": email_from,
                    "to": [email_to],
                    "subject": email_subject,
                    "html": f"<strong>{email_body}</strong>"
                })
                st.success(f"Email sent to {email_to} successfully!")
        except Exception as e:
            st.exception(f"An error occurred: {e}")
