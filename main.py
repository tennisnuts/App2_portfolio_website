import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Oliver Nunn')
    content = '''
    Hello my name is Oliver Nunn and i am a ClimateTech engineer from the University of Oxford.
    '''
    st.info(content)


content2 = '''
Below you can find some of the apps i have built in Python. Please feel free to contact me :)
'''
st.text(content2)

col3, emptycol, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv('data.csv', sep=';')

with col3:
    for index, rows in df[:10].iterrows():
        st.header(rows['title'])
        st.write(rows['description'])
        st.image('images/' + rows['image'])
        st.write(f"[Source Code]({rows['url']})")

with col4:
    for index, rows in df[10:].iterrows():
        st.header(rows['title'])
        st.write(rows['description'])
        st.image('images/' + rows['image'])
        st.write(f"[Source Code]({rows['url']})")

