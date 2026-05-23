import sys
import os
import threading
import time
import uvicorn
import streamlit as st
import requests

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

def run_api():
    try:
        from app.api.main import app as fastapi_app
        uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)
    except Exception as e:
        print(f"FastAPI startup error: {e}")

if "api_started" not in st.session_state:
    thread = threading.Thread(target=run_api, daemon=True)
    thread.start()
    st.session_state.api_started = True
    time.sleep(3)

st.title("Agentic AI Research Assistant")

query = st.text_area("Enter Research Query")

if st.button("Generate"):
    if not query or not query.strip():
        st.warning("Please enter a research query before generating.")
    else:
        with st.spinner("Generating response..."):
            try:
                response = requests.post(
                    "http://localhost:8000/research",
                    json={"query": query},
                    timeout=120
                )
                response.raise_for_status()

                data = response.json()
                answer = data.get("answer", "")

                if answer:
                    st.write(answer)
                else:
                    st.warning("Backend returned no answer. Please try again or check the backend service.")

            except requests.exceptions.ConnectionError:
                st.error("Backend is still starting up. Please wait a few seconds and try again.")
            except requests.exceptions.Timeout:
                st.error("Request timed out. The research query may be too complex.")
            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {e}")
            except ValueError:
                st.error("Received an invalid response from the backend.")
# import streamlit as st
# import requests

# st.title("Agentic AI Research Assistant")

# query = st.text_area("Enter Research Query")

# if st.button("Generate"):
#     if not query or not query.strip():
#         st.warning("Please enter a research query before generating.")
#     else:
#         with st.spinner("Generating response..."):
#             try:
#                 response = requests.post(
#                     "http://localhost:8000/research",
#                     json={"query": query},
#                     timeout=60
#                 )
#                 response.raise_for_status()

#                 data = response.json()
#                 answer = data.get("answer", "")

#                 if answer:
#                     st.write(answer)
#                 else:
#                     st.warning("Backend returned no answer. Please try again or check the backend service.")

#             except requests.exceptions.RequestException as e:
#                 st.error(f"Request failed: {e}")
#             except ValueError:
#                 st.error("Received an invalid response from the backend.")