import tempfile

def save_temp_file(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp:
        tmp.write(uploaded_file.read())
        return tmp.name
