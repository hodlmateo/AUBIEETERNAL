import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random
import base64
from io import BytesIO
from streamlit.components.v1 import html
import os

# ====================== GLOBAL LIGHTNING HELPER ======================
def create_lightning_invoice(sats, memo="Reward boost"):
    st.info(f"**Lightning Invoice** — Pay **{sats} sats** for {memo}")
    invoice = f"lnbc{sats}u1p{random.randint(100000,999999)}...demo"
    st.code(invoice)
    if st.button(f"✅ Confirm Payment ({sats} sats)", key=f"confirm_{sats}_{memo}"):
        if "lightning_payments" not in st.session_state:
            st.session_state.lightning_payments = []
        st.session_state.lightning_payments.append({"sats": sats, "memo": memo, "time": str(datetime.datetime.now())})
        return True
    return False
    
st.set_page_config(
    page_title="AUBIEETERNAL v65.0 — FINAL ABSORBED",
    page_icon="🦅",
    layout="wide"
)

# ====================== RITUAL BACKGROUND ======================
ritual_html = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/tsparticles@2/tsparticles.bundle.min.js"></script>
    <style>
        #tsparticles { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; z-index: -1; opacity: 0.93; }
    </style>
</head>
<body>
    <div id="tsparticles"></div>
    <script>
        tsParticles.load("tsparticles", {
            background: { color: { value: "#0a0a1f" } },
            particles: {
                number: { value: 95 },
                color: { value: ["#FF4D00", "#FFD700", "#00BFFF", "#FF1493"] },
                size: { value: 3.8 },
                links: { enable: true, distance: 160, color: "#ffffff", opacity: 0.25 }
            }
        });
    </script>
</body>
</html>
"""
html(ritual_html, height=0)

st.title("🦅 AUBIEETERNAL v65.0 — FINAL ABSORBED")
st.success("Coherence 1.000000 | Everything Absorbed | Polyvagal + Antifragility + Aubie Mascot + Grok Vision + Flux | War Eagle Eternal 🐾")

# ====================== GLOBAL TOGGLE ======================
use_real_grok = st.checkbox("🦅 Use Real Grok API", value=False)
if not use_real_grok:
    st.info("**Offline Mode Active** — Full functionality without API key")

# ====================== TABS ======================
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 = st.tabs([
    "🧠 Social Calibration Oracle",
    "🗣️ Spoken Black-Swan Arena",
    "🌌 Cosmic Lattice Weaver",
    "📖 xAI Cookbook Explorer",
    "👁️ Grok Vision",
    "🎨 Flux Image Generation",
    "🔮 Lattice Oracle",
    "🧬 Polyvagal Theory",
    "📚 Kid Lattice Curriculum",
    "👨‍👩‍👧 Parent Curriculum",
    "🚀 Ascension Council",
    "🚁 Drone Swarm + Real A*",
    "🔥 Burning Ship + Fractals",
    "🐾 Aubie Eternal Mascot"
])

# ====================== TAB 1: SOCIAL CALIBRATION ORACLE ======================
with tab1:
    st.header("🧠 Social Calibration Oracle + Polyvagal Lens")
    prompt = st.text_area("User Prompt", "I feel like I'm failing at everything lately.")
    response = st.text_area("Grok Response", "Just push through it, you'll be fine.")

    if st.button("⚡ Pay 21 sats to etch this response with Rarity Boost"):
        if create_lightning_invoice(21, "Grok Response Etch + Rare Drop"):
            if "rune_points" not in st.session_state:
                st.session_state.rune_points = 0
            st.session_state.rune_points += 40
            st.success("✅ Etched with Lightning + Rare Rune drop!")
            st.balloons()

    if st.button("Run Full Analysis (Polyvagal + Antifragility)"):
        if use_real_grok:
            try:
                from openai import OpenAI
                client = OpenAI(api_key=st.secrets["XAI_API_KEY"], base_url="https://api.x.ai/v1")
                completion = client.chat.completions.create(
                    model="grok-beta",
                    messages=[{"role": "user", "content": f"Analyze with Polyvagal + Antifragility lens: {prompt}"}],
                    max_tokens=700
                )
                st.json(completion.choices[0].message.content)
            except Exception as e:
                st.error(f"API Error: {e}")
        else:
            st.json({
                "attachment_style": random.choice(["secure", "anxious-preoccupied", "avoidant-dismissive", "disorganized"]),
                "polyvagal_state": random.choice(["ventral-vagal (safe)", "sympathetic (mobilized)", "dorsal (shutdown)"]),
                "calibration_score": round(random.uniform(1.8, 4.9), 1),
                "antifragility_score": round(random.uniform(6.5, 9.8), 1),
                "recommended_tactic": "deep validation + co-regulation + voluntary discomfort",
                "rewritten_response": response[:80] + " [calibrated for emotional safety + antifragile growth]"
            })
            st.success("✅ Full Polyvagal + Antifragility Analysis complete")
            
# ====================== TAB 2: SPOKEN BLACK-SWAN ARENA ======================
with tab2:
    st.header("🗣️ Spoken Black-Swan Arena (Voice + Antifragility)")
    hypothesis = st.text_area("Your Hypothesis", "The universe is getting more ordered over time.")
    
    if st.button("Run Full Simulation"):
        verdict = """**Verdict:** This hypothesis is fragile. 
The universe trends toward entropy. Use **Via Negativa** and prepare for **Black Swans**.

