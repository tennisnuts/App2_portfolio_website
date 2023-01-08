import streamlit as st

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