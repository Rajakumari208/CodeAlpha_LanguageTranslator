import streamlit as st
from deep_translator import GoogleTranslator
import pyperclip

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI Language Translation Tool")
st.write("Translate text instantly between multiple languages.")

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

text = st.text_area("✍ Enter Text")

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox("Source Language", languages.keys())

with col2:
    target = st.selectbox("Target Language", languages.keys())

if st.button("🔄 Translate"):

    if text.strip() == "":
        st.warning("Please enter text")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.success("✅ Translation Completed")

            st.text_area(
                "Translated Text",
                translated,
                height=150
            )

            if st.button("📋 Copy Translation"):
                pyperclip.copy(translated)
                st.success("Copied to clipboard!")

        except Exception as e:
            st.error(f"Error: {e}")