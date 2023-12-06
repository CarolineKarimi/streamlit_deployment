import streamlit as st
from multipage import MultiPage
from apps import gwd_public_db_context,gwd_public_db_summary, gwd_public_db_with_auth

# Set image URL here
image_url = 'https://workerdiaries.org/wp-content/uploads/2022/03/favicon-new.jpg'
# Set the page configuration
st.set_page_config(page_icon=image_url, layout="wide")

# Define your contact email address
contact_email = "carolinekarimi@mfopps.org"
red_markdown = "#F03E35"

# Initialize session state
if "login_status_summary" not in st.session_state:
    st.session_state.login_status_summary = False

if "login_status_detailed" not in st.session_state:
    st.session_state.login_status_detailed = False

# Landing page
st.sidebar.title("Select Dashboard")
selected_dashboard = st.sidebar.radio("options", ['Data/Dashboard context',"Summary Dashboard", "Detailed Dashboard"],label_visibility='collapsed')

# Add a contact support link at the bottom of the sidebar (visible even before login)
with st.sidebar:
    st.markdown(
        f'<a class="custom-link" href="mailto:{contact_email}?subject=Dashboard Issue&body=Please describe the issue you\'re facing." target="_blank" style="color: #1a73e8; font-size: 16px; font-style: italic;">Contact Support</a>',
        unsafe_allow_html=True,
    )

# Login form based on the selected dashboard

# Show the selected dashboard
if selected_dashboard == "Data/Dashboard context":
    gwd_public_db_context.app()
elif selected_dashboard != "Data/Dashboard context":
    with st.sidebar.form("Login_Form"):
        password_input = st.text_input("Enter Password", type="password", key="password_input")

        if selected_dashboard == "Summary Dashboard":
            login_button = st.form_submit_button("Login")

            if login_button and password_input == "~89Wg2t9@W*d":
                st.session_state.login_status_summary = True
            elif login_button and password_input != "~89Wg2t9@W*d":
                st.markdown(f'<p style="color:{red_markdown}; font-size: 14px; font-style: italic;">Please enter a valid password</p>', unsafe_allow_html=True)

        elif selected_dashboard == "Detailed Dashboard":
            login_button = st.form_submit_button("Login")

            if login_button and password_input == "!ck1G;27JW5d":
                st.session_state.login_status_detailed = True
                
            elif login_button and password_input != "!ck1G;27JW5d":
                st.markdown(f'<p style="color:{red_markdown}; font-size: 14px; font-style: italic;">Please enter a valid password</p>', unsafe_allow_html=True)


# Check login status and show the selected dashboard
if st.session_state.login_status_summary and selected_dashboard == "Summary Dashboard":
    gwd_public_db_summary.app()

elif st.session_state.login_status_detailed and selected_dashboard == "Detailed Dashboard":
    gwd_public_db_with_auth.app()
    
    