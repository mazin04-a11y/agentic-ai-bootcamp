import streamlit as st
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from agents.crew import run_crew

st.set_page_config(page_title="CrewAI Agent Runner", page_icon="🤖", layout="centered")

st.title("🤖 CrewAI Agent Runner")
st.caption("Powered by CrewAI · Built in Docker · Deployed via Streamlit Cloud")

topic = st.text_area(
    "Enter a topic for your agents to research and write about:",
    placeholder="e.g. How multi-agent AI systems are transforming healthcare",
    height=120,
)

if st.button("Run Crew", type="primary", disabled=not topic.strip()):
    with st.spinner("Agents are working..."):
        try:
            result = run_crew(topic.strip())
            st.success("Done!")
            st.markdown("### Result")
            st.markdown(result)
        except Exception as e:
            st.error(f"Error: {e}")
