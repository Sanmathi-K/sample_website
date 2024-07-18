import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/images.png")
img_lottie_animation = Image.open("images/Python-Virtualenv.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Sanmathi :wave:")
    st.title("ABOUT VIRTUAL ENVIRONMENT")
    st.write(
        "A basic information about python virtual environment"
    )
    st.write("[Learn More >]()")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what are python virtual environments")
        st.write("##")
        st.write(
            """
            Python virtual environments allow developers to control software dependencies in Python code. 
            They’re useful ways of ensuring that the correct package/library versions are consistently used 
            every time the software runs. Virtual environments also help ensure that the results from running 
            code are reproducible.


            """
        )
        st.write("[Learn more >](https://www.dataquest.io/blog/a-complete-guide-to-python-virtual-environments/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Python virtual Environment")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("when to use virtual environments")
        st.write(
            """
            Working within a Python virtual environment is generally a good idea when developing 
            Python code because they provide ways to control the behavior of a software program. 
            If code is written to generate a specific output given a known input, the same output 
            should be reliably generated for that input whether the code is run on my computer, 
            a remote machine, or someone else’s laptop. Developing software without a virtual 
            environment defined increases the risk of the code failing or producing undesired results.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Benifits of virtual environments")
        st.write(
            """
            Virtual environments have many benefits including easier dependency management 
            and reduced risk of package conflicts and errors caused by software deprecation. 
            Software dependency management is the process of bookkeeping software versions needed 
            for a piece of software to run. Package conflicts arise when two or more software packages are incompatible, causing a piece of software to fail to run. Software deprecation occurs when a part or all of a software program or library changes or is removed.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/IAvAlS0CuxI)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()