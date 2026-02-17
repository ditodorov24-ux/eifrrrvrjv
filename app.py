import streamlit as st

# -------- INITIAL BOOK DATABASE (Session State) --------
if "books" not in st.session_state:
    st.session_state.books = [
        "Nothing can hurt me",
        "The green mile",
        "Coupa mia",
        "The Hobbit",
        "The catcher in the Rye"
    ]

# ----------- APP TITLE ---------
st.title("My Book Library")

st.subheader("Available Books:")

# Показване на книгите
for book in st.session_state.books:
    st.write(f"- {book}")

# ----------- ADD NEW BOOK -----------
st.subheader("Add a New Book")

new_book = st.text_input("Enter book name:")

if st.button("Add Book"):
    if new_book:
        st.session_state.books.append(new_book)
        st.success(f'"{new_book}" added successfully!')
    else:
        st.warning("Please enter a book name.")

