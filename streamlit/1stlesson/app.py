import streamlit as st
st.title ("Test")
st.write ("still a test")

user_name = st.text_input("Enter your name:")
if st.button("Submit"):
    if user_name:
        st.success(f"Hello, {user_name}!")
    else:
        st.warning("Please enter your name before submitting.")

st.subheader("Upload a photo")
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    st.image(uploaded_file, use_column_width=True)