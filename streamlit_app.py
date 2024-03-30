import streamlit as st


# Function to translate menu options to Spanish
def translate_to_spanish(option):
    translation_dict = {
        'Home': 'Homepage',
        'Projects': 'Proyectos',
        'Contact Us': 'Contáctenos',
        'Homepage': 'Página Principal',
        'English': 'English',
        'Spanish': 'Español'
    }
    return translation_dict.get(option, option)


# Set page configuration
st.set_page_config(layout="wide")

# Set page header and footer color
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');

    body {
        margin: 0;
        padding: 0;
    }
    .sidebar {
        background-color: #c9c6b3 !important; /* Set the background color of the sidebar */
    }
    .header, .footer {
        position: fixed;
        width: 100%;
        background-color: #b5b093;
        z-index: 1000; /* Ensure the header and footer appear above other content */
    }
    .header {
        top: 0;
        left: 0;
        height: 110px; /* Adjust the height of the header to 110 pixels */
    }
    .footer {
        bottom: 0;
        left: 0;
        height: 10px; /* Adjust the height of the footer to 10 pixels */
    }
    .content {
        margin-top: 50px; /* Adjust the margin top for the content below the header */
        margin-bottom: 15px; /* Adjust the margin bottom for the content above the footer */
        padding: 20px;
        font-size: 22px; /* Set font size for the content */
        font-weight: bold; /* Make the content bold */
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 20px;
        font-family: 'Anton', sans-serif; /* Set font family to Anton */
    }
    .image-container {
        text-align: center;
        margin-bottom: 20px;
    }
    .logo-container {
        display: flex;
        align-items: center;
    }
    /* Disable pointer events on language select */
    .language-select {
        pointer-events: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo and Title in one row
col1, col2 = st.columns([1, 6])
with col1:
    st.image("/Users/randyresendiz/Downloads/Preview-3.jpg", width=75)
with col2:
    st.markdown('<div class="title">Alonzo\'s Fountains</div>', unsafe_allow_html=True)

# Sidebar title
st.sidebar.markdown('<div class="title">Alonzo\'s Fountains</div>', unsafe_allow_html=True)

# Sidebar navigation dropdown menu for Menu
menu_options_english = ['Homepage', 'Projects', 'Contact Us']
menu_options_spanish = [translate_to_spanish(option) for option in menu_options_english]
menu_option = st.sidebar.selectbox(
    'Menu',
    menu_options_spanish if st.sidebar.selectbox('Language', ['English', 'Español'],
                                                 index=0, key='language') == 'Español' else menu_options_english,
    index=0,  # Set the default index to 0 to make it non-editable
    help="Choose a page to navigate to.",
    key='menu'
)

# Header
st.markdown('<div class="header"></div>', unsafe_allow_html=True)

# Content based on menu selection
if menu_option in ['Homepage', 'Página Principal']:
    # First passage
    st.markdown('<div class="content">'
                'At Alonzo\'s, we take pride in the craftsmanship behind our beautiful selection of fountains and garden decor, designed to enhance your outdoor space.<br><br>'
                'Explore our collection to find the perfect centerpiece for your garden or patio.</div>',
                unsafe_allow_html=True)

    # Image between passages (Clickable)
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.markdown('<a href="https://example.com">', unsafe_allow_html=True)
    st.image("/Users/randyresendiz/Downloads/IMG_2639.jpg", width=int(500 * 0.7))  # 30% smaller
    st.markdown('</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Second passage
    st.markdown(
        '<div class="content">Add charm and personality to your outdoor oasis with our garden decorations, including sculptures, benches, and more.<br><br>'
        'Create inviting gathering spaces with our durable cement tables and benches, crafted with attention to detail.<br><br>'
        'Enhance your garden\'s aesthetic with our elegant statues and sculptures, each showcasing exceptional craftsmanship that adds sophistication to any setting.<br><br>'
        'Experience the beauty of outdoor living with Alonzo\'s Fountains. Welcome to a world where every piece is a testament to exceptional artistry</div>',
        unsafe_allow_html=True)

elif menu_option == 'Projects':
    st.markdown('<div class="content">This is the Projects page content...</div>', unsafe_allow_html=True)
elif menu_option == 'Contact Us':
    st.markdown('<div class="content">This is the Contact Us page content...</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer"></div>', unsafe_allow_html=True)
