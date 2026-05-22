import streamlit as st
from deep_translator import GoogleTranslator
import pyperclip
from gtts import gTTS
import tempfile
from streamlit_mic_recorder import mic_recorder

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

# ---------------- DARK MODE CSS ---------------- #

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}

h1, h2, h3, p {
    color: white;
}

textarea {
    background-color: #1E1E1E !important;
    color: white !important;
    border-radius: 10px !important;
}

.stButton>button {
    background-color: #00ADB5;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    border: none;
}

.stSelectbox div {
    background-color: #1E1E1E;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.title("🌍 AI Language Translation Tool")
st.write("Translate text with AI, Voice Input & Speech Output")

# ---------------- LANGUAGES ---------------- #

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

# ---------------- SESSION STATE ---------------- #

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

# ---------------- TEXT INPUT ---------------- #

text = st.text_area("✍ Enter Text", height=150)

# ---------------- VOICE INPUT ---------------- #

st.subheader("🎤 Voice Input")

audio = mic_recorder(
    start_prompt="Start Recording",
    stop_prompt="Stop Recording",
    key='recorder'
)

if audio:
    st.success("✅ Voice recorded successfully!")

# ---------------- LANGUAGE SELECTION ---------------- #

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox("Source Language", list(languages.keys()))

with col2:
    target = st.selectbox("Target Language", list(languages.keys()))

# ---------------- TRANSLATION ---------------- #

if st.button("🔄 Translate"):

    if text.strip() == "":
        st.warning("⚠ Please enter text")

    else:
        try:

            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.session_state.translated_text = translated

            st.success("✅ Translation Completed")

        except Exception as e:
            st.error(f"❌ Error: {e}")

# ---------------- OUTPUT ---------------- #

if st.session_state.translated_text:

    st.text_area(
        "🌐 Translated Text",
        st.session_state.translated_text,
        height=150
    )

    # ---------------- COPY BUTTON ---------------- #

    if st.button("📋 Copy Translation"):
        pyperclip.copy(st.session_state.translated_text)
        st.success("Copied Successfully!")

    # ---------------- TEXT TO SPEECH ---------------- #

    tts = gTTS(
        text=st.session_state.translated_text,
        lang=languages[target]
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        temp_filename = fp.name
        tts.save(temp_filename)

    st.audio(temp_filename)

# ---------------- FOOTER ---------------- #

st.markdown("---")
st.markdown(
    "<center>Developed by Rajakumari M 🚀</center>",
    unsafe_allow_html=True
)