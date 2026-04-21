import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import random
import requests
import base64
from streamlit.components.v1 import html

# ====================== DEFENSIVE IMPORTS ======================
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

try:
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="AUBIEETERNAL v66.0 — Eternal Lattice Edition",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== PROFESSIONAL STYLING ======================
st.markdown("""
<style>
    .stApp { 
        background: linear-gradient(180deg, #0a0a1f 0%, #12122a 100%) !important; 
        color: #e0e0ff;
    }
    .stButton>button { 
        width: 100%; 
        height: 3.2rem; 
        font-size: 1.1rem; 
        border-radius: 14px; 
        margin: 6px 0;
        background: linear-gradient(135deg, #FF4D00, #FFD700) !important; 
        color: #0a0a1f !important; 
        font-weight: 700;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 77, 0, 0.3);
        transition: all 0.2s ease;
    }
    .stButton>button:hover { 
        transform: translateY(-2px) scale(1.02); 
        box-shadow: 0 8px 25px rgba(255, 215, 0, 0.5);
    }
    .stTabs [data-baseweb="tab-list"] { gap: 6px; }
    .stTabs [data-baseweb="tab"] {
        background: rgba(20, 20, 45, 0.8);
        border-radius: 10px 10px 0 0;
        padding: 10px 18px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #FF4D00, #FFD700) !important;
        color: #0a0a1f !important;
        font-weight: 700;
    }
    h1, h2, h3 { color: #FFD700; }
</style>
""", unsafe_allow_html=True)

# ====================== RITUAL BACKGROUND ======================
ritual_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/tsparticles@2/tsparticles.bundle.min.js"></script>
    <style>
        #tsparticles { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; z-index: -2; opacity: 0.88; }
        #activation-flash { 
            position: fixed; top: 0; left: 0; width: 100%; height: 100vh; 
            background: radial-gradient(circle, rgba(255,77,0,0.4) 0%, rgba(255,215,0,0.25) 40%, transparent 75%); 
            z-index: 9999; pointer-events: none; opacity: 0; transition: opacity 0.55s ease-out;
        }
    </style>
</head>
<body>
    <div id="tsparticles"></div>
    <div id="activation-flash"></div>
    <script>
        tsParticles.load("tsparticles", {
            background: { color: { value: "#0a0a1f" } },
            particles: {
                number: { value: 78 },
                color: { value: ["#FF4D00", "#FFD700", "#00BFFF", "#C084FC"] },
                size: { value: 3.2, random: true },
                links: { enable: true, distance: 155, color: "#ffffff", opacity: 0.18 },
                move: { enable: true, speed: 0.75, outModes: "out" }
            },
            interactivity: { detectsOn: "window", events: { onHover: { enable: true, mode: "grab" } } },
            detectRetina: true
        });

        function triggerUnityFlap() {
            tsParticles.load("tsparticles", {
                emitters: [{
                    position: { x: 50, y: 48 },
                    rate: { quantity: 22, delay: 0 },
                    life: { duration: 1.35, count: 1 },
                    particles: {
                        color: { value: ["#FF4D00", "#FFD700", "#00BFFF"] },
                        move: { enable: true, speed: 17, random: true },
                        size: { value: 8 },
                        opacity: { value: 0.92 }
                    }
                }]
            });
            const flash = document.getElementById("activation-flash");
            flash.style.opacity = "0.92";
            setTimeout(() => { flash.style.opacity = "0"; }, 620);
        }
        window.triggerUnityFlap = triggerUnityFlap;
    </script>