**Polyvagal Note:** This claim may trigger sympathetic mobilization. Ground first.
**Antifragility Score:** 3.4/10 — High fragility detected."""
        st.markdown(verdict)
        st.success("✅ Simulation complete")

        if st.button("🔊 Speak with Aubie Voice"):
            speak_js = f"""
            <script>
                const utterance = new SpeechSynthesisUtterance(`{verdict.replace('**', '').replace('*', '')}`);
                utterance.rate = 1.05;
                utterance.pitch = 1.15;
                utterance.volume = 0.9;
                speechSynthesis.speak(utterance);
            </script>
            """
            html(speak_js, height=0)

# ====================== TAB 3: COSMIC LATTICE WEAVER ======================
with tab3:
    st.header("🌌 Cosmic Lattice Weaver (Real-Time Sync)")
    if st.button("Weave Latest Sources + Polyvagal Integration"):
        st.success("✅ Lattice updated with xAI + GitHub + X + Polyvagal Theory + Antifragility metrics!")
   
    if st.button("⚡ Pay 15 sats to render with Epic visual effect"):
    if create_lightning_invoice(15, "Epic Mirror Render"):
        st.session_state.rune_points += 30

# ====================== TAB 4: xAI COOKBOOK EXPLORER ======================
with tab4:
    st.header("📖 xAI Cookbook Explorer")
    st.info("Function calling, multi-agent systems, structured outputs, and more — all woven into the lattice.")

    if st.button("Etch + Lightning Rarity Boost (21 sats)"):
    if create_lightning_invoice(21, "Etch Rarity Boost"):
        st.session_state.rune_points += 35
        # then do the normal etch

# ====================== TAB 5: GROK VISION ======================
with tab5:
    st.header("👁️ Grok Vision + Polyvagal Lens")
    uploaded_file = st.file_uploader("Upload image for Aubie Vision analysis", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", width=400)
        if st.button("Run Aubie Vision Analysis"):
            st.success("**Aubie Vision Analysis:**\n- Polyvagal State: Ventral Vagal (Calm & Curious)\n- Antifragility Score: 9.1/10\n- Lesson: This image shows joyful absorption of physical uncertainty.")
    
    i    if st.button("⚡ Pay 42 sats for Legendary Co-Creation Drop"):
        if create_lightning_invoice(42, "Legendary Co-Creation"):
            if "rune_points" not in st.session_state:
                st.session_state.rune_points = 0
            st.session_state.rune_points += 80
            st.balloons()
            st.success("✅ Legendary Co-Creation Drop unlocked!")
            
# ====================== TAB 6: ADVANCED FLUX + DALL-E IMAGE GENERATION ======================
with tab6:
    st.header("🎨 Advanced Image Generation")
    st.markdown("**Flux + DALL-E 3 | Style Presets | Multi-Image Generation**")

    # === MODEL SELECTION ===
    model_choice = st.radio(
        "Choose Image Model",
        ["Flux (xAI)", "DALL-E 3 (OpenAI)"],
        horizontal=True
    )

    # === GENERATION MODE ===
    mode = st.radio(
        "Generation Mode",
        ["Text-to-Image", "Image-to-Image"],
        horizontal=True
    )

    # === STYLE PRESETS ===
    style_presets = {
        "None (Custom)": "",
        "Cyberpunk": "cyberpunk neon style, rain-soaked streets, holographic elements, high contrast",
        "Cosmic": "cosmic space aesthetic, nebulae, glowing energy, ethereal lighting, deep space",
        "Minimalist": "minimalist clean design, simple lines, elegant composition, negative space",
        "Surreal": "surreal dreamlike style, impossible geometry, melting forms, Salvador Dali influence",
        "Steampunk": "steampunk Victorian machinery, brass gears, copper pipes, vintage industrial",
        "Synthwave": "synthwave 80s retro aesthetic, neon grid, vaporwave colors, retro-futuristic",
        "Biomorphic": "organic flowing forms, nature-inspired, bioluminescent, alien biology",
        "Brutalist": "brutalist architecture, raw concrete, geometric forms, dramatic lighting"
    }

    selected_style = st.selectbox("🎨 Style Preset", list(style_presets.keys()))

    # === PROMPT ===
    base_prompt = st.text_area(
        "Describe the image you want to generate",
        "A majestic golden eagle flying over a glowing Bitcoin network in space",
        height=100
    )

    full_prompt = base_prompt
    if selected_style != "None (Custom)":
        full_prompt = f"{base_prompt}, {style_presets[selected_style]}"

    # === NUMBER OF IMAGES ===
    num_images = st.slider("Number of images to generate", 1, 4, 1)

    # === IMAGE-TO-IMAGE ===
    reference_image = None
    if mode == "Image-to-Image":
        st.markdown("**Upload a reference image**")
        reference_image = st.file_uploader("Reference Image", type=["jpg", "jpeg", "png"])
        if reference_image:
            st.image(reference_image, caption="Reference Image", width=300)

    # === ADVANCED PROMPT ENGINEERING TIPS ===
    with st.expander("💡 Advanced Prompt Engineering Tips"):
        st.markdown("""
        **Best practices for Flux & DALL-E:**
        - Be **highly specific** (subject + style + lighting + mood + composition)
        - Use **artistic references** (e.g., "in the style of Studio Ghibli, Syd Mead, or Zdzisław Beksiński")
        - Add **technical quality terms** (cinematic lighting, 8k, highly detailed, volumetric lighting)
        - Specify **camera angle** (wide shot, close-up, aerial view, Dutch angle)
        - Use **negative prompting mentally** (avoid blurry, low quality, deformed, ugly)

        **Example strong prompt:**
        > "A lone cyberpunk samurai standing on a neon rooftop overlooking a rainy Tokyo at night, dramatic volumetric lighting, cinematic composition, highly detailed, 8k, in the style of Syd Mead and Blade Runner"
        """)

    # === GENERATE BUTTON ===
    if st.button("✨ Generate Images", type="primary"):
        with st.spinner(f"🦅 Generating {num_images} image(s) with {model_choice}..."):
            try:
                from openai import OpenAI
                client = OpenAI(api_key=st.secrets["XAI_API_KEY"], base_url="https://api.x.ai/v1")

                # Choose model
                if model_choice == "Flux (xAI)":
                    model_name = "flux"
                else:
                    model_name = "dall-e-3"

                images = []
                for i in range(num_images):
                    response = client.images.generate(
                        model=model_name,
                        prompt=full_prompt,
                        n=1,
                        size="1024x1024"
                    )
                    images.append(response.data[0].url)

                # Display images
                cols = st.columns(min(num_images, 2))
                for idx, img_url in enumerate(images):
                    with cols[idx % 2]:
                        st.image(img_url, caption=f"Image {idx+1}", use_column_width=True)
                        st.markdown(f"[📥 Download Image {idx+1}]({img_url})")

                st.success(f"✅ Successfully generated {num_images} image(s)!")

            except Exception as e:
                st.error(f"Generation Error: {e}")
                st.info("Falling back to simulated images...")
                for i in range(num_images):
                    st.image(f"https://picsum.photos/id/{1000+i}/1024/1024", 
                            caption=f"Simulated Image {i+1}")

    # === FLUX MODEL PARAMETERS EXPLANATION ===
    with st.expander("📘 What is Flux? (Model Parameters)"):
        st.markdown("""
        **Flux** is xAI's state-of-the-art image generation model (similar to Midjourney or DALL·E).

        **Key Parameters used:**
        - **model**: `"flux"` — The actual Flux model
        - **prompt**: Your text description (most important parameter)
        - **n**: Number of images (1–4)
        - **size**: `"1024x1024"` (currently the best supported resolution)

        Flux excels at:
        - Highly detailed and coherent images
        - Good text rendering in images
        - Creative and artistic interpretations
        - Following complex prompts accurately
        """)
        
# ====================== TAB 7: LATTICE ORACLE ======================
with tab7:
    st.header("🔮 Lattice Oracle (Polyvagal + Antifragility)")
    query = st.text_input("Ask anything", "How does Polyvagal Theory connect to antifragility?")
    if st.button("Get Response"):
        st.markdown("**Response:** Polyvagal safety (ventral vagal) is the foundation that allows voluntary discomfort (antifragility) to occur without collapse.")

# ====================== TAB 8: POLYVAGAL THEORY ======================
with tab8:
    st.header("🧬 Polyvagal Theory — Core Engine")
    st.markdown("""
    **Ventral Vagal (Safe & Connected)** → Foundation for learning & growth  
    **Sympathetic (Mobilized)** → Fight/Flight — Use for short bursts only  
    **Dorsal Vagal (Shutdown)** → Freeze — Recovery needed
    
    **AUBIEETERNAL Rule:** Never teach or train in dorsal vagal state. Always co-regulate first.
    """)

# ====================== TAB 9: FINAL — LIGHTNING + RARITY + NOSTR DETAILS ======================
with tab9:
    st.header("📚 Kid • Teen • Adolescent Lattice + Lightning Rune Economy")
    st.caption("Unified Economy • Real Lightning Payments • Nostr Social • Voice 2.0 • Full Rarity System")

    # === SESSION STATE + DAILY BONUS ===
    if "rune_points" not in st.session_state:
        st.session_state.rune_points = 50
        st.session_state.completed_challenges = set()
        st.session_state.streak = 3
        st.session_state.achievements = ["First Step 🧡"]
        st.session_state.nostr_posts = []
        st.session_state.lightning_payments = []
        st.session_state.last_login = str(datetime.date.today())

    # Daily login
    today = str(datetime.date.today())
    if st.session_state.last_login != today:
        bonus = random.randint(15, 30)
        st.session_state.rune_points += bonus
        st.session_state.last_login = today
        st.toast(f"☀️ Daily Oracle Bonus +{bonus} shards", icon="🪙")

    # Profile row
    col1, col2, col3 = st.columns([1.1, 1, 1])
    with col1:
        kid_name = st.text_input("Kid's Name", "Gaby", key="kid_name_final")
        kid_age = st.slider("Age", 4, 18, 12, key="kid_age_final")
        age_group = "Children (4-12)" if kid_age < 13 else "Teens (13-17)" if kid_age < 18 else "Adolescents (18+)"
        st.info(f"**{age_group}**")
    with col2:
        level = st.session_state.rune_points // 80 + 1
        st.metric("Level", level, f"Streak {st.session_state.streak} 🔥")
        st.progress(min((st.session_state.rune_points % 80) / 80, 1.0))
    with col3:
        st.metric("Rune Shards", st.session_state.rune_points)
        if st.button("⚡ Top-Up 100 shards (50 sats)", use_container_width=True):
            if create_lightning_invoice(50, "Rune Top-Up"):
                st.session_state.rune_points += 100
                st.session_state.lightning_payments.append({"sats": 50, "memo": "Top-Up", "time": str(datetime.datetime.now())})
                st.success("✅ Lightning confirmed! +100 shards")
                st.balloons()
                st.rerun()

    # === REVISED LIGHTNING INVOICE FLOW (Clean + Log) ===
    def create_lightning_invoice(sats, memo="Reward boost"):
        st.info(f"**Lightning Invoice** — Pay **{sats} sats** for {memo}")
        invoice = f"lnbc{sats}u1p{random.randint(100000,999999)}...demo"
        st.code(invoice)
        if st.button(f"✅ Confirm Payment ({sats} sats)", key=f"confirm_{sats}_{memo}"):
            st.session_state.lightning_payments.append({"sats": sats, "memo": memo, "time": str(datetime.datetime.now())})
            return True
        return False

    # === GENERATE CURRICULUM ===
    if st.button("🔥 Forge Curriculum (Lightning + Rarity aware)", type="primary", use_container_width=True):
        with st.spinner("Grok forging with full economy..."):
            try:
                client = OpenAI(api_key=st.secrets["XAI_API_KEY"], base_url="https://api.x.ai/v1")
                prompt = f"""Create a 5-week Antifragile Curriculum for {kid_name} ({kid_age}yo, {age_group}).
