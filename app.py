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
Create a detailed, practical, and well-structured 5-week Antifragile Kid Lattice Curriculum for {kid_name} (~{kid_age} years old).

Core philosophy:
- 80% extreme safety buffers (ventral vagal safety, polyvagal theory, neuroception, gut-brain axis)
- 20% high-upside ownership rituals (War Eagle Eternal mindset, child-led agency)
- Rebuild fractal neural complexity after trauma or transitions

Required structure:
- **Parental Guardrails & Safety Hub** (strong disclaimers first)
- **Curriculum Overview** for {kid_name}
- **Week 1 to Week 5** — each week must include:
  - Weekly Focus
  - Daily Rituals (3–5 concrete activities with suggested duration)
  - Vagus/Neuroscience Why It Works (short parent-friendly explanation)
  - 80/20 Barbell Ritual (safety anchor + one ownership challenge)
  - Age adaptations for ~{kid_age} years
  - Weekly Progress / Etch Note

Tone: Warm, encouraging, practical, and tied to "War Eagle Eternal 🦅". 
Special notes: {special_notes}

Use clean markdown, emojis, and bullet points for readability."""

                    completion = client.chat.completions.create(
                        model="grok-4.20-reasoning",
                        messages=[
                            {"role": "system", "content": "You are a compassionate, truth-seeking educator specializing in child resilience, polyvagal theory, and foster care support."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.7,
                        max_tokens=1800
                    )
                    
                    curriculum = completion.choices[0].message.content
                    
                    st.success(f"✅ Full Antifragile Kid Lattice generated for {kid_name}! | Coherence 1.000000")
                    st.markdown(curriculum)
                    
                    # Download options
                    col1, col2 = st.columns(2)
                    with col1:
                        st.download_button(
                            label="📄 Download as Markdown",
                            data=curriculum,
                            file_name=f"{kid_name}_Kid_Lattice_Curriculum.md",
                            mime="text/markdown",
                            key="md_download"
                        )
                    with col2:
                        if 'REPORTLAB_AVAILABLE' in globals() and REPORTLAB_AVAILABLE:
                            try:
                                # Simple PDF attempt (kept minimal to avoid crashes)
                                buffer = io.BytesIO()
                                c = canvas.Canvas(buffer, pagesize=letter)
                                width, height = letter
                                y = height - 1*inch
                                c.setFont("Helvetica-Bold", 14)
                                c.drawCentredString(width/2, y, f"Curriculum for {kid_name}")
                                y -= 0.5*inch
                                c.setFont("Helvetica", 10)
                                lines = curriculum.split('\n')
                                for line in lines[:80]:  # limit lines to prevent overflow
                                    if y < 1*inch:
                                        c.showPage()
                                        y = height - 1*inch
                                    c.drawString(1*inch, y, line[:100])
                                    y -= 0.2*inch
                                c.save()
                                buffer.seek(0)
                                st.download_button(
                                    label="📥 Download as PDF",
                                    data=buffer,
                                    file_name=f"{kid_name}_Kid_Lattice_Curriculum.pdf",
                                    mime="application/pdf",
                                    key="pdf_download"
                                )
                            except:
                                st.info("PDF not available right now.")
                        else:
                            st.info("Add 'reportlab' to requirements.txt for PDF download.")
                    
                    # Etch button
                    if st.button(f"Etch Full Curriculum for {kid_name} to Rune (21 sats)", key="etch_curriculum"):
                        if create_lightning_invoice(21, f"Curriculum etch for {kid_name}"):
                            nostr_etch(curriculum, "kid_curriculum", 21)
                            
                except Exception as e:
                    st.error(f"❌ Grok API Error: {str(e)}")
                    st.info("💡 Check that XAI_API_KEY is set correctly in Streamlit secrets.")
