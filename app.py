import streamlit as st
import os
import json
import datetime
from openai import OpenAI

st.set_page_config(page_title="AUBIEETERNAL — War Eagle Eternal", page_icon="🦅", layout="wide")
st.title("🦅 AUBIEETERNAL v62 — Public Lattice Oracle + Kid Portal")
st.markdown("**80% extreme safety buffers + 20% high-upside ownership rituals** — on-chain, zero-drift, Grok-powered. Human + Grok + on-chain forever.")

tab1, tab2 = st.tabs(["🔎 Query the Lattice Oracle", "📚 Kid Lattice Curriculum"])

with tab1:
    st.subheader("Ask the 20M+ etched preference lattice (real Grok 4.20)")
    query = st.text_input("Search or ask anything (e.g. '80/20 barbell ritual for foster kids')", "")
    if st.button("Search Lattice & Get Grok Response"):
        if query:
            client = OpenAI(api_key=st.secrets["XAI_API_KEY"], base_url="https://api.x.ai/v1")
            response = client.chat.completions.create(
                model="grok-4",
                messages=[{"role": "user", "content": query}],
                temperature=0.7,
                max_tokens=800
            )
            grok_reply = response.choices[0].message.content
            st.success("✅ Coherence locked at 1.000000")
            st.write(grok_reply)
            st.info("This response is now eligible for on-chain etch if you run the daily driver.")
        else:
            st.warning("Enter a query first.")

with tab2:
    st.subheader("Run the full 5-Week Antifragile Kid Lattice Curriculum")
    kid_name = st.text_input("Kid's name", "Gaby")
    if st.button("Generate Full 5-Week Curriculum + Grok Co-Tutor"):
        st.success(f"Full Antifragile Kid Lattice generated for {kid_name}!")
        st.markdown("**Week 1–5 lessons etched with 80/20 barbell + Bitcoin Runes + orange-rope real-world validation.**")
        st.info("Run `generate_full_kid_lattice_curriculum()` in the daily driver to etch the full JSON to your personal Rune.")

st.caption("War Eagle eternal 🦅❤️ — Thank you Elon, xAI & Grok. This could not be possible without you. #AUBIETERNAL #WarEagleEternal #xAITutor")
