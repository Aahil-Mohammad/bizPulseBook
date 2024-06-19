import streamlit as st
import os
from streamlit_supabase_auth import login_form, logout_button

os.environ["SUPABASE_URL"] = "https://cweordholuvkdavqvzlz.supabase.co"
os.environ["SUPABASE_KEY"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN3ZW9yZGhvbHV2a2RhdnF2emx6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTgxMjc1NDIsImV4cCI6MjAzMzcwMzU0Mn0.K7NsU8WCDOwcONLabLCGp7o_RJl02Z4YPopH9okUiUQ"

session = login_form(
    url="https://cweordholuvkdavqvzlz.supabase.co",
    apiKey="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN3ZW9yZGhvbHV2a2RhdnF2emx6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTgxMjc1NDIsImV4cCI6MjAzMzcwMzU0Mn0.K7NsU8WCDOwcONLabLCGp7o_RJl02Z4YPopH9okUiUQ",
    providers=["google"]
)

# Get the value of the 'page' query parameter
page = st.query_params["page"]

with st.sidebar:
    logout_button()
