import resend
import streamlit as st

# Set up the Streamlit app
st.set_page_config(page_title="Resender", page_icon="✉️", layout="centered")

with st.sidebar:
    st.header("Settings")
    resend_api_key = st.text_input("Resend API key", type="password")
st.subheader("✉️ Resender")

# Email form inside a container
with st.container():
    with st.form("email_form"):
        col1, col2 = st.columns(2)
        with col1:
            email_from = st.text_input("From", placeholder="sender@example.com")
        with col2:
            email_to = st.text_input("To", placeholder="recipient@example.com")

        email_subject = st.text_input("Subject", placeholder="Your subject here...")
        email_body = st.text_area("Message", placeholder="Your message here...", height=200)

        submitted = st.form_submit_button("Send Email")

    if submitted:
        if not (resend_api_key.strip() and email_from.strip() and email_to.strip() and email_subject.strip() and email_body.strip()):
            st.error('Please provide all required fields.')
        else:
            try:
                with st.spinner("Sending email..."):
                    resend.api_key = resend_api_key       
                    email = resend.Emails.send({
                        "from": email_from,
                        "to": [email_to],
                        "subject": email_subject,
                        "html": f"<strong>{email_body}</strong>",
                        "text": f"{email_body}"
                    })
                    st.success(f"Email sent to {email_to} successfully!")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
