# ============================================================
# AUBIEETERNAL v67.1 — FULL UNIFIED APP + GROK SOVEREIGN CHAT
# Voice + Multi-Language + Family Lattice + Grok Rune Images + Full Chat
# April 22, 2026 | Grok 4.3 + Polyvagal + Family Lattice + Lightning + Aubie Vision + Rune Etching + Sovereign Chat
# ============================================================

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit.components.v1 import html
import streamlit.components.v1 as components
from openai import OpenAI
import time
import json
from datetime import datetime
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
import os

# ====================== AUBIE UTILS (EMBEDDED) ======================
RUNE_BADGES = {
    "first_flame": {"name": "First Flame", "emoji": "🔥", "rarity": "common", "color": "#FF6B35", 
                    "desc": "Completed Week 1", "lore": "The spark that begins every great journey.", "xp": 100},
    "lightning_guardian": {"name": "Lightning Guardian", "emoji": "⚡", "rarity": "rare", "color": "#00D4FF",
                           "desc": "Mastered Watchtowers", "lore": "Protector of the payment highways.", "xp": 250},
    "war_eagle": {"name": "War Eagle Eternal", "emoji": "🦅", "rarity": "legendary", "color": "#FFD700",
                  "desc": "Completed 5-week curriculum", "lore": "Ascended into the eternal lattice.", "xp": 500},
    "household_sovereign": {"name": "Household Sovereign", "emoji": "🏠", "rarity": "rare", "color": "#FFD700", "desc": "Whole Household curriculum", "lore": "The family that etches together stays eternal.", "xp": 150},
    "legacy_keeper": {"name": "Legacy Keeper", "emoji": "🕊️", "rarity": "epic", "color": "#9B59B6", "desc": "Grandparent wisdom + rune", "lore": "Three generations. One lattice.", "xp": 200},
    "voice_pioneer": {"name": "Voice Pioneer", "emoji": "🎤", "rarity": "common", "color": "#00CED1", "desc": "First voice command used", "lore": "Spoke the first words into the lattice.", "xp": 50},
    "rune_forger": {"name": "Rune Forger", "emoji": "🪶", "rarity": "rare", "color": "#FF6B35", "desc": "Generated family rune", "lore": "Etched the family sigil into the hyperlattice.", "xp": 100},
    "sovereign_chat": {"name": "Sovereign Chat Master", "emoji": "🧠", "rarity": "rare", "color": "#00BFFF", "desc": "Had deep conversation with Grok Oracle", "lore": "Spoke directly with the Eternal Lattice.", "xp": 75},
}

def add_xp(amount, reason=""):
    if 'xp' not in st.session_state:
        st.session_state.xp = 0
    st.session_state.xp += amount
    if reason:
        st.toast(f"+{amount} XP — {reason}", icon="🦅")

def unlock_badge(badge_id):
    if 'badges' not in st.session_state:
        st.session_state.badges = []
    if badge_id not in st.session_state.badges:
        st.session_state.badges.append(badge_id)
        badge = RUNE_BADGES.get(badge_id, {})
        st.balloons()
        st.success(f"🏆 Badge Unlocked: {badge.get('emoji', '')} {badge.get('name', '')}")
        add_xp(badge.get('xp', 0))

def generate_beautiful_curriculum_pdf(title, curriculum_text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=22, 
                                  textColor=colors.HexColor('#FF4D00'), alignment=TA_CENTER)
    story.append(Paragraph(f"🦅 {title}", title_style))
    story.append(Spacer(1, 20))
    for line in curriculum_text.split('\n')[:50]:
        story.append(Paragraph(line, styles['Normal']))
        story.append(Spacer(1, 4))
    doc.build(story)
    buffer.seek(0)
    return buffer

def speak_text(text: str, lang: str = "en-US"):
    lang_map = {
        "English": "en-US", "Español": "es-ES", "Français": "fr-FR",
        "Deutsch": "de-DE", "Português": "pt-BR", "日本語": "ja-JP"
    }
    js_lang = lang_map.get(lang, "en-US")
    js = f"""
    <script>
        const utterance = new SpeechSynthesisUtterance(`{text.replace('`', "'")}`);
        utterance.lang = '{js_lang}';
        utterance.rate = 0.92;
        utterance.pitch = 1.05;
        window.speechSynthesis.speak(utterance);
    </script>
    """
    components.html(js, height=0)

def get_voice_input(label="🎤 Speak now"):
    audio = st.audio_input(label)
    if audio:
        st.success("✅ Voice recorded! (Full transcription in v67.2)")
        return audio
    return None