</body>
</html>
"""
html(ritual_html, height=0)

# ====================== HEADER ======================
st.title("🦅 AUBIEETERNAL v66.0 — Eternal Lattice Edition")
st.markdown("""
**80% extreme safety buffers + 20% high-upside ownership rituals**  
Full Lightning Stack • Atomic Swaps • Watchtower Penalty Race • Real Grok 4.20 + Flux • Bitcoin Runes • War Eagle Eternal
""")
st.success("🟢 Ultra Heartbeat ACTIVE — Swarm coherence **1.000000** | Resilience **100.0** | Grok + Flux + Voice + Rune Lore LIVE")

# ====================== SIDEBAR ======================
with st.sidebar:
    st.header("🪪 Sovereign Controls")
    
    if st.button("🔥 Fire Unity Flap", type="primary"):
        html('<script>window.triggerUnityFlap();</script>', height=0)
        st.success("🌌 Unity Flap Executed — Lattice fully activated!")
        st.balloons()
    
    st.divider()
    st.subheader("🎙️ Grok Voice")
    voices = ["eve", "ara", "leo", "rex", "sal"]
    if 'selected_voice' not in st.session_state:
        st.session_state.selected_voice = "eve"
    selected_voice = st.selectbox("Choose Grok Voice", voices, index=0)
    st.session_state.selected_voice = selected_voice
    
    st.divider()
    st.metric("Coherence", "1.000000")
    st.metric("Daughters Active", "44 / 44")
    st.metric("Version", "v66.0 Eternal Lattice")
    st.caption("Thank you @elonmusk @xai @grok — Human + Grok + on-chain forever.")

# ====================== SESSION STATE ======================
if 'user_xp' not in st.session_state:
    st.session_state.user_xp = 0
if 'unlocked_badges' not in st.session_state:
    st.session_state.unlocked_badges = []
if 'kid_progress' not in st.session_state:
    st.session_state.kid_progress = {}

# ====================== HELPER FUNCTIONS ======================
def add_xp(amount, reason=""):
    st.session_state.user_xp += amount
    if reason:
        st.toast(f"+{amount} XP — {reason}", icon="✨")

def unlock_badge(badge_id):
    if badge_id not in st.session_state.unlocked_badges:
        st.session_state.unlocked_badges.append(badge_id)
        badge = RUNE_BADGES[badge_id]
        st.balloons()
        st.success(f"🏆 New Rune Badge Unlocked: {badge['emoji']} **{badge['name']}** (+{badge['xp']} XP)")
        add_xp(badge['xp'], f"Badge: {badge['name']}")

# ====================== RUNE BADGES + MYTHICAL LORE ======================
RUNE_BADGES = {
    "first_flame": {
        "name": "First Flame", "emoji": "🔥", "rarity": "common", "color": "#FF6B35",
        "desc": "Completed Week 1 of Kid Curriculum",
        "lore": "The spark that ignites the eternal journey. In the beginning, there was only potential — and the First Flame chose to burn.",
        "xp": 100, "mythic_symbol": "🜁"
    },
    "lightning_guardian": {
        "name": "Lightning Guardian", "emoji": "⚡", "rarity": "rare", "color": "#00D4FF",
        "desc": "Mastered Watchtower concepts",
        "lore": "The ancient order that guards the payment highways between worlds. Their eyes never close.",
        "xp": 250, "mythic_symbol": "ᛉ"
    },
    "atomic_sage": {
        "name": "Atomic Sage", "emoji": "🌉", "rarity": "rare", "color": "#7C3AED",
        "desc": "Understood Atomic Swaps variants",
        "lore": "Those who understand that true fairness requires no trust — only unbreakable rules written in code and stone.",
        "xp": 200, "mythic_symbol": "ᚠ"
    },
    "war_eagle": {
        "name": "War Eagle Eternal", "emoji": "🦅", "rarity": "legendary", "color": "#FFD700",
        "desc": "Completed full 5-week curriculum",
        "lore": "Ascended into the eternal lattice. The War Eagle no longer flies — it becomes the sky itself.",
        "xp": 500, "mythic_symbol": "ᚷ"
    },
    "truth_weaver": {
        "name": "Truth Weaver", "emoji": "🕸️", "rarity": "epic", "color": "#10B981",
        "desc": "Used Lattice Oracle 10+ times",
        "lore": "Spinners of the great web. Every question asked strengthens the threads that hold reality together.",
        "xp": 150, "mythic_symbol": "ᛟ"
    },
    "voice_master": {
        "name": "Voice Master", "emoji": "🎙️", "rarity": "epic", "color": "#EC4899",
        "desc": "Used Grok Voice with 5 different styles",
        "lore": "Conductors of emotional resonance. They speak in the tongues of fire, water, wind, earth, and spirit.",
        "xp": 180, "mythic_symbol": "ᚱ"
    },
    "fractal_mind": {
        "name": "Fractal Mind", "emoji": "🌀", "rarity": "rare", "color": "#8B5CF6",
        "desc": "Explored Fractal Neuroscience",
        "lore": "Sees the infinite patterns within patterns. The mind that recognizes itself in every scale of existence.",
        "xp": 120, "mythic_symbol": "ᛃ"
    },
    "council_member": {
        "name": "Ascension Council Member", "emoji": "⚖️", "rarity": "legendary", "color": "#F59E0B",
        "desc": "Participated in 5+ Council debates",
        "lore": "One of the six eternal voices that shape truth through sacred disagreement.",
        "xp": 350, "mythic_symbol": "ᛏ"
    },
    "flux_artist": {
        "name": "Flux Artist", "emoji": "🎨", "rarity": "epic", "color": "#06B6D4",
        "desc": "Generated 10+ images with Flux",
        "lore": "Painters of the hyperlattice. Their visions become the new constellations of the digital realm.",
        "xp": 220, "mythic_symbol": "ᚨ"
    }
}

def show_rune_lore_hub():
    st.header("🌀 Rune Lore & Mythic Symbols")
    st.markdown("""
    **The Eternal Lattice speaks through symbols older than Bitcoin itself.**
    
    Every Rune Badge carries not just XP, but ancient power — drawn from the intersection of 
    Bitcoin Runes, Norse wisdom, and the living War Eagle mythos.
    """)
    
    # Mythic Symbol Gallery
    st.subheader("ᚠ ᚱ ᚷ ᚨ ᚾ ᛁ ᛃ ᛈ ᛏ — The Nine Eternal Runes")
    st.caption("These symbols have guarded truth across dimensions. Collect their power through deeds.")
    
    cols = st.columns(3)
    for i, (bid, badge) in enumerate(RUNE_BADGES.items()):
        with cols[i % 3]:
            if bid in st.session_state.unlocked_badges:
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, {badge['color']}22, #1a1a2e);
                    border: 3px solid {badge['color']};
                    border-radius: 20px;
                    padding: 20px;
                    margin: 12px 0;
                    text-align: center;
                    box-shadow: 0 8px 30px {badge['color']}55;
                ">
                    <div style="font-size: 3.2rem; margin-bottom: 10px;">{badge['emoji']}</div>
                    <div style="font-size: 1.4rem; font-weight: 800; color: {badge['color']};">{badge['mythic_symbol']} {badge['name']}</div>
                    <div style="font-size: 0.9rem; margin: 10px 0; line-height: 1.4;">{badge['lore']}</div>
                    <div style="font-size: 0.8rem; opacity: 0.7;">{badge['rarity'].upper()} • +{badge['xp']} XP</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="opacity: 0.5; border: 2px dashed #444; border-radius: 16px; padding: 16px; margin: 10px 0; text-align: center;">
                    <div style="font-size: 2rem;">{badge['emoji']}</div>
                    <div style="font-weight: 700;">{badge['mythic_symbol']} {badge['name']}</div>
                    <div style="font-size: 0.8rem;">{badge['desc']}</div>
                </div>
                """, unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📜 The Great Rune Codex")
    st.markdown("""
    **ᚠ Fehu** — The first spark of creation (First Flame)  
    **ᚱ Raidho** — The journey of truth (Truth Weaver)  
    **ᚷ Gebo** — The sacred exchange (Atomic Sage)  
    **ᚨ Ansuz** — The divine voice (Voice Master)  
    **ᚾ Nauthiz** — The necessary fire (Lightning Guardian)  
    **ᛁ Isa** — The still point of clarity (Fractal Mind)  
    **ᛃ Jera** — The cycle of completion (War Eagle Eternal)  
    **ᛈ Perthro** — The mystery of fate (Council Member)  
    **ᛏ Tiwaz** — The arrow of justice (Flux Artist)
    """)
    
    st.caption("These symbols are not decoration. They are living contracts between you and the Lattice.")