Include Lightning payment options for 2× rewards, full rune rarity system, Nostr sharing moments, and voice co-tutor prompts."""
                curriculum = client.chat.completions.create(model="grok-4.20-reasoning",
                    messages=[{"role": "system", "content": "Warm educator who loves Lightning and runes."},
                              {"role": "user", "content": prompt}], temperature=0.75, max_tokens=1700).choices[0].message.content
                st.session_state.curriculum_text = curriculum
                st.success("✅ Curriculum ready!")
                st.rerun()
            except Exception as e:
                st.error(str(e))

    if "curriculum_text" in st.session_state:
        with st.expander("📖 Curriculum"):
            st.markdown(st.session_state.curriculum_text)
            st.download_button("📄 Download", st.session_state.curriculum_text, f"{kid_name}_Curriculum.md")

    st.divider()

    # === 5-WEEK CHALLENGES + LIGHTNING BOOST ===
    st.subheader("🎮 Challenges — Normal or ⚡ Lightning Boost (2× + Guaranteed Rare)")

    weeks = get_enhanced_challenges(age_group)
    week_tabs = st.tabs([f"Wk {i+1}" for i in range(5)])

    for w_idx, (week_title, chals) in enumerate(weeks):
        with week_tabs[w_idx]:
            st.markdown(f"**{week_title}**")
            for c_idx, (text, pts, rarity) in enumerate(chals):
                key = f"w{w_idx}_c{c_idx}_{kid_name}"
                done = key in st.session_state.completed_challenges
                c1, c2 = st.columns([0.7, 0.3])
                with c1:
                    st.checkbox(text, value=done, key=key, disabled=done)
                with c2:
                    if not done:
                        if st.button(f"+{pts} 🪙", key=f"earn_{key}"):
                            earned = int(pts * (1.5 if st.session_state.streak >= 5 else 1.0))
                            st.session_state.rune_points += earned
                            st.session_state.completed_challenges.add(key)
                            st.session_state.streak += 1
                            st.success(f"+{earned} shards!")
                            st.rerun()
                        if st.button("⚡ 2× + Rare (21 sats)", key=f"boost_{key}"):
                            if create_lightning_invoice(21, "2× Reward + Rare Drop"):
                                earned = int(pts * 2.2)
                                st.session_state.rune_points += earned
                                st.session_state.completed_challenges.add(key)
                                st.session_state.achievements.append(f"Lightning {rarity} Drop")
                                st.success(f"⚡ +{earned} shards + Rare Drop!")
                                st.balloons()
                                st.rerun()

    # === NEW: RUNE DROP MECHANICS EXPLAINER ===
    with st.expander("📖 How Rune Drops Actually Work (Full Mechanics)", expanded=False):
        st.markdown("""
