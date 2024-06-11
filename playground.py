# import streamlit as st
# import requests
# import sys
# from st_login_form import login_form


# ## Define functions
# #get books
# def retrieve_book(query,page=1):
#     url = f"https://openlibrary.org/search.json?q={query}&page={page}"
#     response = requests.get(url)
#     return response.json()

# #show query result books

# def show_books(books):
#     for book in books.get('docs',[]):
#         title=book.get('title','no title')
#         author = book.get('author_name', 'No authors')
#         publish_year = book.get('first_publish_year', 'No publish year')
#         book_key = book.get('key')
#         cover_id = book.get('cover_i')
#         cover_url = f"http://covers.openlibrary.org/b/id/{cover_id}-L.jpg" if cover_id else ""
#         more_info = f"https://openlibrary.org{book_key}"
#         if cover_url:
#             st.image(cover_url, width=150)
#         st.header(title)
#         st.write(author)
#         st.write(publish_year)
#         st.write(f"[More Info]({more_info})")
# #Search button
# search_button = """
#    <style>
# .custom-button {
#     background-color: white;
#     color: black;
#     padding: 6px 30px 8px;
#     border: 2px solid grey;
#     border-radius: 10px;
#     cursor: pointer;
#     font-size: 15px;
#     margin-top: 28px;
# }
# .custom-button:hover {
#     color: #009193;
#     border: 2px solid #009193;
# }
# .custom-button:active {
#     background-color: #009193;
#     border:2px solid #009193;
#     color:white;
# }
# </style>
# <button class="custom-button">Search</button>
#     """

# random_button = """
#    <style>
# .custom-button {
#     background-color: white;
#     color: black;
#     padding: 5px 10px 8px;
#     border: 2px solid grey;
#     border-radius: 10px;
#     cursor: pointer;
#     font-size: 15px;
#     margin-top: 28px;
# }
# .custom-button:hover {
#     color: #009193;
#     border: 2px solid #009193;
# }
# .custom-button:active {
#     background-color: #009193;
#     border:2px solid #009193;
#     color:white;
# }
# </style>
# <button class="custom-button">Suggest a book</button>
#     """

# if 'show_selectbox' not in st.session_state:
#     st.session_state.show_selectbox = False

# # Define a function to toggle the selectbox
# def toggle_selectbox():
#     st.session_state.show_selectbox = not st.session_state.show_selectbox


    

# # Custom title
# st.markdown("<h1 style='margin-left:-50px; text-align:center; font-size:36px; margin-top: -50px'>Welcome to <br> <span style= color:#009193> BizPulse's</span> Book Tracker</h1>", unsafe_allow_html=True)

# st.sidebar.title("Search Book, Your Library, Book Suggester")
# # Create columns
# col1, col2, col3 = st.columns([0.6,0.2,0.2])

# # Custom CSS for styling
# # Create the login form
# # Custom CSS for styling
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #f0f2f6;
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         height: 100vh;
#     }
#     .container {
#         width: 400px;
#         padding: 2rem;
#         background-color: white;
#         border-radius: 10px;
#         box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
#         text-align: center;
#     }
#     .title {
#         font-size: 2rem;
#         font-weight: bold;
#         margin-bottom: 1rem;
#         color: #009193;
#         text-align: center;
#     }
#     .input-field {
#         width: 100%;
#         padding: 0.75rem;
#         margin: 0.5rem 0;
#         font-size: 1rem;
#         border: 1px solid #ccc;
#         border-radius: 5px;
#     }
#     .button {
#         width: 100%;
#         padding: 0.75rem;
#         font-size: 1.25rem;
#         background-color: #009193;
#         color: white;
#         border: none;
#         border-radius: 5px;
#         cursor: pointer;
#         transition: background-color 0.3s ease;
#     }
#     .button:hover {
#         background-color: #00796b;
#     }
#     .footer {
#         margin-top: 1rem;
#         color: #666;
#     }
#     .link {
#         margin-top: 1rem;
#         color: #009193;
#         cursor: pointer;
#         text-decoration: underline;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Define the login function
# # def login_page():
# #     st.markdown('<div class="container">', unsafe_allow_html=True)
# #     st.image("C:/Users/Aahil/OneDrive/Documents/Projects/BookTrackerAndSuggester/logo-color.png", width=100)
# #     st.markdown('<div class="title">Login</div>', unsafe_allow_html=True)
# #     username = st.text_input("Email", placeholder="Your Email", key="login_email")
# #     password = st.text_input("Password", type="password", placeholder="Your Password", key="login_password")

# #     if st.button("Login"):
# #         if username == "admin" and password == "password":
# #             st.success("Login successful!")
# #         else:
# #             st.error("Invalid username or password")

# #         if st.button("Go to Register"):
# #             st.session_state.page = 'register'


# streamlit_app.py

import streamlit as st
from st_supabase_connection import SupabaseConnection

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Perform query.
rows = conn.query("*", table="mytable", ttl="10m").execute()

# Print results.
for row in rows.data:
    st.write(f"{row['name']} has a :{row['pet']}:")