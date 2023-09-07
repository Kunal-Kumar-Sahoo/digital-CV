from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_directory = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_directory / 'styles' / 'main.css'
resume_file = current_directory / 'assets' / 'Kunal Resume.pdf'
profile_pic = current_directory / 'assets' / 'profile.jpeg'

# --- GENERAL SETTINGS ---
PAGE_TITLE = 'Digital CV | Kunal Kumar Sahoo'
PAGE_ICON = ':wave:'
NAME = 'Kunal Kumar Sahoo'
DESCRIPTION = '''
Computer Science undergraduate, exploring the domains of Artificial Intelligence and Robotics
'''
EMAIL = 'kunal.sahoo2003@gmail.com'
SOCIAL_MEDIA = {
    'LinkedIn': 'https://linkedin.com/in/kunal-kumar-sahoo/',
    'Twitter': 'https://twitter.com/KunalKSahoo/',
    'GitHub': 'https://github.com/Kunal-Kumar-Sahoo/'
}
PROJECTS = {
    'PyCoWINAPI: Python wrapper around CoWIN API for finding vaccination slots': 'https://github.com/Kunal-Kumar-Sahoo/PyCowinAPI',
    'Mask Police: Detects in real-time if a person is wearking mask or not': 'https://github.com/Kunal-Kumar-Sahoo/Face-Mask-Detection-Python',
    'NLP 101: Basic applications of NLP visualized on a website': 'https://github.com/Kunal-Kumar-Sahoo/NLP-App-101',
    'SolarPY: Physics engine for solar system simulation': 'https://github.com/Kunal-Kumar-Sahoo/Solar-System-Simulator',
    'StockPY: Dashboard to retrieve S&P500 and its corresponding closing price': 'https://github.com/Kunal-Kumar-Sahoo/StockPY'
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file, 'r') as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap='small')

with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label='📄 Download Resume',
        data=PDFbyte,
        file_name=resume_file.name,
        mime='application/octet-stream',
    )
    st.write(':email:', EMAIL)