import streamlit as st
import pandas as pd
import duckdb

# title
st.write("""
# SQL SRS
Spaced Repetition System SQL practice
""")

with st.sidebar:
    option = st.selectbox(
        "What would you like to review",
        ("Joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme.."
    )

    st.write('You selected:', option)

data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    sql_query = st.text_area(label="Entrez votre input")
    result = duckdb.query(sql_query).df()

    st.dataframe(result)

with tab2:
    st.write("foufou")

with tab3:
    st.write("rourou")