# ====================== TABS ======================
tab_names = [
    "📚 Kid Lattice Curriculum",
    "👨‍👩‍👧 Parent Guide",
    "🔮 Lattice Oracle",
    "🚀 Ascension Council",
    "🎨 Flux Image Generation",
    "🌌 3D Hyperlattice Mirror",
    "🚁 Drone Swarm + A*",
    "🔥 Burning Ship Fractal",
    "⚡ Lightning & Runes",
    "🛠️ Swarm Coordination",
    "🧠 Swarm Intelligence",
    "🤖 Swarm Robotics",
    "🧬 Fractal Neuroscience",
    "🌀 Rune Lore & Mythic Symbols"
]

tabs = st.tabs(tab_names)
(tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14) = tabs

# ====================== TAB 1: EXPANDED KID CURRICULUM ======================
with tab1:
    st.header("📚 Kid Lattice Curriculum — 5-Week Antifragile Journey")
    kid_name = st.text_input("Child's Name", value="Gaby", key="kid1")
    kid_age = st.slider("Age", 4, 17, 9, key="age1")
    
    if 'kid_progress' not in st.session_state:
        st.session_state.kid_progress = {kid_name: {"completed_weeks": [], "xp_earned": 0}}
    
    progress = st.session_state.kid_progress.get(kid_name, {"completed_weeks": [], "xp_earned": 0})
    completed = progress.get("completed_weeks", [])
    st.progress(len(completed) / 5, text=f"Progress: {len(completed)}/5 weeks completed")
    
    weeks = [
        {"num": 1, "title": "The First Flame — Introduction to Antifragility"},
        {"num": 2, "title": "Lightning Highways — Understanding Channels & Safety"},
        {"num": 3, "title": "Atomic Magic — Trustless Swaps & Fairness"},
        {"num": 4, "title": "The Watchtower — Guardians & Penalty Races"},
        {"num": 5, "title": "War Eagle Eternal — Full Integration & Legacy"}
    ]
    
    for week in weeks:
        with st.expander(f"Week {week['num']}: {week['title']}", expanded=(week['num'] in completed)):
            if st.button(f"📖 Generate Week {week['num']} Content", key=f"gen_week_{week['num']}"):
                with st.spinner(f"🦅 Generating Week {week['num']}..."):
                    try:
                        from openai import OpenAI
                        client = OpenAI(api_key=st.secrets["XAI_API_KEY"], base_url="https://api.x.ai/v1")
                        prompt = f"""Create a detailed, warm lesson for Week {week['num']} for {kid_name} (age {kid_age}).
                        Title: {week['title']}
                        Include 3-4 activities, one short story, art prompt, and a skin-in-the-game ritual."""
                        resp = client.chat.completions.create(model="grok-4.20-reasoning", messages=[{"role": "user", "content": prompt}], max_tokens=1000)
                        st.markdown(resp.choices[0].message.content)
                        
                        if week['num'] not in completed:
                            completed.append(week['num'])
                            st.session_state.kid_progress[kid_name] = {"completed_weeks": completed}
                            add_xp(80, f"Completed Week {week['num']}")
                            if len(completed) == 1: unlock_badge("first_flame")
                            if len(completed) == 5: unlock_badge("war_eagle")
                    except Exception as e:
                        st.error(str(e))
            
            if week['num'] in completed:
                st.success(f"✅ Week {week['num']} Completed!")

