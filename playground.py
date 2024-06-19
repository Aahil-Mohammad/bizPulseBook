import streamlit as st
import os
from streamlit_supabase_auth import login_form, logout_button

os.environ["SUPABASE_URL"] = "https://cweordholuvkdavqvzlz.supabase.co"
os.environ["SUPABASE_KEY"] = "your_supabase_key_here"

session = login_form(
    url="https://cweordholuvkdavqvzlz.supabase.co",
    apiKey="your_supabase_api_key_here",
    providers=["google"]
)

# Check if 'page' exists in query params
page = st.query_params.get("page", None)

if page == "success":
    st.write("Page is success!")

with st.sidebar:
    logout_button()
