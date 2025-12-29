import langchain_helper as lch
import streamlit as st
import textwrap

st.title('YOUTUBE ASSISTANT')

with st.sidebar:
    with st.form(key="my_form"):
        youtube_url= st.sidebar.text_area(
            label="Enter the youtube video url that you need assitance with:",
            max_chars=50
        )
        query= st.sidebar.text_area(
            label="What's your querry?",
            max_chars=100,
            key="query"
        )
        submit_btn= st.form_submit_button(label="Submit")

if youtube_url and query:
    db= lch.create_vector_db_from_youtube_url(youtube_url)
    response, data= lch.get_respponse_from_querry(db, query)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width=85))


