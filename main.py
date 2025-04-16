import streamlit as st

# Define pages
def index_page():
    st.title("Home Page")
    st.write("Welcome to the home page!")

def about_page():
    st.title("About Page")
    st.write("This is the about page.")

def contact_page():
    st.title("Contact Page")
    st.write("Get in touch with us.")

# Create a navigation menu
def main():
    pages = {
        "Home": index_page,
        "About": about_page,
        "Contact": contact_page,
    }

    selected_page = st.sidebar.selectbox("Select a page", list(pages.keys()))
    pages[selected_page]()

if __name__ == "__main__":
    main()