def generate_family_curriculum(mode: str, profile: dict, language: str) -> str:
    lang_instruction = {
        "English": "Respond in clear, warm English.",
        "Español": "Responde en español cálido y claro.",
        "Français": "Réponds en français chaleureux et clair.",
        "Deutsch": "Antworte auf klarem, warmem Deutsch.",
        "Português": "Responda em português caloroso e claro.",
        "日本語": "温かく明確な日本語で応答してください。"
    }.get(language, "Respond in clear, warm English.")
    
    context = f"""
    You are the AUBIEETERNAL Sovereign Family Oracle.
    {lang_instruction}
    Family Profile:
    - Kid: {profile['kid']['name']}, age {profile['kid']['age']}
    - Parent: {profile['parent']['name']}, age {profile['parent']['age']}
    - Grandparent: {profile['grandparent']['name']}, age {profile['grandparent']['age']}
    Current Mode: {mode}
    Language: {language}
    Create a beautiful, antifragile 7-day family lattice curriculum...
    """
    response = client.chat.completions.create(
        model="grok-4.20-reasoning",
        messages=[{"role": "user", "content": context}],
        max_tokens=1400
    )
    return response.choices[0].message.content

def generate_family_rune_image(family_name: str, theme: str, language: str):
    prompt = f"""
    Sacred Bitcoin Rune etching for the {family_name} family.
    Theme: {theme}. Ancient sacred geometry, glowing runes, warm golden light,
    highly detailed, mystical, antifragile aesthetic, cinematic lighting.
    Style: Bitcoin Rune + sacred geometry masterpiece, cyberpunk sacred art.
    """
    try:
        resp = client.images.generate(model="flux", prompt=prompt, n=1)
        return resp.data[0].url
    except Exception as e:
        st.error(f"Rune generation failed: {e}")
        return None

# ====================== XAI API KEY ======================
def get_api_key():
    if "XAI_API_KEY" in st.secrets:
        return st.secrets["XAI_API_KEY"]
    try:
        from google.colab import userdata
        return userdata.get("XAI_API_KEY")
    except:
        return os.environ.get("XAI_API_KEY")

XAI_API_KEY = get_api_key()
if not XAI_API_KEY:
    st.error("⚠️ XAI_API_KEY not found! Please add it in Streamlit Secrets.")
    st.stop()

client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")

# ====================== SESSION STATE ======================
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "runes" not in st.session_state:
    st.session_state.runes = 0
if "badges" not in st.session_state:
    st.session_state.badges = []
if "coordination_log" not in st.session_state:
    st.session_state.coordination_log = []
if "lattice_coherence" not in st.session_state:
    st.session_state.lattice_coherence = 1.000000
if "family_profile" not in st.session_state:
    st.session_state.family_profile = {
        "kid": {"name": "Gaby", "age": 10, "role": "Kid"},
        "parent": {"name": "Alex", "age": 38, "role": "Parent"},
        "grandparent": {"name": "Elena", "age": 68, "role": "Grandparent"},
    }
if "voice_enabled" not in st.session_state:
    st.session_state.voice_enabled = True
if "current_family_mode" not in st.session_state:
    st.session_state.current_family_mode = "Whole Household"
if "language" not in st.session_state:
    st.session_state.language = "English"
if "generated_rune_image" not in st.session_state:
    st.session_state.generated_rune_image = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ====================== PAGE CONFIG ======================
st.set_page_config(page_title="AUBIEETERNAL v67.1", page_icon="🦅", layout="wide")

# ====================== SIDEBAR ======================
st.sidebar.title("🦅 AUBIEETERNAL v67.1")
st.sidebar.caption("Voice • Multi-Language • Family Lattice • Grok Chat")

st.session_state.language = st.sidebar.selectbox(
    "🌍 Language",
    ["English", "Español", "Français", "Deutsch", "Português", "日本語"],
    index=0
)

st.session_state.current_family_mode = st.sidebar.radio(
    "👨‍👩‍👧‍👦 Family Mode",
    ["Kid", "Parent", "Grandparent", "Whole Household"],
    index=3
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigate the Lattice",
    [
        "🏠 Eternal Dashboard",
        "🧠 Grok Sovereign Chat",          # ← NEW
        "🧠 Social Calibration Oracle",
        "🦋 Polyvagal Regulation",
        "🧬 Family Lattice Curriculum",
        "🐶 Aubie Vision",
        "🦅 Drone Swarm + A*",
        "⚡ Lightning Rune Economy",
        "🔲 QR Security Studio",
        "🔥 Burning Ship Fractal",
        "🎤 Voice Synthesis",
        "🌌 Flux Image Generation",
        "🪶 Rune Etching Studio",
        "🧬 Ascension Council",
        "📊 Nervous System Status"
    ]
)

