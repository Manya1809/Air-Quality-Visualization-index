import streamlit as st

def app():
    st.title("**FREQUENTLY ASKED QUESTIONS**\n\n\n\n\n\n\n")
    st.write("\n\n\n\n\n\n\nQ1 **:What this site is about?**")
    st.write("A1 :blue[This site is build with the intent of visualizing the air quality trends in the India.]")
    st.write("Q2 **How past data does it cover?**")
    st.write("A2 :blue[Data from 2015 to 2020.]")
    st.write("Q3 **Is the dashboard interactive?**")
    st.write("A3 :blue[Yes dashboard is interactive.]")


    st.markdown("""
    <style>
    .big-font {
        font-size:300px!important;
    }
    </style>
    """, unsafe_allow_html=True)