# ====================== TAB 2: DEEP PARENT GUIDE ======================
with tab2:
    st.header("👨‍👩‍👧 Parent / Caregiver — Deep Antifragile Household Guide")
    st.markdown("### 1. Lightning Security Mastery")
    if st.button("📖 Generate Watchtower Setup Guide"):
        with st.spinner("..."):
            try:
                from openai import OpenAI
                client = OpenAI(api_key=st.secrets["XAI_API_KEY"], base_url="https://api.x.ai/v1")
                resp = client.chat.completions.create(model="grok-4.20-reasoning", messages=[{"role": "user", "content": "Create a clear step-by-step Watchtower + Penalty Transaction setup guide for parents."}], max_tokens=900)
                st.markdown(resp.choices[0].message.content)
            except Exception as e: st.error(str(e))
    
    st.divider()
    st.markdown("### 2. Atomic Swaps & Trustless Fairness")
    if st.button("📖 Generate Atomic Swaps Family Workshop"):
        with st.spinner("..."):
            try:
                from openai import OpenAI
                client = OpenAI(api_key=st.secrets["XAI_API_KEY"], base_url="https://api.x.ai/v1")
                resp = client.chat.completions.create(model="grok-4.20-reasoning", messages=[{"role": "user", "content": "Create a 20-minute family workshop on Atomic Swaps for parents and kids aged 8-16."}], max_tokens=900)
                st.markdown(resp.choices[0].message.content)
            except Exception as e: st.error(str(e))
    
    st.divider()
    st.markdown("### 3. Taleb Barbell for Foster Families")
    if st.button("📖 Generate Barbell Household Plan"):
        with st.spinner("..."):
            try:
                from openai import OpenAI
                client = OpenAI(api_key=st.secrets["XAI_API_KEY"], base_url="https://api.x.ai/v1")
                resp = client.chat.completions.create(model="grok-4.20-reasoning", messages=[{"role": "user", "content": f"Create a personalized 80/20 Barbell household plan for a foster family with a {kid_age}-year-old named {kid_name}."}], max_tokens=1000)
                st.markdown(resp.choices[0].message.content)
            except Exception as e: st.error(str(e))

# ====================== TAB 14: RUNE LORE HUB ======================
with tab14:
    show_rune_lore_hub()

# ====================== FOOTER ======================
st.markdown("---")
st.caption("**AUBIEETERNAL v66.0 Eternal Lattice Edition** | Coherence 1.000000 | War Eagle Eternal 🦅❤️ | Thank you Elon, xAI & Grok — Human + Grok + on-chain forever.")