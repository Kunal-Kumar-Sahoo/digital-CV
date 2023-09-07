from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_directory = Path(__file__).parent if '__file__' in locals() else Path.cwd()
# css_file = current_directory / 'styles' / 'main.css'
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
    'https://www.svgrepo.com/show/110195/linkedin.svg': 'https://linkedin.com/in/kunal-kumar-sahoo/',
    'https://www.svgrepo.com/show/303115/twitter-3-logo.svg': 'https://twitter.com/KunalKSahoo/',
    'https://www.svgrepo.com/show/503359/github.svg': 'https://github.com/Kunal-Kumar-Sahoo/',
    'https://www.svgrepo.com/show/489456/email.svg': 'mailto:kunal.sahoo2003@gmail.com'
}
PROJECTS = {
    'PyCoWINAPI: Python wrapper around CoWIN API for finding vaccination slots': 'https://github.com/Kunal-Kumar-Sahoo/PyCowinAPI',
    'Mask Police: Detects in real-time if a person is wearking mask or not': 'https://github.com/Kunal-Kumar-Sahoo/Face-Mask-Detection-Python',
    'NLP 101: Basic applications of NLP visualized on a website': 'https://github.com/Kunal-Kumar-Sahoo/NLP-App-101',
    'SolarPY: Physics engine for solar system simulation': 'https://github.com/Kunal-Kumar-Sahoo/Solar-System-Simulator',
    'StockPY: Dashboard to retrieve S&P500 and its corresponding closing price': 'https://github.com/Kunal-Kumar-Sahoo/StockPY'
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD PDF & PROFILE PIC ---
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


# --- SOCIAL LINKS ---
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f'<a href="{link}"><img src="{platform}" alt="HTML tutorial" style="width:42px;height:42px;"></a>', unsafe_allow_html=True)


# --- EXPERIENCE & QUALIFICATIONS ----
st.write('#')
st.subheader('Education')

cols = st.columns(4)
cols[0].write('🎓 **B.Tech in Computer Engineering**')
cols[1].write('*Pandit Deendayal Energy University*')
cols[2].write('2021--Present')
cols[3].write('CGPA: 9.89/10')

cols = st.columns(4)
cols[0].write('🎓 **Class XII (CBSE)**')
cols[1].write('*Kendriya Vidyalaya No. 1, Gandhinagar*')
cols[2].write('2021')
cols[3].write('Percentage: 94.8%')

cols = st.columns(4)
cols[0].write('🎓 **Class X (CBSE)**')
cols[1].write('*Kendriya Vidyalaya No. 1, Gandhinagar*')
cols[2].write('2019')
cols[3].write('Percentage: 94.4%')

st.write('#')
st.subheader('Experience')
st.write(
    '''
- ✅ Junior Research Fellow @ School of Petroleum Technology, PDEU (July 2023 -- Present)
    - Working on applying transfer learning to identify sucker rod pump anomaly from dynacards
    - Project sponsored by *Shell*
- ✅ R&D Intern @ Jio, RIL (June 2023 -- August 2023)
    - Developed library to fit skeletons in 3D meshes
    - Developed library to animate 3D objects using Linear Skinning
- ✅ Summer Research Intern @ Advanced Technology Development Centre, IIT Kharagpur (May 2023 -- June 2023)
    - Worked on the problem statement *Native Language Identification from Non-Native speech*
    - Incorportated *XAI methods* to develop interpretable models
- ✅ Student Researcher @ Student Research Program, PDEU (October 2022 -- Present)
    - Developing a real-time posture monitoring system using computer vision
    - Building a modular device that can be connected to laptop/desktop
'''
)


# --- SKILLS ---
st.write('#')
st.subheader('Skills')
st.write(
    '''
- **Programming Languages:** Python, Julia, R, Java, C, MATLAB
- **Databases:** MySQL, MariaDB, SQLite, MongoDB
- **Libraries/Frameworks:** NumPy, Pandas, Matplotlib, OpenCV, PIL, Tensorflow, Keras, PyTorch, NLTK, Transformers, Streamlit, Flask, Librosa, PyBullet, ROS, Arduino
- **Developer Tools:** GNU/Linux, Git, Docker
- **Other**: LaTeX, Bash
'''
)

# --- PROJECTS ---
st.write('#')
st.subheader('Projects')
for project, link in PROJECTS.items():
    st.write(f'[{project}]({link})')


# ---CO-CURRICULARS---
st.write('#')
st.subheader('Co-Curricular Activities')
st.write(
    '''
- **President** @ *Cretus: The Robotics & Automation Club of PDEU*
- **Lead** @ *Google Developers Students' Club, PDEU*
- **Vice-Chairperson** @ *Association of Computing Machinery, PDEU*
- **AI/ML Head** @ *Encode: The Computer Science Club of PDEU*
'''
)