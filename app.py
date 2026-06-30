
import streamlit as st
from backend.parser import analyze_java_code

st.set_page_config(page_title="Legacy Code Insight Agent", layout="wide")
st.title("🤖 GenAI-Powered Legacy Code Insight Agent (MVP)")

uploaded = st.file_uploader("Upload Java File", type=["java"])

if uploaded:
    code = uploaded.read().decode("utf-8", errors="ignore")
    result = analyze_java_code(code)

    c1,c2,c3 = st.columns(3)
    c1.metric("Classes", result["classes"])
    c2.metric("Methods", result["methods"])
    c3.metric("Imports", result["imports"])

    st.subheader("Project Summary")
    st.write(result["summary"])

    
    question = st.text_input("Ask about the code")
    if question:
        st.success("POC Answer")
        st.write(result["summary"])
