import threading
import time
import uvicorn
import streamlit as st
import requests

def run_api():
    uvicorn.run("app.api.main:app", host="0.0.0.0", port=8000)

if "api_started" not in st.session_state:
    thread = threading.Thread(target=run_api, daemon=True)
    thread.start()
    st.session_state.api_started = True
    time.sleep(2)  # Give FastAPI a moment to start up

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