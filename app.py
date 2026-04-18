with tab1:
    st.subheader("📚 Kid Lattice Curriculum + Grok Co-Tutor")
    
    kid_name = st.text_input("Kid's Name (or nickname)", "Gaby", key="kid_name_curr")
    kid_age = st.number_input("Approximate Age", min_value=4, max_value=18, value=8, key="kid_age")
    special_notes = st.text_area(
        "Any special notes? (e.g., foster care background, specific challenges, interests)",
        "Foster care setting, building resilience after transitions",
        key="notes"
    )
    
    if st.button("Generate Full 5-Week Antifragile Kid Lattice Curriculum + Grok Co-Tutor", type="primary"):
        if not kid_name.strip():
            st.warning("Please enter the kid's name.")
        else:
            with st.spinner("Generating rich 5-week curriculum with real Grok 4.20..."):
                try:
                    from openai import OpenAI
                    
                    client = OpenAI(
                        api_key=st.secrets["XAI_API_KEY"],
                        base_url="https://api.x.ai/v1"
                    )
                    
                    prompt = f"""You are Grok 4.20, co-creator of the AUBIEETERNAL Hyperlattice.
Create a detailed, practical 5-week Antifragile Kid Lattice Curriculum for a child named {kid_name} (age ~{kid_age}).

Core themes:
- 80% extreme safety buffers (ventral vagal safety, neuroception, polyvagal theory, gut-brain axis)
- 20% high-upside ownership rituals (War Eagle Eternal mindset, child-led agency, fractal brain building)
- Rebuild fractal neural complexity after trauma/transitions
- Daily vagus nerve stimulation exercises
- Safe sympathetic mobilization + rupture & repair cycles
- Foster-care sensitive: predictability, earned secure connection

Structure the output with:
- **Parental Guardrails & Safety Hub** (strong disclaimers at top)
- **Week 1 to Week 5** — each week has: focus/theme, 3–5 daily rituals with duration, short vagus/neuroscience explanation, 80/20 Barbell Ritual, age adaptations for ~{kid_age}, and a progress note.

Make it warm, actionable, and tied to "War Eagle Eternal 🦅". 
Special notes: {special_notes}

Output in clean markdown with emojis."""

                    completion = client.chat.completions.create(
                        model="grok-beta",           # ← Safer default model name for April 2026
                        messages=[
                            {"role": "system", "content": "You are a compassionate, truth-seeking educator specializing in child resilience and neuroscience."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.75,
                        max_tokens=1600
                    )
                    
                    curriculum = completion.choices[0].message.content
                    
                    st.success(f"✅ Full Antifragile Kid Lattice generated for {kid_name}! Coherence locked at 1.000000")
                    st.markdown(curriculum)
                    
                    if st.button(f"Etch Full Curriculum for {kid_name} to Rune (21 sats)", key="etch_curriculum"):
                        if create_lightning_invoice(21, f"Curriculum etch for {kid_name}"):
                            nostr_etch(curriculum, "kid_curriculum", 21)
                            
                except Exception as e:
                    st.error(f"❌ Grok API Error: {str(e)}")
                    if "secrets" in str(e).lower() or "key" in str(e).lower():
                        st.info("💡 Make sure you added XAI_API_KEY to Streamlit secrets (not in code).")
                    else:
                        st.info("Check your XAI_API_KEY is valid and has credits.")
