import streamlit as st
st.set_page_config(page_title="mango", 
                   page_icon="4463971.png",
                   layout="wide")
st.title("welcome")
tab1,tab2=st.tabs(["Main","Second"])
with tab1:
    st.header("Main")
    st.write("This is the main tab.")
    col1,col2=st.columns([1,2])
    with col1:
        st.image("images.jpg", caption="ilovemangoes",width=300)
    with col2:
        st.subheader("Mangoes are delicious fruits that are loved by many people around the world. They come in various varieties and are known for their sweet and juicy flavor.")
        st.write("Mangoes are not only tasty but also packed with nutrients, making them a healthy choice for a snack or dessert.")
        st.write("In addition to being enjoyed fresh, mangoes can be used in a variety of recipes, including smoothies, salads, and desserts.")
        st.write("Overall, mangoes are a versatile and delightful fruit that can be enjoyed in many different ways.")
        with st.container():
            st.success("Mangoes are a great source of vitamins and minerals, including vitamin C, vitamin A, and potassium.")
            st.warning("However, some people may be allergic to mangoes, so it's important to be cautious if you have a known allergy.")
            st.markdown("For more information about mangoes, you can visit the [Mango Board](https://www.mango.org/) website.")
            st.markdown("You can also check out the [Mango Recipes](https://www.allrecipes.com/recipes/16792/fruits-and-vegetables/fruits/mango/) page for delicious ways to enjoy mangoes.")
            