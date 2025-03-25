#code for sidebar and login
import streamlit as st
def login_page():
    st.title("🔐 Login to Care Companion")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "1234":  # Dummy login check
            st.session_state["logged_in"] = True
            st.success("✅ Login successful! Redirecting...")
            st.experimental_rerun()  # Refresh the page
        else:
            st.error("❌ Invalid credentials. Try again!")
if _name_ == "_main_":
    login_page()
    
import streamlit as st
from login import login_page  # Import the login function from login.py

# 🚀 Set page configuration
st.set_page_config(page_title="Care Companion", page_icon="💙", layout="wide")

# 🔐 Check if user is logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    login_page()  
    st.stop()  

# 🎨 Sidebar Navigation
st.sidebar.title("🔹 Care Companion")
page = st.sidebar.radio("Select a Feature", ["Home 🏠", "Unstructured to Structured 🔄", "Keyword Extraction 🔍", "Text Summarization 📜"])

# 🏠 Home Page
if page == "Home 🏠":
    st.title("🏥 Welcome to Care Companion!")
    st.subheader("Your AI-powered assistant for medical text processing. 🚀")
    st.write("Empowering healthcare with AI-driven solutions for better insights and analysis.")

    st.markdown("### 🔥 Why Care Companion?")
    st.write("""
    ✅ Extract *meaningful information* from raw text  
    ✅ Find *important keywords* in large medical documents  
    ✅ Summarize *long reports* into easy-to-read summaries  
    """)
    
    st.info("💡 Knowledge Box: AI is transforming healthcare, reducing paperwork, and enhancing diagnostics!")
    st.image("https://source.unsplash.com/800x400/?medical,AI", caption="AI in Healthcare", use_column_width=True)

# 📌 Feature 1: Unstructured Data to Structured Data
elif page == "Unstructured to Structured 🔄":
    st.title("📝 Convert Unstructured Data to Structured Data 📊")
    st.write("Transform complex medical notes into structured information for better analysis. ✨")

    user_input = st.text_area("📝 Enter unstructured text here:", height=150)
    
    if st.button("Convert to Structured Data"):
        # 🔹 Replace this with your actual processing function
        structured_output = f"🔹 Processed Structured Data for: {user_input[:50]}..." if user_input else "No input provided."
        st.success(structured_output)
    st.markdown("### 🌟 Benefits:")
    st.write("""
    🔹 Organized and structured data  
    🔹 Faster access to patient insights  
    🔹 Easier data processing and analysis  
    """)
    st.success("💡 Did you know? Data structuring can improve healthcare decisions and speed up research!")
# 🔍 Feature 2: Keyword Extraction
elif page == "Keyword Extraction 🔍":
    st.title("🔍 Find Important Keywords in Medical Text 🏥")
    st.write("Extract key medical terms and critical insights from large documents efficiently.")
    user_input = st.text_area("📄 Enter medical text:", height=150)
    if st.button("Extract Keywords"):
        # 🔹 Replace this with your actual keyword extraction logic
        keywords = f"🔹 Extracted Keywords: ['health', 'diagnosis', 'treatment']" if user_input else "No input provided."
        st.success(keywords)

    st.markdown("### 🏆 How it Helps:")
    st.write("""
    ✅ Saves time in analyzing reports  
    ✅ Identifies key symptoms and conditions  
    ✅ Helps doctors focus on important data  
    """)

    st.warning("💡 Fact: NLP-based keyword extraction helps detect diseases faster!")

def summarizer(text, max_length=150, min_length=30, do_sample=False):
    return [{"summary_text": "This is a sample summary for demonstration purposes."}]

# Text Summarization Feature
if page == "Text Summarization 📜":
    st.title("📜 Summarize Long Medical Reports with AI 🚀")
    user_input = st.text_area("📜 Paste the medical report here:", height=200)

    if st.button("Summarize Text"):
        if user_input:
            summary = summarizer(user_input, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
            st.success(f"🔹 Summary: {summary}")

            # Display translation options
            st.markdown("### 🌐 Translate Summary")
            language_choice = st.radio("Choose a language for translation:", ["Gujarati", "Marathi", "Hindi"])

            if st.button("Translate Summary"):
                if language_choice == "Gujarati":
                    translation = translator_gu(summary)[0]['translation_text']
                elif language_choice == "Marathi":
                    translation = translator_mr(summary)[0]['translation_text']
                else:
                    translation = translator_hi(summary)[0]['translation_text']
                st.success(f"🔹 Translated Summary: {translation}")
        else:
            st.warning("Please enter text to summarize.")
    st.markdown("### 🔹 Why Summarization?")
    st.write("""
    🏥 Saves doctors' time  
    📄 Makes reports easier to understand  
    🔬 Highlights critical information  
    """)

    st.info("💡 AI Trivia: Medical report summarization can reduce reading time by 60%!")
# 🎨 Footer
st.sidebar.markdown("---")
st.sidebar.write("💙 *Care Companion - AI for Healthcare!* 🚀")