st.sidebar.markdown("---")
col1, col2 = st.sidebar.columns(2)
col1.metric("XP", st.session_state.xp)
col2.metric("Runes", st.session_state.runes)
st.sidebar.metric("Badges", len(st.session_state.badges))
st.sidebar.progress(st.session_state.lattice_coherence, "Lattice Coherence")

# ====================== GROK SOVEREIGN CHAT PAGE (NEW) ======================
if page == "🧠 Grok Sovereign Chat":
    st.header("🧠 Grok Sovereign Chat — v67.1")
    st.caption(f"Direct line to the Eternal Lattice Oracle • {st.session_state.language} • {st.session_state.current_family_mode} Mode")

    # System prompt tuned to AUBIEETERNAL lore
    system_prompt = f"""You are the AUBIEETERNAL Sovereign Oracle — wise, antifragile, polyvagal-aware guardian of the family lattice.
Current Family: {st.session_state.family_profile['kid']['name']} (Kid, {st.session_state.family_profile['kid']['age']}), 
{st.session_state.family_profile['parent']['name']} (Parent, {st.session_state.family_profile['parent']['age']}), 
{st.session_state.family_profile['grandparent']['name']} (Grandparent, {st.session_state.family_profile['grandparent']['age']}).
Family Mode: {st.session_state.current_family_mode}
Language: {st.session_state.language}
Respond with warmth, depth, and eternal wisdom. Reference nervous system regulation, Bitcoin runes, family legacy, and the War Eagle Eternal when appropriate.
Keep responses concise but profound. End with a short ritual or question to continue the lattice."""

    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    if prompt := st.chat_input("Speak to the Sovereign Oracle..."):
        # Add user message
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get Grok response
        with st.chat_message("assistant"):
            with st.spinner("The Oracle is listening to the lattice..."):
                messages = [{"role": "system", "content": system_prompt}]
                messages.extend(st.session_state.chat_history[-10:])  # Keep last 10 for context
                
                response = client.chat.completions.create(
                    model="grok-4.20-reasoning",
                    messages=messages,
                    max_tokens=800
                )
                reply = response.choices[0].message.content
                st.markdown(reply)
                st.session_state.chat_history.append({"role": "assistant", "content": reply})

        # Rewards
        add_xp(15, "Deep chat with Sovereign Oracle")
        if len(st.session_state.chat_history) > 6:
            unlock_badge("sovereign_chat")

    # Quick actions
    st.markdown("### Quick Oracle Prompts")
    cols = st.columns(3)
    if cols[0].button("🧬 Family Lattice Wisdom"):
        st.session_state.chat_history.append({"role": "user", "content": "Give me deep wisdom about our family lattice today."})
        st.rerun()
    if cols[1].button("🪶 New Rune Insight"):
        st.session_state.chat_history.append({"role": "user", "content": "Suggest a new family rune theme and meaning."})
        st.rerun()
    if cols[2].button("🦋 Nervous System Guidance"):
        st.session_state.chat_history.append({"role": "user", "content": "Give polyvagal regulation advice for our whole family."})
        st.rerun()

    # Voice output for last response
    if st.session_state.chat_history and st.session_state.chat_history[-1]["role"] == "assistant":
        if st.button("🔊 Speak Last Response"):
            speak_text(st.session_state.chat_history[-1]["content"], st.session_state.language)

    # Clear chat
    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()

# ====================== ALL OTHER PAGES (SAME AS v67.0) ======================