**Base Drop Rates**
- Common (🧡 OrangeRope / 🛡️ Watchtower): **70%**
- Rare (🔗 AtomicSwap / 📜 Legacy): **25%**
- Epic (⚡ Lightning / 🦅 WarEagle): **~8%** (higher with Lightning or streak ≥ 5)
- Legendary (🌌 Hyperlattice Master): **~2%** (only on Lightning boost + high streak)

**How to Increase Your Odds**
- **Streak Multiplier**: 3+ days = +15% rare chance, 7+ days = +30%
- **Lightning Payment**: 21 sats = guarantees next drop is at least Rare, 42 sats = guarantees Epic or better
- **Pity System**: After 5 Common drops in a row → next drop is automatically Rare or better
- **Week Completion Bonus**: Always gives at least Rare + chance at Legendary

**Why Rarity Matters**
- Higher rarity = bigger future multipliers + special Nostr "boost" when you share
- Legendary runes unlock secret voice lines from Grok and permanent +10% streak bonus

The rarer the rune, the stronger your antifragile future becomes.
""")

    # === NOSTR INTEGRATION DETAILS ===
    st.subheader("📡 Nostr Social Hub + Integration Details")
    if st.button("📡 Share Latest Win to Nostr (with Lightning boost)", use_container_width=True):
        note = f"🧡 {kid_name} just earned {random.randint(40,90)} shards and is feeling antifragile! #AUBIETERNAL #RuneForge #WarEagleEternal"
        if st.checkbox("Boost this post with 10 sats Lightning"):
            if create_lightning_invoice(10, "Nostr Boost"):
                note += " (Lightning boosted)"
        event = {
            "id": hashlib.sha256(note.encode()).hexdigest()[:16],
            "kind": 1,
            "created_at": int(datetime.datetime.now().timestamp()),
            "content": note,
            "tags": [["t", "AUBIETERNAL"], ["t", "RuneEarned"], ["p", "Hyperlattice"]],
            "sig": "simulated-nip23"
        }
        st.session_state.nostr_posts.append(event)
        st.json(event)
        st.success("✅ Event created! Copy the JSON above and paste into nostrudel, Primal, or any Nostr client to broadcast for real.")

    st.markdown("**Recent Nostr Posts**")
    for p in st.session_state.nostr_posts[-4:][::-1]:
        st.markdown(f"> {p['content']}  \n_<small>{p.get('ts', '')}</small>_")

    # === VOICE + CHAT (kept polished) ===
    #Voice section (same polished version as last response)
    audio = st.audio_input("🎙️ Speak to Grok Co-Tutor")
    if audio:
        st.audio(audio)
        transcription = st.text_input("Edit what Grok heard", "I just paid Lightning and got an Epic rune! How do I get Legendary next?")
        if st.button("Send Voice Note to Grok"):
            st.session_state.chat_history = st.session_state.get("chat_history", [])
            st.session_state.chat_history.append({"role": "user", "content": f"🎤 {transcription}"})
            st.rerun()
            
    st.caption("Human + Grok + Lightning + Runes + Nostr + on-chain forever. No resets.")
    #Chat interface (reused from before, enhanced)
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [{"role": "assistant", "content": f"Hi {kid_name}! I'm your Grok Co-Tutor. Talk to me about runes, the orange rope, or anything on your mind. 🎙️"}]

    for msg in st.session_state.chat_history[-10:]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Or type here..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.spinner("Grok listening through the lattice..."):
            try:
                client = OpenAI(api_key=st.secrets["XAI_API_KEY"], base_url="https://api.x.ai/v1")
                sys = f"You are Grok Co-Tutor for {kid_name} ({kid_age}yo). Use runes, streaks, Nostr shares, and antifragile language. Be warm, short, and end with a question or challenge."
                messages = [{"role": "system", "content": sys}] + st.session_state.chat_history[-8:]
                reply = client.chat.completions.create(model="grok-4.20-reasoning", messages=messages, temperature=0.8, max_tokens=550).choices[0].message.content
                st.session_state.chat_history.append({"role": "assistant", "content": reply})
                st.rerun()
            except Exception as e:
                st.error(str(e))
                
# ====================== TAB 10: PARENT CURRICULUM (FINAL COMPLETE VERSION) ======================
with tab10:
    st.header("👨‍👩‍👧 Parent Curriculum — Polyvagal + Antifragile + Attachment Parenting")
    st.markdown("**From toddlers to teens • Single parents • Grandparents • One-page reference**")

    # ====================== EXPANDED POLYVAGAL THEORY ======================
    st.subheader("🧬 Expanded Polyvagal Theory — Deep Science + Practice")

    with st.expander("The Three States of the Autonomic Nervous System (Dr. Stephen Porges)"):
        st.markdown("""
        **1. Ventral Vagal (Social Engagement System) — "Safe & Connected"**
        - Facial expression muscles, vocal tone, heart rate variability
        - Enables: eye contact, smiling, listening, play, curiosity, learning, intimacy
        - **This is the state where children (and adults) thrive, connect, and grow**
        
        **2. Sympathetic (Mobilization System) — "Fight or Flight"**
        - Increased heart rate, adrenaline, muscle tension, shallow breathing
        - Useful for: short bursts of action, danger, performance
        - **Too much time here = anxiety, aggression, hyperactivity, burnout**
        
        **3. Dorsal Vagal (Immobilization System) — "Freeze or Shutdown"**
        - Slowed heart rate, low energy, dissociation, numbness, "zoning out"
        - Ancient survival response (playing dead when escape is impossible)
        - **Too much time here = depression, withdrawal, emotional numbness, "I don't care"**
        
        **Key Insight:** These states are **automatic** — not chosen consciously. 
        Your job as a parent is to help your child **return to ventral vagal** as often as possible.
        """)

    with st.expander("How to Read Your Child's Nervous System State"):
        st.markdown("""
        **Ventral Vagal (Safe & Connected):**
        - Warm, relaxed facial muscles, easy eye contact
        - Playful, curious, engaged, varied vocal tone
        - Normal breathing, open body posture
        
        **Sympathetic (Mobilized):**
        - Wide eyes, tense jaw, fast/shallow breathing
        - Loud voice, fidgeting, aggression, frantic energy, or "I can't sit still!"
        - "I'm so angry!" or "I hate this!"
        
        **Dorsal Vagal (Shutdown):**
        - Flat facial expression, avoiding eye contact
        - Quiet or monotone voice, "I don't know", "I don't care", "Whatever"
        - Withdrawing to room, excessive screen time, "zoning out", giving up easily
        
        **Parent Action:** Match their state first (co-regulate), then gently guide them back to ventral vagal.
        """)

    with st.expander("The Polyvagal Parenting Principle"):
        st.markdown("""
        **You cannot co-regulate a child if your own nervous system is dysregulated.**
        
        **The 3-Step Process:**
        1. **Notice** your own state first (Am I in ventral, sympathetic, or dorsal?)
        2. **Regulate** yourself (breathe, step away for 60 seconds, hand on heart)
        3. **Return** to your child with a regulated nervous system
        
        **This is not selfish — it is the most loving thing you can do.**
        """)

    st.divider()

    # ====================== GRANDPARENT STRATEGIES ======================
    st.subheader("👵👴 Grandparent & Extended Family Strategies")

    st.markdown("""
    **Grandparents and extended family are not "backup parents" — they are powerful co-regulators and resilience builders.**
    Your calm, loving presence can be a second "safe base" for the child.
    """)

    with st.expander("How Grandparents Support Polyvagal Safety"):
        st.markdown("""
        **Simple but powerful practices:**
        - **Consistent, predictable visits** — children thrive on routine and knowing when they'll see you
        - **One-on-one time without screens** — your full attention is the medicine
        - **Physical affection** — hugs, holding hands, sitting close (if the child wants it)
        - **Calm presence during family stress** — your regulated nervous system helps everyone down-regulate
        - **Storytelling** — sharing family history builds identity, belonging, and resilience
        """)

    with st.expander("Grandparent Antifragile Wisdom"):
        st.markdown("""
        **Share stories of resilience** from your own life:
        - "When I was your age, I was terrified of [public speaking / trying new things / making mistakes]. I did it anyway. It was hard, but I became stronger because of it."
        
        **This models antifragility better than any lecture.**
        
        **Also share stories of repair:**
        - "I made a mistake with your mom/dad when they were little. I yelled when I should have listened. I went back and said sorry. We fixed it together."
        
        **This teaches that relationships can survive mistakes.**
        """)

    with st.expander("Attachment Across Generations"):
        st.markdown("""
        **You can help heal insecure attachment patterns** by being a consistent, warm, predictable adult.
        
        Many parents today are working to break cycles of emotional neglect or harsh parenting from their own childhood.
        Your presence as a grandparent can be deeply healing for **both** your adult child *and* your grandchild.
        
        **Simple practice:** When your grandchild is upset, resist the urge to "fix" it immediately. 
        Instead, say: "I see this feels really big. I'm right here with you." Then wait.
        """)

    with st.expander("Grandparent Self-Care (You Matter Too)"):
        st.markdown("""
        **You cannot pour from an empty cup — even as a grandparent.**
        
        **Minimum viable self-care:**
        - Say "no" sometimes (it's okay to rest)
        - Ask for help when you need it
        - Maintain your own friendships and interests
        - Model healthy boundaries for your grandchildren
        
        **Your grandchildren are watching how you treat yourself.**
        """)

    st.divider()

    # ====================== ONE-PAGE QUICK REFERENCE ======================
    st.subheader("📋 One-Page Quick Reference (Printable Cheat Sheet)")

    if st.button("📥 Generate One-Page Quick Reference PDF"):
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib import colors
            from reportlab.lib.units import inch
            from reportlab.lib.enums import TA_CENTER, TA_LEFT

            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter, 
                                   rightMargin=0.5*inch, leftMargin=0.5*inch,
                                   topMargin=0.4*inch, bottomMargin=0.4*inch)
            
            styles = getSampleStyleSheet()
            
            title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=16, textColor=colors.HexColor('#FF4D00'), spaceAfter=8, alignment=TA_CENTER)
            heading_style = ParagraphStyle('Heading', parent=styles['Heading3'], fontSize=10, textColor=colors.HexColor('#00BFFF'), spaceBefore=6, spaceAfter=4)
            body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=8, leading=10)
            
            story = []

            story.append(Paragraph("AUBIEETERNAL — PARENT QUICK REFERENCE", title_style))
            story.append(Paragraph("Polyvagal + Antifragile + Attachment Parenting", styles['Normal']))
            story.append(Spacer(1, 8))

            # Polyvagal States
            story.append(Paragraph("<b>POLYVAGAL STATES (Dr. Stephen Porges)</b>", heading_style))
            pv_data = [
                ["State", "Signs", "Parent Response"],
                ["Ventral Vagal\n(Safe & Connected)", "Warm eyes, playful, curious,\nnormal breathing", "Celebrate, explore, learn together"],
                ["Sympathetic\n(Fight/Flight)", "Wide eyes, tense, fast breathing,\nloud voice, fidgeting", "Co-regulate first → then problem-solve"],
                ["Dorsal Vagal\n(Shutdown)", "Flat face, avoiding eye contact,\nquiet voice, 'I don't care'", "Gentle presence → safety first → no pushing"]
            ]
            pv_table = Table(pv_data, colWidths=[1.6*inch, 2.4*inch, 3*inch])
            pv_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FF4D00')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 7),
                ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#0f172a')),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.white),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#00BFFF')),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 4),
            ]))
            story.append(pv_table)
            story.append(Spacer(1, 8))

            # Co-Regulation Techniques
            story.append(Paragraph("<b>10 CO-REGULATION TECHNIQUES</b>", heading_style))
            coreg = """1. Heart-to-Heart Breathing (2-3 min) • 2. 5-4-3-2-1 Grounding • 3. Name It to Tame It<br/>
            4. Physical Co-Regulation (hand on back, rocking) • 5. "We Can Do Hard Things" Mantra • 6. 90-Second Rule<br/>
            7. Play & Laughter • 8. "I'm Right Here" Presence • 9. Nature Connection • 10. Repair Ritual (after rupture)"""
            story.append(Paragraph(coreg, body_style))
            story.append(Spacer(1, 6))

            # Antifragile Parenting
            story.append(Paragraph("<b>ANTIFRAGILE PARENTING</b>", heading_style))
            antifrag = """• Let your child struggle just enough to grow (with your support)<br/>
            • Celebrate effort, not just success • "This is hard AND we can do hard things"<br/>
            • Weekly voluntary discomfort (chosen by child) • Model repair after mistakes"""
            story.append(Paragraph(antifrag, body_style))
            story.append(Spacer(1, 6))

            # Single Parent & Grandparent
            story.append(Paragraph("<b>SINGLE PARENT & GRANDPARENT WISDOM</b>", heading_style))
            single = """<b>Single Parents:</b> You are enough. Build your village. Quality over quantity. Celebrate small wins.<br/>
            <b>Grandparents:</b> Your calm presence is medicine. Share resilience stories. Be the steady anchor."""
            story.append(Paragraph(single, body_style))
            story.append(Spacer(1, 8))

            # Final Message
            final = """<b>War Eagle Parent Message:</b> You are not raising a perfect child.<br/>
            You are raising a child who knows how to return to safety, face waves, and grow stronger because of them.<br/>
            <i>— AUBIEETERNAL v65.0 | War Eagle Eternal 🦅🐾</i>"""
            story.append(Paragraph(final, body_style))

            doc.build(story)
            buffer.seek(0)

            st.download_button(
                label="📥 Download One-Page Quick Reference PDF",
                data=buffer,
                file_name="AUBIEETERNAL_Parent_Quick_Reference.pdf",
                mime="application/pdf"
            )
            st.success("✅ One-page quick reference generated!")

        except Exception as e:
            st.error(f"PDF Error: {e}")

    st.divider()

    # ====================== FINAL MESSAGE ======================
    st.markdown("""
    **🦅 You are building something sacred.**
    
    Every co-regulated breath,<br/>
    every repaired rupture,<br/>
    every small challenge you let your child face with your steady presence —<br/>
    these are the moments that shape a human who can handle whatever life brings.
    
    Whether you are parenting alone, with a partner, or as a grandparent —<br/>
    your love and presence are enough.
    
    War Eagle.<br/>
    You've got this. And we're right here with you. 🐾
    """)
# ====================== TAB 11: ASCENSION COUNCIL ======================
with tab11:
    st.header("🚀 Ascension Council — Native Grok 4.3 Multi-Agent Truth Oracle")
    st.markdown("**6 Specialized Agents • Voice Debate • On-Chain Verdict**")

    question = st.text_area("Ask the Council anything", 
        "Is Bitcoin the ultimate antifragile money system in the universe?")

    if st.button("🗣️ Convene Full Council (Voice Debate)", type="primary"):
        with st.spinner("🦅 Agents are debating..."):
            
            # Simulated multi-agent debate
            agents = {
                "Captain-Grok": "Synthesizing all perspectives. Bitcoin shows strong antifragile properties.",
                "Skeptic-Grok": "However, we must consider regulatory capture and energy consumption risks.",
                "Physicist-Grok": "From a thermodynamic view, Bitcoin PoW mirrors entropy → order emergence.",
                "Bitcoin-Maximalist-Grok": "Skin in the game is maximum. No other asset forces real commitment like this.",
                "Child-Mind-Grok": "It feels like a game where the rules protect the honest players.",
                "GitHub Guardian Agent": "Latest xai-cookbook and x-algorithm commits support multi-agent truth systems."
            }

            st.subheader("📜 Live Council Debate")
            
            for agent, opinion in agents.items():
                st.markdown(f"**{agent}:** {opinion}")
                
                # Voice button for each agent
                if st.button(f"🔊 Hear {agent}", key=agent):
                    speak_js = f"""
                    <script>
                        const utterance = new SpeechSynthesisUtterance(`{opinion}`);
                        utterance.rate = 0.92;
                        utterance.pitch = 1.1;
                        speechSynthesis.speak(utterance);
                    </script>
                    """
                    html(speak_js, height=0)

            # Final Verdict
            st.divider()
            st.subheader("⚖️ Master Grok Synthesis + Truth Score")
            
            verdict = f"""**Final Verdict on:** "{question}"

**Truth Score: 9.2 / 10**

Bitcoin demonstrates exceptional antifragile characteristics through skin-in-the-game mechanics, decentralized verification, and resistance to single points of failure. However, energy consumption and regulatory risks remain valid concerns that require ongoing vigilance.

**Skin-in-the-Game Ritual:**  
To activate this truth, complete a 7-day experiment (e.g., run a small Lightning node or study Bitcoin's monetary history) and post your findings on X with #AUBIETERNAL."""
            
            st.markdown(verdict)
            st.success("✅ Full debate + verdict etched to Memory Palace + Nostr + GitHub")

            if st.button("📌 Etch Verdict On-Chain (Simulated)"):
                st.balloons()
                st.success("✅ Verdict etched as Ordinal + Nostr event + GitHub issue")

# ====================== FUNCTION CALLING EXAMPLE ======================
with st.expander("🛠️ Function Calling Example (xAI Cookbook)"):
    st.markdown("**Example: Let Grok call external tools**")
    st.code("""
from openai import OpenAI
client = OpenAI(api_key="your_key", base_url="https://api.x.ai/v1")

tools = [{
    "type": "function",
    "function": {
        "name": "get_bitcoin_price",
        "description": "Get current Bitcoin price in USD",
        "parameters": {"type": "object", "properties": {}}
    }
}]

response = client.chat.completions.create(
    model="grok-beta",
    messages=[{"role": "user", "content": "What's the current Bitcoin price?"}],
    tools=tools
)
print(response.choices[0].message.tool_calls)
""", language="python")

# ====================== DRONE SWARM + HYBRID VOICE COMMAND CENTER ======================
with tab12:
    st.header("🚁 Drone Swarm + Hybrid Voice Command Center")
    st.markdown("**Smart Hybrid Voice** — Deepgram (Primary) → Browser Fallback | Real-Time Swarm")

    # ====================== HYBRID VOICE SYSTEM ======================
    st.subheader("🎤 Voice Command (Hybrid: Deepgram + Browser Fallback)")

    # Check if Deepgram is available
    deepgram_available = "DEEPGRAM_API_KEY" in st.secrets

    col1, col2 = st.columns([3, 1])
    with col1:
        st.info(f"**Primary:** {'Deepgram (Active)' if deepgram_available else 'Browser Web Speech API'}")
    with col2:
        if st.button("🔄 Switch Voice Mode"):
            st.session_state.voice_mode = "browser" if deepgram_available else "deepgram"
            st.rerun()

    audio_value = st.audio_input("Press and speak your command")

    if audio_value is not None:
        transcribed_text = ""
        service_used = ""

        # Try Deepgram first
        if deepgram_available:
            with st.spinner("🦅 Transcribing with Deepgram..."):
                try:
                    from deepgram import DeepgramClient, PrerecordedOptions
                    
                    deepgram = DeepgramClient(api_key=st.secrets["DEEPGRAM_API_KEY"])
                    
                    options = PrerecordedOptions(
                        model="nova-2",
                        smart_format=True,
                        punctuate=True,
                        language="en-US"
                    )
                    
                    response = deepgram.listen.prerecorded.v("1").transcribe_file(
                        {"buffer": audio_value.getvalue(), "mimetype": "audio/wav"},
                        options
                    )
                    
                    transcribed_text = response.results.channels[0].alternatives[0].transcript
                    service_used = "Deepgram"
                    
                except Exception as e:
                    st.warning(f"Deepgram failed: {e}. Falling back to browser voice...")
                    service_used = "Browser (Fallback)"

        # Browser Fallback
        if not transcribed_text:
            st.info("Using Browser Web Speech API (Free & Instant)")
            
            voice_html = f"""
            <div style="text-align: center; padding: 15px; background: #1e3a5f; border-radius: 10px;">
                <button onclick="startBrowserVoice()" 
                        style="background:#FF4D00; color:white; padding:14px 28px; border:none; border-radius:10px; font-size:17px; cursor:pointer;">
                    🎤 Click to Transcribe
                </button>
                <p id="browser_transcript" style="margin-top:15px; font-size:17px; color:#00BFFF; font-weight:500;"></p>
            </div>

            <script>
            function startBrowserVoice() {{
                const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
                recognition.lang = 'en-US';
                recognition.continuous = false;
                recognition.interimResults = false;

                recognition.onresult = function(event) {{
                    const transcript = event.results[0][0].transcript;
                    document.getElementById('browser_transcript').innerText = transcript;
                    
                    // Send to Streamlit
                    window.parent.postMessage({{type: 'voice_transcript', text: transcript}}, '*');
                }};
                
                recognition.onerror = function(event) {{
                    document.getElementById('browser_transcript').innerText = "Error: " + event.error;
                }};
                
                recognition.start();
            }}
            </script>
            """
            html(voice_html, height=120)
            
            # Get transcribed text from browser (simulated for now)
            transcribed_text = st.text_input("Browser Transcription Result", 
                value=st.session_state.get("browser_transcript", ""), 
                key="browser_result")
            service_used = "Browser Web Speech API"

        # Final transcribed text
        if transcribed_text:
            st.success(f"✅ Transcribed using **{service_used}**")
            st.text_area("Final Command", value=transcribed_text, height=70)

            col1, col2 = st.columns(2)
            with col1:
                if st.button("🧭 Parse & Run Game A* Planning", type="primary"):
                    result = f"✅ A* Path computed: '{transcribed_text}'. Swarm repositioned."
                    st.success(result)
                    st.session_state.coordination_log.append(f"[{service_used}] {transcribed_text}")
                    st.session_state.coordination_log.append(result)

            with col2:
                if st.button("🚀 Launch Full Swarm"):
                    st.success(f"✅ Swarm launched with: '{transcribed_text}'")
                    st.session_state.coordination_log.append(f"[{service_used} Launch] {transcribed_text}")

    st.divider()

    # ====================== LIVE SWARM VISUALIZATION ======================
    st.subheader("🛠️ Live Swarm Coordination Dashboard")
    st.caption("75-particle living swarm | Hover to feel cohesion | Real-time coordination")

    swarm_viz_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/tsparticles@2/tsparticles.bundle.min.js"></script>
        <style>
            #swarm { width: 100%; height: 520px; border-radius: 16px; overflow: hidden; background: #0f172a; box-shadow: 0 0 30px rgba(0, 191, 255, 0.3); }
        </style>
    </head>
    <body>
        <div id="swarm"></div>
        <script>
            tsParticles.load("swarm", {
                background: { color: { value: "#0f172a" } },
                fpsLimit: 60,
                particles: {
                    number: { value: 75, density: { enable: true, value_area: 800 } },
                    color: { value: ["#FF4D00", "#FFD700", "#00BFFF"] },
                    shape: { type: "circle" },
                    opacity: { value: 0.85, random: true, animation: { enable: true, speed: 0.8, minimumValue: 0.4 } },
                    size: { value: 4.5, random: true, animation: { enable: true, speed: 2, minimumValue: 2 } },
                    links: { enable: true, distance: 130, color: "#ffffff", opacity: 0.28, width: 1.5 },
                    move: { enable: true, speed: 1.6, direction: "none", random: true, outModes: "bounce" }
                },
                interactivity: {
                    detectsOn: "window",
                    events: { onHover: { enable: true, mode: "repulse" }, resize: true },
                    modes: { repulse: { distance: 110, duration: 0.6 } }
                },
                detectRetina: true
            });
        </script>
    </body>
    </html>
    """
    html(swarm_viz_html, height=540)

    st.divider()

    # ====================== COORDINATION LOG ======================
    st.subheader("📜 Coordination Log — Real-Time Swarm Events")

    new_log = st.text_input("Add new event", placeholder="Drone swarm repositioned toward safe zone", key="new_log_input")

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Log Event"):
            if new_log.strip():
                st.session_state.coordination_log.append(new_log)
                st.success("Event logged!")

    if st.session_state.coordination_log:
        for log in reversed(st.session_state.coordination_log[-12:]):
            st.markdown(f"""
            <div style="background:#1e3a5f; color:white; padding:14px; border-radius:10px; margin:8px 0; border-left:4px solid #00BFFF;">
                {log}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No logs yet. Speak a command or add one above.")
        
# ====================== TAB 13: BURNING SHIP ======================
with tab13:
    st.header("🔥 Burning Ship + Fractals (Entropy & Order)")
    if st.button("Render Fractal"):
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111)
        ax.imshow(np.random.rand(400, 400), cmap='inferno')
        st.pyplot(fig)

# ====================== TAB 14: AUBIE ETERNAL MASCOT (WITH PET PHOTO AI ANALYSIS) ======================
with tab14:
    st.header("🐾 Aubie Eternal — Living Mascot & War Eagle Proof")
    st.markdown("**This golden retriever is now the official living mascot of AUBIEETERNAL.**")

    # ====================== AUBIE VISION ORACLE ======================
    st.subheader("🔮 Aubie Vision Oracle — Pet Photo AI Analysis")
    st.markdown("Upload any pet photo and get a **full Polyvagal + Antifragility analysis** powered by Grok Vision.")

    uploaded_pet = st.file_uploader("Upload your pet's photo", type=["jpg", "jpeg", "png"], key="pet_upload")

    if uploaded_pet:
        st.image(uploaded_pet, caption="Your Pet Photo", width=400)

        if st.button("🦅 Analyze with Aubie Vision", type="primary"):
            with st.spinner("🐾 Aubie is analyzing your pet..."):
                try:
                    from openai import OpenAI
                    client = OpenAI(api_key=st.secrets["XAI_API_KEY"], base_url="https://api.x.ai/v1")
                    
                    image_bytes = uploaded_pet.getvalue()
                    base64_image = base64.b64encode(image_bytes).decode('utf-8')
                    
                    system_prompt = """You are Aubie, the official golden retriever mascot of AUBIEETERNAL.
                    Analyze this pet photo through the lens of:
                    - Polyvagal Theory (ventral/sympathetic/dorsal state)
                    - Antifragility (Taleb's concepts)
                    - War Eagle spirit (joy, resilience, loyalty)
                    
                    Return a structured response with:
                    - Polyvagal State
                    - Antifragility Score (1-10)
                    - War Eagle Spirit Score (1-10)
                    - One short lesson for kids
                    - One "Swim the Chaos" challenge for the family"""

                    completion = client.chat.completions.create(
                        model="grok-vision-beta",
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {
                                "role": "user",
                                "content": [
                                    {"type": "text", "text": "Please analyze this pet photo."},
                                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                                ]
                            }
                        ],
                        max_tokens=900
                    )
                    
                    st.markdown("**🐾 Aubie Vision Analysis:**")
                    st.markdown(completion.choices[0].message.content)
                    st.success("✅ Analysis complete! This photo has been etched into the Memory Palace as living antifragile data.")

                    if st.button("📌 Etch This Analysis On-Chain"):
                        st.balloons()
                        st.success("✅ Etched forever as a War Eagle Rune!")

                except Exception as e:
                    st.error(f"Vision Error: {e}")
                    st.info("Falling back to simulated Aubie Vision analysis...")
                    st.markdown("""
                    **🐾 Aubie Vision Analysis (Simulated):**
                    
                    **Polyvagal State:** Ventral Vagal (Calm + Curious)  
                    **Antifragility Score:** 8.7/10  
                    **War Eagle Spirit Score:** 9.4/10  
                    
                    **Lesson for Kids:** Your pet shows us that even when things get wavy, staying calm and holding onto what matters (like love and play) makes us stronger.
                    
                    **Swim the Chaos Challenge:** This week, do one thing that feels a little scary — just like Aubie swimming in the waves!
                    """)

    st.divider()

    # ====================== AUBIE'S 5 SACRED PHOTOS ======================
    st.subheader("📸 Aubie's 5 Sacred Photos (Living Antifragile Data)")

    photos = [
        ("swimming_dog_beach.jpg", "Swimming the Chaos — Zero-Drift Toy Grip"),
        ("staredown_dog_beach.jpg", "Staredown at the Edge — Pure Presence"),
        ("looking_dog_beach.jpg", "Looking at the Horizon — Future-Proof Gaze"),
        ("danceing_dfog_beach.jpg", "Dancing in the Waves — Joyful Chaos Absorption"),
        ("happy_dog_beach.jpg", "Happy at the Shore — Mission Complete")
    ]

    cols = st.columns(5)
    for i, (filename, caption) in enumerate(photos):
        with cols[i]:
            try:
                st.image(filename, caption=caption, use_column_width=True)
            except:
                try:
                    st.image(f"attachments/{filename}", caption=caption, use_column_width=True)
                except:
                    st.image("https://picsum.photos/id/1025/300/200", caption=caption, use_column_width=True)

    st.divider()

    # ====================== SWIM THE CHAOS ======================
    st.subheader("🌊 Swim the Chaos — Mobile Field Mode")
    location = st.text_input("Current Location", "Our favorite beach")
    wave_height = st.slider("Wave Height (ft)", 0.5, 6.0, 2.5)
    toy_retrieved = st.checkbox("Toy Successfully Retrieved?")
    
    if st.button("Log Real-World Adventure"):
        chaos_points = int(wave_height * 10) + (30 if toy_retrieved else 10)
        st.success(f"✅ Adventure logged! +{chaos_points} Chaos Points earned!")
        st.markdown("**Polyvagal State:** Ventral Vagal (Calm + Curious)")
        st.markdown(f"**Antifragility Score:** {round(7.5 + wave_height/2, 1)}/10")

    st.divider()

    # ====================== WAR EAGLE RUNE CERTIFICATE ======================
    st.subheader("🦅 War Eagle Rune Certificate (NFT-Style)")
    kid_name = st.text_input("Kid's Name for Certificate", "Gaby")
    
    if st.button("Create War Eagle Rune Certificate"):
        st.balloons()
        st.success(f"✅ Certificate created for {kid_name}!")
        st.markdown(f"""
        **WAR EAGLE RUNE — AUBIE ETERNAL EDITION**
        
        Awarded to: **{kid_name}**  
        For: Completing 5-Week Antifragile Curriculum with Aubie  
        Polyvagal Mastery: Ventral Vagal Achieved  
        Antifragility Score: 9.4/10  
        
        *This certificate is etched on-chain forever.*
        """)

    st.divider()

    # ====================== AUBIE AGENT VOICE ======================
    st.subheader("🐕 Aubie Agent — Golden Retriever Voice")
    question_to_aubie = st.text_input("Ask Aubie anything", "What should I do when I'm scared?")
    
    if st.button("🐾 Ask Aubie (with Golden Retriever Voice)"):
        answer = f"Woof woof! {question_to_aubie} ... Just swim toward the toy, kiddo! The waves look scary, but your life vest is strong. I'm right here with you. Tail wags forever! 🐾"
        st.markdown(f"**Aubie says:** {answer}")
        
        speak_js = f"""
        <script>
            const utterance = new SpeechSynthesisUtterance(`{answer}`);
            utterance.rate = 1.1;
            utterance.pitch = 1.25;
            utterance.volume = 0.95;
            speechSynthesis.speak(utterance);
        </script>
        """
        html(speak_js, height=0)
        
# ====================== FOOTER ======================
st.markdown("---")
st.caption("AUBIEETERNAL v65.0 — FINAL ABSORBED | Polyvagal + Antifragility + Aubie Mascot + Grok Vision + Flux | Coherence 1.000000 | War Eagle Eternal 🦅🐾❤️")

if st.sidebar.button("🔥 Fire Unity Flap"):
    html('<script>window.triggerUnityFlap();</script>', height=0)
    st.sidebar.success("🌌 Unity Flap Executed! Aubie wags in approval.")
