import streamlit as st
from agents.video_agent import initialize_agent, analyze_video_with_agent
from utils.file_utils import save_temp_file
from config.config import configure_environment

from pathlib import Path
import os

# Configure environment
configure_environment()

# Page setup
st.set_page_config(page_title="Video Chat AI", page_icon="🎥", layout="wide")
st.title("🎥 AI Chat with Your Video")
st.caption("Powered by Gemini 2.0 Flash + Phi Agent")

# Sidebar: File upload
st.sidebar.header("📁 Upload Video")
video_file = st.sidebar.file_uploader("Upload a video", type=["mp4", "mov", "avi"])

video_path = None
if video_file:
    video_path = save_temp_file(video_file)
    st.sidebar.video(video_path)
    st.sidebar.success("Video uploaded successfully!")

# Session state for chat history and file path
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "agent" not in st.session_state:
    st.session_state.agent = initialize_agent()

# Main area logic
if video_file and video_path:
    st.subheader("💬 Chat About the Video")

    # Chat input
    user_input = st.chat_input("Ask something about the video...")

    if user_input:
        # Add user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Process with AI agent
        with st.spinner("Analyzing video..."):
            try:
                response = analyze_video_with_agent(st.session_state.agent, video_path, user_input)
                st.session_state.chat_history.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"Error: {e}"
                st.session_state.chat_history.append({"role": "assistant", "content": error_msg})

    # Render full conversation
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Reset button
    if st.sidebar.button("🔁 Clear Chat"):
        st.session_state.chat_history = []
        if video_path:
            Path(video_path).unlink(missing_ok=True)
        st.rerun()
else:
    st.info("👈 Upload a video from the sidebar to begin chatting.")
