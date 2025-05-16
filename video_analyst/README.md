# 🎥 AI Video Chat Summarizer App

An AI-powered web application that lets you **chat with your videos**! Upload any video file and interact with it using natural language. Powered by **Google Gemini 2.0 Flash**, **Phi Agent**, and **Streamlit**.

---

## 🧠 Features

- 🎬 Upload and preview `.mp4`, `.mov`, or `.avi` videos
- 💬 Ask natural language questions about the video content
- ⚡ Gemini 2.0 Flash for fast, multimodal video understanding
- 🌐 DuckDuckGo tool for live web context (via Phi Agent)
- 💡 Clear chat history and reset session easily
- 🧱 Clean modular codebase (easy to extend)

---

## 🚀 Demo

![demo](https://your-demo-link-or-screenshot.png)

---

## 📁 Project Structure

.
├── app.py # Main Streamlit app
├── agents/
│ └── video_agent.py # AI Agent logic using Gemini + Phi
├── utils/
│ └── file_utils.py # File saving utility
├── config/
│ └── settings.py # API key & env configuration
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the repository

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-video-chat-app.git
cd ai-video-chat-app
```

### 2. Create .env file

Add your Google Generative AI API Key:

```bash
GOOGLE_API_KEY=your-api-key-here
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

## ✨ Example Prompts

1. "What is this video about?"

2. "Summarize the key points."

3. "List any people mentioned in the video."

4. "Does this video mention recent events?"

## 🔐 Environment Variables

    Variable	  |      Description

GOOGLE_API_KEY Your Google Gemini API key

## 🛠️ Technologies Used

- Streamlit
- Google Gemini 2.0 Flash
- Phi Agent Framework
- DuckDuckGo Tool
- Python 3.9+

## 📌 Future Improvements

- Support for PDFs, DOCX, and Excel
- Multilingual query support
- Summarization timeline or highlights
- Streamlit Cloud or Docker deployment

## 🙌 Acknowledgements

- Google Generative AI
- Phi Agent Framework
- Streamlit Team

🔗 Connect
📧 Email: snsupratim@gmail.com

---
