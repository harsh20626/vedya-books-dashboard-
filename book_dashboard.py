import streamlit as st
import os

# Set the title of the dashboard
st.markdown("<h1 style='text-align: center; font-weight: bold;'>Vedya Books</h1>", unsafe_allow_html=True)

# Define the price categories, including new categories
price_categories = {
    "Books Priced from Rs. 5": 5,
    "Books priced at Rs. 150": 150,
    "Books priced at Rs. 180": 180,
    "Books priced at Rs. 200": 200,
    "Books priced at Rs. 300": 300,
    "Stickers priced at Rs. 30": 30,
    "Wallpapers priced at Rs. 50": 50,
    "wallpaper with Frame priced at Rs. 100": 100,
}

# Create a folder structure for images
for folder_name in price_categories.keys():
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Display the folders and images
st.header("Books Sorted by Pricing")

for folder_name in price_categories.keys():
    if st.button(folder_name):
        images = os.listdir(folder_name)
        
        st.subheader(folder_name)
        cols = st.columns(3)  # Create 3 columns for grid view
        for i, image in enumerate(images):
            image_path = os.path.join(folder_name, image)
            with cols[i % 3]:  # Distribute images across columns
                st.image(image_path, caption=image, use_container_width=True)
                if st.button(f"View {image}"):
                    st.image(image_path, caption=image, use_container_width=True)

# Add styling to use Poppins font
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
<style>
    body {
        font-family: 'Poppins', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

st.write("Contacts: Phone No. 9315791917 or Instagram: @Vedyabooks")
