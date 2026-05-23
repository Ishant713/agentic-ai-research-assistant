import streamlit as st
import requests

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
                    timeout=60
                )
                response.raise_for_status()

                data = response.json()
                answer = data.get("answer", "")

                if answer:
                    st.write(answer)
                else:
                    st.warning("Backend returned no answer. Please try again or check the backend service.")

            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {e}")
            except ValueError:
                st.error("Received an invalid response from the backend.")