import urllib
import streamlit as st
from groq import Groq
import time
import requests

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="NEXUS AI 10.0 (Free Version)",
    page_icon="🆓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. Custom CSS ---
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; font-weight: 800; color: #f55036; margin-bottom: 1rem; }
    .stButton>button { color: white; background-color: #f55036; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

# --- 3. API Key Management (Groq) ---
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Groq API Key (Free from console.groq.com)
    api_key = st.text_input("Enter Groq API Key (Free)", type="password", help="Get one for free at console.groq.com")
    
    if api_key:
        try:
            client = Groq(api_key=api_key)
            st.success("🟢 Connected to Groq (Llama 3)")
        except Exception as e:
            st.error(f"Connection Error: {e}")
    else:
        st.warning("🟡 Please enter Groq API Key to Chat.")
        st.info("Images do not require a key.")
    
    st.markdown("---")
    st.markdown("### How to use")
    st.write("1. Get a free Groq key.")
    st.write("2. Chat with Llama 3.")
    st.write("3. Generate Art for Free.")

# --- 4. Initialize Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 5. Main Application Layout ---
st.markdown('<div class="main-header">NEXUS AI (Free Tier)</div>', unsafe_allow_html=True)
tab1, tab2 = st.tabs(["💬 Smart Chat", "🎨 Free Image Gen"])

# ==========================================
# TAB 1: CHAT INTERFACE (Using Groq/Llama 3)
# ==========================================
with tab1:
    st.subheader("Chat with Llama 3 (via Groq)")
    
    # Display History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input
    if prompt := st.chat_input("Ask me anything..."):
        if not api_key:
            st.error("Please enter your Groq API Key in the sidebar first!")
        else:
            # Add User Message
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate Response
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""

                try:
                    # Call Groq API (Llama 3 70B model - very smart)
                    stream = client.chat.completions.create(
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ],
                        model="llama-3.3-70b-versatile", # This is the free high-end model
                        stream=True,
                    )

                    # Stream text
                    for chunk in stream:
                        if chunk.choices[0].delta.content:
                            full_response += chunk.choices[0].delta.content
                            message_placeholder.markdown(full_response + "▌")
                    
                    message_placeholder.markdown(full_response)

                except Exception as e:
                    full_response = f"Error: {str(e)}"
                    message_placeholder.markdown(full_response)

            st.session_state.messages.append({"role": "assistant", "content": full_response})
# ==========================================
# TAB 2: IMAGE GENERATOR (Force Fetch Fix)
# ==========================================
with tab2:
    st.subheader("Free Image Generator (No Key Required)")
    st.caption("Powered by Pollinations.ai - Completely Free")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        img_prompt = st.text_input("Describe the image:", placeholder="A cyberpunk cat, neon lights, highly detailed...")
    with col2:
        generate_btn = st.button("🎨 Generate", use_container_width=True)

    if generate_btn and img_prompt:
        with st.spinner("Generating artwork..."):
            # 1. Encode the prompt
            safe_prompt = urllib.parse.quote(img_prompt)
            seed = int(time.time())
            
            # 2. Construct the URL
            image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?width=1024&height=1024&seed={seed}"
            
            # 3. Force the computer to download the image data
            try:
                response = requests.get(image_url)
                
                # Check if we successfully got the image
                if response.status_code == 200:
                    st.success("Image generated for free!")
                    # We display the raw image data (bytes) instead of the URL
                    st.image(response.content, caption=f"Generated: {img_prompt}", use_container_width=True)
                    st.markdown(f"[🔗 Open Image in New Tab]({image_url})")
                else:
                    st.error(f"Failed to download image. Status code: {response.status_code}")
                    st.markdown(f"Try manually: {image_url}")

            except Exception as e:
                st.error(f"An error occurred: {e}")