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
PAGE_ICON = ':laptop:'
NAME = 'Kunal Kumar Sahoo'
DESCRIPTION = '''
Computer Science undergraduate, exploring the domains of **Artificial Intelligence** and **Robotics**
'''
EMAIL = 'kunal.sahoo2003@gmail.com'
SOCIAL_MEDIA = {
    'https://www.svgrepo.com/show/110195/linkedin.svg': 'https://linkedin.com/in/kunal-kumar-sahoo/',
    'https://www.svgrepo.com/show/303115/twitter-3-logo.svg': 'https://twitter.com/KunalKSahoo/',
    'https://www.svgrepo.com/show/503359/github.svg': 'https://github.com/Kunal-Kumar-Sahoo/',
    'https://www.svgrepo.com/show/489456/email.svg': 'mailto:kunal.sahoo2003@gmail.com'
}
PROJECTS = {
    'Stream Segment': {'url': 'https://github.com/Kunal-Kumar-Sahoo/inpaint-sd-sam', 'description': 'A web-app to perform semantic segmentation on images using pre-trained DeepLabV3-ResNet101 Hybrid model'},
    'GenMuzic': {'url': 'https://github.com/Kunal-Kumar-Sahoo/genmuzic', 'description': 'A streamlit-based web-application that generates music from text prompt using Meta\'s Audiocraft'},
    'In-Painting App': {'url': 'https://github.com/Kunal-Kumar-Sahoo/inpaint-sd-sam', 'description': 'A simple web application that performs prompt-based Stable Diffusion in selected segments of an image that is segmented using Meta\'s Segment Anything Model'},
    'Q-Lunar Lander': {'url': 'https://github.com/Kunal-Kumar-Sahoo/deep-Q-lunar-lander', 'description': 'Simulated Lunar Landing through attitude control using Deep Q-learning'},
    'PyCoWINAPI': {'url': 'https://github.com/Kunal-Kumar-Sahoo/PyCowinAPI', 'description': 'A simple Python wrapper around CoWIN-platform API to automate COVID-19 Vaccine Slot Booking. (3.5K+ downloads)'},
    'Mask Police': {'url': 'https://github.com/Kunal-Kumar-Sahoo/Face-Mask-Detection-Python', 'description': 'Python application to detect whether a person is wearing face mask or not (in realtime) using MobileNetV2 architecture and standard Kaggle Dataset'},
    'NLP 101': {'url': 'https://github.com/Kunal-Kumar-Sahoo/NLP-App-101', 'description': 'Simple web application to demonstrate various applications of Natural Language Processing to beginners'},
    'Snap Filters': {'url': 'https://github.com/Kunal-Kumar-Sahoo/snap-filters', 'description': 'Python application to overlay SnapChat like filters on faces in real-time through Face Detection and HoG-Feature Extraction technique'},
    'StockPY': {'url': 'https://github.com/Kunal-Kumar-Sahoo/StockPY', 'description': 'A simple streamlit dashboard to visualize closing S&P500 stock prices'}
}
CERTIFICATES = {
    'Level 3 GenAI: Prompt Engineering': 'https://www.cloudskillsboost.google/public_profiles/f63cc28c-fa62-4ec4-9f6e-1c4a53bab56c/badges/5635041?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share',
    'Google Cloud Computing Foundations: Data, ML, and AI in Google Cloud': 'https://www.cloudskillsboost.google/public_profiles/f63cc28c-fa62-4ec4-9f6e-1c4a53bab56c/badges/5534797?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share',
    'Perform Foundational Data, ML, and AI Tasks in Google Cloud': 'https://www.cloudskillsboost.google/public_profiles/f63cc28c-fa62-4ec4-9f6e-1c4a53bab56c/badges/5611064?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share',
    'Perform Foundational Infrastructure Tasks in Google Cloud': 'https://www.cloudskillsboost.google/public_profiles/f63cc28c-fa62-4ec4-9f6e-1c4a53bab56c/badges/5605855?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share',
    'Fundamentals of Deep Learning': 'https://courses.nvidia.com/certificates/d6b2c9046845476ba62392e0ac418f3b/',
    'Industry Approach to IoT with Deep Learning': 'https://certopus.com/c/97f183c11035402199565a5049247bc5',
    'Webinar on Recent Advancements in Computer Vision': 'https://pdpuacin-my.sharepoint.com/personal/kunal_sce21_pdpu_ac_in/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fkunal%5Fsce21%5Fpdpu%5Fac%5Fin%2FDocuments%2FE%2Dcertificate%20for%20Kunal%20Kumar%20Sahoo%2DCV%2Dworkshop%2Epdf&parent=%2Fpersonal%2Fkunal%5Fsce21%5Fpdpu%5Fac%5Fin%2FDocuments&ga=1',
    'Applications of Statistics in Data Analytics': 'https://drive.google.com/file/d/1SCvHtapfScbM7esz0yNkhu41yuMf9skF/view',
    'Apprenticeship, The Machine Learning & Deep Learning Show': 'https://verification.givemycertificate.com/v/54ac7ab1-d242-4235-9c0c-c95f86e1af6b'
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

st.write('#')
st.subheader('Skills')

cols = st.columns(2, gap='small')
cols[0].markdown('<p style="margin-bottom: -10px;"><strong>Programming Languages</strong></p>', unsafe_allow_html=True)
cols[1].markdown('<p style="margin-bottom: -10px;">Python, Julia, R, Java, C/C++, Bash, MATLAB (Basic)</p>', unsafe_allow_html=True)

cols = st.columns(2, gap='small')
cols[0].markdown('<p style="margin-bottom: -10px;"><strong>Databases</strong></p>', unsafe_allow_html=True)
cols[1].markdown('<p style="margin-bottom: -10px;">MySQL, MongoDB, SQLite, Postgres</p>', unsafe_allow_html=True)

cols = st.columns(2, gap='small')
cols[0].markdown('<p style="margin-bottom: -10px;"><strong>Libraries/Frameworks</strong></p>', unsafe_allow_html=True)
cols[1].markdown('<p style="margin-bottom: -10px;">PyBullet, NumPy, Pandas, Matplotlib, OpenCV, PIL, Tensorflow, Keras, PyTorch, NLTK, Transformers, Streamlit, Flask, Librosa, ROS</p>', unsafe_allow_html=True)

cols = st.columns(2, gap='small')
cols[0].markdown('<p style="margin-bottom: -10px;"><strong>Developer Tools</strong></p>', unsafe_allow_html=True)
cols[1].markdown('<p style="margin-bottom: -10px;">GNU/Linux, Docker, Git, Google Cloud Platforms, Anaconda</p>', unsafe_allow_html=True)

cols = st.columns(2, gap='small')
cols[0].markdown('<p style="margin-bottom: -10px;"><strong>Microcontrollers/Microprocessors</strong></p>', unsafe_allow_html=True)
cols[1].markdown('<p style="margin-bottom: -10px;">Arduino, Raspberry Pi, ESP32, STM32, Jetson NANO</p>', unsafe_allow_html=True)


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
- ✅ Junior Research Fellow @ *School of Petroleum Technology, PDEU* (July 2023 -- Present)
    - Working on applying transfer learning to identify sucker rod pump anomaly from dynacards
    - Project sponsored by **Shell**
- ✅ R&D Intern @ *Jio, RIL* (June 2023 -- August 2023)
    - Developed library to fit skeletons in 3D meshes
    - Developed library to animate 3D objects using Linear Skinning
- ✅ Summer Research Intern @ *ATDC, IIT Kharagpur* (May 2023 -- June 2023)
    - Worked on the problem statement *Native Language Identification from Non-Native speech*
    - Incorportated **XAI methods** to develop interpretable models
- ✅ Student Researcher @ Student Research Program, PDEU (October 2022 -- Present)
    - Developing a real-time posture monitoring system using computer vision
    - Building a modular device that can be connected to laptop/desktop
'''
)

# --- PROJECTS ---
st.write('#')
st.subheader('Projects')
for project, content in PROJECTS.items():
    st.write(f'* **[{project}]({content["url"]})**: {content["description"]}')

# ---ACHIEVEMENTS---
st.write('#')
st.subheader('Achievements')
st.write(
'''
- Filed 1 *Provisional Design Patent* and 1 *Provisional Product Patent* under Indian Patent Office
- Amongst [top 4%](https://quine.sh/user/Kunal-Kumar-Sahoo) developers wordwide (Python, rank 115) on *Quine.sh*
- Within top 10 best projects in University-level Smart India Hackathon, 2023
- Received funding of **225K INR** for project idea under SSIP Policy
- Won **150K INR** as prize money in *Robofest 3.0*
- Second runner-up at *EnCode hackathon* at IIT Guwahati (sponsor: **Bosch**)
- Grand finalist of *Azadi ka Amrit Mahotsav Hackathon 2022*, organized by Govt. of Gujarat
'''
)

# --- CERTIFICATIONS -----
st.write('#')
st.subheader('Certifications')
for certificate, link in CERTIFICATES.items():
    st.write(f'[{certificate}]({link})')

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