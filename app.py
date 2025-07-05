import streamlit as st
import time

# Page setup
st.set_page_config(page_title="A Tiny Journey 🌸", page_icon="💌", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .main {
            background-color: F5F5DC;
            padding: 2em;
            border-radius: 1em;
        }
        .title {
            font-size: 40px;
            color: 2F4F4F;
            text-align: center;
            margin-bottom: 10px;
        }
        .text {
            font-size: 18px;
            color: 87CEFA;
            text-align: center;
            margin: 20px 0;
        }
        .button {
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>A Tiny Journey of Forgiveness </div>", unsafe_allow_html=True)

# Step 1: Introduction
with st.container():
    st.markdown("<div class='text'>Once upon a sleepy morning... someone (me ) hit snooze one too many times.</div>", unsafe_allow_html=True)
    st.markdown("<div class='text'>Sayang was very angry, So i made you this little journey. ❤️ </div>", unsafe_allow_html=True)
    if st.button("Vanakam pls press enter"):
        st.session_state.step = 1

# Step 2: Little Confession
if st.session_state.get("step") == 1:
    time.sleep(0.5)
    st.markdown("<div class='text'>I messed up. I woke up tooooooooooooooooo late </div>", unsafe_allow_html=True)
    time.sleep(0.5)
    st.markdown("<div class='text'>But when I woke up, the first thing I thought was...</div>", unsafe_allow_html=True)
    if st.button("Enna??? "):
        st.session_state.step = 2

# Step 3: The Thought
if st.session_state.get("step") == 2:
    st.markdown("<div class='text'>“Oh no... I let my favorite human down.” </div>", unsafe_allow_html=True)
    time.sleep(1)
    st.markdown("<div class='text'> Im waking up tooooooo late and its making her miss me so much?(FUCK LONG DISTANCE!!!!)</div>", unsafe_allow_html=True)
    if st.button("Keep going if u shrimp me "):
        st.session_state.step = 3

# Step 4: Soft Game (just a cute question)
if st.session_state.get("step") == 3:
    st.markdown("<div class='text'>Pop quiz: What do I owe you?</div>", unsafe_allow_html=True)
    answer = st.radio("Choose wisely...", ["Kisses", "Huggies", "kunafah", "Vodka", "dubai choco", "Lando Norris (I may be jealous but its okay)", "All of the above "])
    if st.button("Submit my answer"):
        st.session_state.step = 4

# Step 5: Final message
if st.session_state.get("step") == 4:
    st.balloons()
    st.markdown("<div class='text'> It’s all of the above!!!! </div>", unsafe_allow_html=True)
    st.markdown("<div class='text'>Nandriii for waiting for my dumbass to wake up everyday hehehe i shrimp youuuuuuuu✨</div>", unsafe_allow_html=True)
    st.markdown("<div class='text'>When u come back on the 8th i will drown with nini kisses❤️❤️❤️❤️❤️❤️❤️❤️</div>", unsafe_allow_html=True)