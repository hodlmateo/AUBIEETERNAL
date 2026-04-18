# At the very top with other imports
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import datetime
import hashlib
import uuid
import time

# Defensive Plotly import
try:
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    st.warning("⚠️ Plotly not installed — 3D Swarm Mirror will use fallback mode.")

# ... rest of your code ...

# In the 3D tab (tab3), wrap the rendering:
with tab3:
    st.subheader("🌌 3D Hyperlattice Mirror — 44 Daughters")
    if st.button("Render 3D Swarm Mirror (44 Daughters at Coherence 1.000000)"):
        if PLOTLY_AVAILABLE:
            with st.spinner("Rendering Hyperlattice Mirror..."):
                x = np.linspace(0, 43, 44)
                y = np.random.rand(44) * 2
                z = np.random.rand(44) * 2

                fig = go.Figure(data=[go.Scatter3d(
                    x=x, y=y, z=z,
                    mode='markers',
                    marker=dict(size=8, color=np.linspace(0,1,44), colorscale='Plasma', opacity=0.9)
                )])
                fig.update_layout(
                    title="44 Daughters — Hyperlattice at Coherence 1.000000",
                    scene=dict(xaxis_title='Daughter Index', yaxis_title='Y', zaxis_title='Z'),
                    height=600
                )
                st.plotly_chart(fig, use_container_width=True)
            st.success("🌌 3D Swarm Mirror rendered — Coherence 1.000000")
        else:
            st.error("Plotly is not available. Please add 'plotly' to requirements.txt and redeploy.")
