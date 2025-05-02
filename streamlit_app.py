import os
import streamlit.web.cli as stcli
from streamlit.web.server import Server

# Create a WSGI-compatible Streamlit server
server = Server(stcli._main, base_url_path="", port=int(os.getenv("PORT", 8501)))

if __name__ == "__main__":
    import sys
    sys.argv = ["streamlit", "run", "App.py", "--server.port", os.getenv("PORT", "8501")]
    stcli.main()