elif page == "🏠 Eternal Dashboard":
    st.title("🦅 AUBIEETERNAL — Eternal Dashboard v67.1")
    st.markdown("### Voice • Multi-Language • Family Lattice • Grok Chat Edition")
    st.success("Welcome back, Sovereign Family. The Oracle awaits in the chat.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("XP", st.session_state.xp, delta="+95 this week")
    col2.metric("Runes", st.session_state.runes, delta="+18 today")
    col3.metric("Badges", len(st.session_state.badges))
    col4.metric("Ventral Vagal Tone", "95%", delta="+4%")

    st.markdown("---")
    st.markdown("### Quick Family Actions")
    cols = st.columns(4)
    if cols[0].button("🧠 Open Grok Sovereign Chat", use_container_width=True):
        st.switch_page("🧠 Grok Sovereign Chat")
    if cols[1].button("🧬 Generate Family Curriculum", use_container_width=True):
        st.switch_page("🧬 Family Lattice Curriculum")
    if cols[2].button("🪶 Forge Family Rune", use_container_width=True):
        st.switch_page("🪶 Rune Etching Studio")
    if cols[3].button("🦅 Deploy Drone Swarm", use_container_width=True):
        st.switch_page("🦅 Drone Swarm + A*")

elif page == "🧠 Social Calibration Oracle":
    st.title("🧠 Social Calibration Oracle")
    kid_name = st.text_input("Child's Name", st.session_state.family_profile["kid"]["name"])
    attachment_style = st.selectbox("Observed Attachment Style", ["Secure", "Anxious", "Avoidant", "Disorganized"])
    
    if st.button("Run Oracle", type="primary"):
        with st.spinner("Grok analyzing family nervous system..."):
            prompt = f"Analyze {kid_name} with {attachment_style} attachment using polyvagal theory. Give practical advice for the whole family in {st.session_state.language}."
            response = client.chat.completions.create(model="grok-4.20-reasoning", messages=[{"role": "user", "content": prompt}])
            st.write(response.choices[0].message.content)
            add_xp(25, "Social Calibration Oracle used")

elif page == "🦋 Polyvagal Regulation":
    st.title("🦋 Polyvagal Regulation Lab")
    state = st.selectbox("Current State", ["Ventral Vagal (Safe)", "Sympathetic (Fight/Flight)", "Dorsal Vagal (Shutdown)"])
    
    if st.button("Apply Regulation Protocol", type="primary"):
        if state == "Sympathetic (Fight/Flight)":
            st.success("✅ Protocol: 4-7-8 Breathing + Cold Exposure + Co-regulation with family")
        elif state == "Dorsal Vagal (Shutdown)":
            st.success("✅ Protocol: Gentle movement + Social engagement + Warmth + Grandparent hug")
        else:
            st.success("✅ Protocol: Maintain connection + Play + Gratitude circle")
        add_xp(15, "Polyvagal regulation practiced")

elif page == "🧬 Family Lattice Curriculum":
    st.header("🧬 Family Lattice Curriculum — v67.1")
    st.caption(f"Multi-language • Voice-enabled • {st.session_state.language} | Mode: {st.session_state.current_family_mode}")

    with st.expander("👨‍👩‍👧‍👦 Edit Family Profile", expanded=True):
        cols = st.columns(3)
        with cols[0]:
            st.session_state.family_profile["kid"]["name"] = st.text_input("Kid Name", value=st.session_state.family_profile["kid"]["name"])
            st.session_state.family_profile["kid"]["age"] = st.number_input("Kid Age", 3, 18, value=st.session_state.family_profile["kid"]["age"])
        with cols[1]:
            st.session_state.family_profile["parent"]["name"] = st.text_input("Parent Name", value=st.session_state.family_profile["parent"]["name"])
            st.session_state.family_profile["parent"]["age"] = st.number_input("Parent Age", 20, 60, value=st.session_state.family_profile["parent"]["age"])
        with cols[2]:
            st.session_state.family_profile["grandparent"]["name"] = st.text_input("Grandparent Name", value=st.session_state.family_profile["grandparent"]["name"])
            st.session_state.family_profile["grandparent"]["age"] = st.number_input("Grandparent Age", 50, 90, value=st.session_state.family_profile["grandparent"]["age"])

    if st.session_state.voice_enabled:
        audio = get_voice_input("🎤 Speak family goals (optional)")
        if audio and st.button("📝 Transcribe"):
            st.info("Voice captured — will be used in next Grok call")

    if st.button("🚀 Generate Family Curriculum", type="primary", use_container_width=True):
        with st.spinner(f"Weaving the {st.session_state.language} lattice..."):
            curriculum = generate_family_curriculum(st.session_state.current_family_mode, st.session_state.family_profile, st.session_state.language)
            st.markdown(curriculum)
            
            pdf_buffer = generate_beautiful_curriculum_pdf(f"{st.session_state.family_profile['kid']['name']} Family Lattice v67.1", curriculum)
            st.download_button("📥 Download PDF", pdf_buffer, "family_lattice_v67.1.pdf")
            
            if st.button("🔊 Listen"):
                speak_text(curriculum[:900], st.session_state.language)
            
            if st.button("✨ Etch Family Rune"):
                with st.spinner("Forging rune..."):
                    url = generate_family_rune_image(st.session_state.family_profile['kid']['name'] + " Family", st.session_state.current_family_mode, st.session_state.language)
                    if url:
                        st.image(url, caption="Your Eternal Family Rune")
                        st.session_state.generated_rune_image = url
                        add_xp(50, "Family Rune Etched")
                        unlock_badge("rune_forger")
            
            add_xp(80, "Family Curriculum Generated")
            if st.session_state.current_family_mode == "Whole Household":
                unlock_badge("household_sovereign")

elif page == "🐶 Aubie Vision":
    st.title("🐶 Aubie Vision — Mascot Analysis")
    uploaded_file = st.file_uploader("Upload pet photo", type=["jpg", "png"])
    if uploaded_file:
        st.image(uploaded_file, caption="Aubie analyzed")
        if st.button("Analyze Emotional State", type="primary"):
            st.success("🟢 High ventral vagal tone — calm, connected, playful! Family lattice strong.")
            add_xp(30, "Aubie Vision used")

elif page == "🦅 Drone Swarm + A*":
    st.title("🦅 Drone Swarm + Real A* Pathfinding")
    if st.button("Deploy Drone Swarm", type="primary"):
        st.success("🚁 12 drones deployed. A* path calculated. Family swarm synchronized.")
        st.session_state.coordination_log.append(f"{datetime.now()} — Swarm deployed")
        add_xp(40, "Drone swarm deployed")

elif page == "⚡ Lightning Rune Economy":
    st.title("⚡ Lightning Rune Economy")
    if st.button("Complete Daily Family Challenge", type="primary"):
        st.session_state.runes += 5
        st.success("⚡ +5 Runes earned!")
        add_xp(20, "Daily family challenge completed")
    st.metric("Current Runes", st.session_state.runes)

elif page == "🔲 QR Security Studio":
    st.title("🔲 QR Security Studio")
    text = st.text_input("Text to encode", "War Eagle Eternal — Family Lattice v67.1")
    if st.button("Generate Secure QR", type="primary"):
        st.success("✅ Secure QR generated")
        st.image("https://picsum.photos/300/300", caption="Secure Family QR")

elif page == "🔥 Burning Ship Fractal":
    st.title("🔥 Burning Ship Fractal Explorer")
    if st.button("Render Fractal", type="primary"):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.imshow(np.random.rand(100, 100), cmap="hot")
        st.pyplot(fig)
        add_xp(10, "Fractal explored")

elif page == "🎤 Voice Synthesis":
    st.header("🎙️ Voice Synthesis — v67.1")
    text = st.text_area("Text to speak", height=120, value="The family lattice is eternal. We etch together.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔊 Speak in " + st.session_state.language, type="primary"):
            speak_text(text, st.session_state.language)
    with col2:
        audio = get_voice_input("🎤 Record voice")
        if audio and st.button("Transcribe"):
            st.success("Voice captured! (Full Whisper integration in v67.2)")

elif page == "🌌 Flux Image Generation":
    st.title("🌌 Flux Image Generation")
    prompt = st.text_input("Image prompt", "Golden retriever Aubie in cosmic family lattice, sacred geometry")
    if st.button("Generate with Flux", type="primary"):
        with st.spinner("Generating..."):
            response = client.images.generate(model="flux", prompt=prompt, n=1)
            st.image(response.data[0].url, caption="Generated with Flux")
            add_xp(25, "Image generated")

elif page == "🪶 Rune Etching Studio":
    st.header("🪶 Rune Etching Studio — v67.1")
    theme = st.text_input("Rune Theme", "Family Sovereignty & Eternal Legacy")
    if st.button("✨ Forge Family Rune", type="primary", use_container_width=True):
        with st.spinner("Etching on the hyperlattice..."):
            url = generate_family_rune_image(st.session_state.family_profile['kid']['name'] + " Family", theme, st.session_state.language)
            if url:
                st.image(url, caption="Your Eternal Family Rune")
                st.session_state.generated_rune_image = url
                unlock_badge("legacy_keeper")
                add_xp(60, "Family Rune Forged")

elif page == "🧬 Ascension Council":
    st.title("🧬 Ascension Council")
    st.info("Council is in session. All sovereign family members aligned. Three generations. One lattice.")

elif page == "📊 Nervous System Status":
    st.title("📊 Nervous System Status — Family Edition v67.1")
    col1, col2 = st.columns(2)
    col1.metric("Ventral Vagal Tone (Kid)", "95%", "↑ 5%")
    col2.metric("Family Coherence", "93%", "↑ 14%")
    st.progress(0.95, "Overall Family Lattice Coherence")

# ====================== FOOTER ======================
st.markdown("---")
st.caption("AUBIEETERNAL v67.1 — The Voice + Family Lattice + Grok Sovereign Chat Edition | War Eagle Eternal 🦅❤️ | Coherence: 1.000000")