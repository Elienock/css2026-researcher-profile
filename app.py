import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from datetime import datetime

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Elienock Lubaya Mulumba | Researcher Profile",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    .main .block-container {
        padding-top: 2rem;
        max-width: 1100px;
    }

    .hero-section {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        padding: 2.5rem 2rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
    }

    .hero-name {
        font-family: 'Inter', sans-serif;
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
        color: #ffffff;
    }

    .hero-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        font-weight: 300;
        color: #b0d4e8;
        margin-bottom: 1rem;
    }

    .hero-bio {
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem;
        line-height: 1.7;
        color: #d0e4f0;
        max-width: 800px;
    }

    .metric-card {
        background: #ffffff;
        border: 1px solid #e8edf2;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        transition: transform 0.2s ease;
    }

    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    }

    .metric-value {
        font-family: 'Inter', sans-serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: #203a43;
    }

    .metric-label {
        font-family: 'Inter', sans-serif;
        font-size: 0.8rem;
        font-weight: 500;
        color: #6b7c8a;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .section-header {
        font-family: 'Inter', sans-serif;
        font-size: 1.4rem;
        font-weight: 600;
        color: #1a2f3a;
        border-bottom: 3px solid #2c5364;
        padding-bottom: 0.5rem;
        margin: 2rem 0 1rem 0;
    }

    .project-card {
        background: linear-gradient(to right, #f8fbfd, #ffffff);
        border-left: 4px solid #2c5364;
        padding: 1.2rem 1.5rem;
        border-radius: 0 12px 12px 0;
        margin-bottom: 1rem;
        box-shadow: 0 1px 6px rgba(0,0,0,0.04);
    }

    .project-title {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1.05rem;
        color: #1a2f3a;
        margin-bottom: 0.3rem;
    }

    .project-desc {
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
        color: #4a5c6a;
        line-height: 1.6;
    }

    .skill-tag {
        display: inline-block;
        background: #e8f4f8;
        color: #2c5364;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        margin: 0.2rem;
        font-family: 'Inter', sans-serif;
    }

    .timeline-item {
        border-left: 2px solid #2c5364;
        padding-left: 1.5rem;
        padding-bottom: 1.5rem;
        position: relative;
    }

    .timeline-item::before {
        content: '';
        position: absolute;
        left: -6px;
        top: 4px;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #2c5364;
    }

    .timeline-year {
        font-family: 'Inter', sans-serif;
        font-size: 0.75rem;
        font-weight: 600;
        color: #2c5364;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .timeline-title {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        color: #1a2f3a;
        font-size: 0.95rem;
    }

    .timeline-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 0.85rem;
        color: #6b7c8a;
    }

    .contact-badge {
        display: inline-block;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.2);
        padding: 0.3rem 0.9rem;
        border-radius: 20px;
        color: #b0d4e8;
        font-size: 0.85rem;
        margin: 0.2rem;
        font-family: 'Inter', sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### Navigation")
    page = st.radio(
        "Go to",
        ["Home", "Research & Projects", "Skills & Tools", "Achievements & Impact", "Contact"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("##### Quick Links")
    st.markdown("[GitHub](https://github.com/Elienock) · [LinkedIn](https://linkedin.com/)")
    st.markdown("---")
    st.caption(f"Last updated: {datetime.now().strftime('%B %Y')}")


# ══════════════════════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════════════════════
if page == "Home":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-name">Elienock Lubaya Mulumba</div>
        <div class="hero-title">Software Engineer · Research Fellow (CHPC 2026) · ML Practitioner</div>
        <div class="hero-bio">
            A versatile Software Engineer with over 4 years of industry experience and a newly
            completed Advanced Diploma in Computer Science. I specialize in bridging the gap between
            high-level architectural design and low-level computational efficiency. My work focuses
            on building scalable digital ecosystems and applying Machine Learning to solve real-world
            logistical and social challenges.
        </div>
        <div style="margin-top:1rem;">
            <span class="contact-badge">📍 Pretoria, South Africa</span>
            <span class="contact-badge">🎓 Tshwane University of Technology</span>
            <span class="contact-badge">🏢 Founder, Albo Tech SARL & Claudine Tech</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><div class="metric-value">4+</div><div class="metric-label">Years Experience</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><div class="metric-value">2</div><div class="metric-label">Tech Companies Founded</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><div class="metric-value">5+</div><div class="metric-label">Certifications</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><div class="metric-value">2</div><div class="metric-label">Countries (SA & DRC)</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-year">2026</div>
        <div class="timeline-title">CHPC Coding Summer School — Research Fellow</div>
        <div class="timeline-subtitle">University of Pretoria · High-Performance Computing</div>
    </div>
    <div class="timeline-item">
        <div class="timeline-year">Completed</div>
        <div class="timeline-title">Advanced Diploma in Computer Science</div>
        <div class="timeline-subtitle">Tshwane University of Technology (TUT)</div>
        <div class="timeline-subtitle" style="margin-top:0.3rem; color:#4a5c6a;">
            Specialization: <em>Full-Stack Systems, Machine Learning & Predictive Modeling</em>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">Certifications</div>', unsafe_allow_html=True)

    certs = [
        "Machine Learning (SETA)", "Cisco Cybersecurity", "CHPC 2026 Research Fellow",
        "Full-Stack Development", "Data Science & Predictive Modeling"
    ]
    tags_html = " ".join([f'<span class="skill-tag">{c}</span>' for c in certs])
    st.markdown(tags_html, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# RESEARCH & PROJECTS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Research & Projects":
    st.markdown('<div class="section-header">Flagship Project — The Kneel</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
        <div class="project-title">The Kneel: Sophisticated Digital Ecosystem Platform</div>
        <div class="project-desc">
            Currently architecting <strong>The Kneel</strong>, a sophisticated digital ecosystem
            designed for specialized community connectivity and service management. The platform
            implements secure, invite-only authentication protocols, complex database relations,
            and high-performance backend logic to deliver a seamless, scalable user experience.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("##### System Architecture")

    fig_arch = go.Figure()

    boxes = [
        {"x": 0.5, "y": 0.9, "text": "User Layer\n(Invite-Only Auth)", "color": "#0f2027"},
        {"x": 0.5, "y": 0.72, "text": "API Gateway\n& Security (SOS Protocols)", "color": "#203a43"},
        {"x": 0.15, "y": 0.5, "text": "Java Backend\n(Multi-threaded)", "color": "#2c5364"},
        {"x": 0.5, "y": 0.5, "text": "PHP Services\n(API Integration)", "color": "#2c5364"},
        {"x": 0.85, "y": 0.5, "text": "ML Pipeline\n(Predictive Models)", "color": "#2c5364"},
        {"x": 0.5, "y": 0.28, "text": "Complex Database\nRelations & Analytics", "color": "#203a43"},
        {"x": 0.5, "y": 0.1, "text": "Dashboard &\nBusiness Intelligence", "color": "#0f2027"},
    ]

    for b in boxes:
        fig_arch.add_shape(
            type="rect",
            x0=b["x"] - 0.13, y0=b["y"] - 0.06,
            x1=b["x"] + 0.13, y1=b["y"] + 0.06,
            fillcolor=b["color"], line=dict(width=0),
            layer="below",
        )
        fig_arch.add_annotation(
            x=b["x"], y=b["y"], text=b["text"],
            showarrow=False, font=dict(color="white", size=11),
        )

    arrows = [
        (0.5, 0.84, 0.5, 0.78),
        (0.5, 0.66, 0.15, 0.56),
        (0.5, 0.66, 0.5, 0.56),
        (0.5, 0.66, 0.85, 0.56),
        (0.15, 0.44, 0.5, 0.34),
        (0.5, 0.44, 0.5, 0.34),
        (0.85, 0.44, 0.5, 0.34),
        (0.5, 0.22, 0.5, 0.16),
    ]
    for ax, ay, bx, by in arrows:
        fig_arch.add_annotation(
            x=bx, y=by, ax=ax, ay=ay,
            xref="x", yref="y", axref="x", ayref="y",
            showarrow=True, arrowhead=2, arrowsize=1.2,
            arrowwidth=1.5, arrowcolor="#6b7c8a",
        )

    fig_arch.update_layout(
        xaxis=dict(range=[0, 1], showgrid=False, zeroline=False, visible=False),
        yaxis=dict(range=[0, 1], showgrid=False, zeroline=False, visible=False),
        height=480, margin=dict(l=20, r=20, t=10, b=10),
        plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig_arch, use_container_width=True)

    st.markdown('<div class="section-header">Research — Water Infrastructure Failure Prediction</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
        <div class="project-title">Predictive Modeling for Public Infrastructure Failure</div>
        <div class="project-desc">
            Developed predictive models for water infrastructure failure, utilizing real-world data sets
            to calculate <strong>Optimal Response Time (ORT)</strong> vs. <strong>Actual Repair Time (ART)</strong>.
            Applied regression analysis, data cleaning, and ML techniques to identify failure patterns
            and optimize maintenance scheduling for public water systems.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("##### Infrastructure Response Analysis (Simulated)")

    np.random.seed(42)
    months = pd.date_range("2024-06-01", periods=12, freq="M").strftime("%b %Y")
    ort = np.random.uniform(2, 6, 12)
    art = ort + np.random.uniform(1, 8, 12)

    fig_infra = go.Figure()
    fig_infra.add_trace(go.Bar(x=months, y=ort, name="Optimal Response Time (hrs)", marker_color="#2c5364"))
    fig_infra.add_trace(go.Bar(x=months, y=art, name="Actual Repair Time (hrs)", marker_color="#e07a5f"))
    fig_infra.add_trace(go.Scatter(
        x=months, y=art - ort, name="Gap (ART - ORT)",
        line=dict(color="#f2cc8f", width=2.5, dash="dot"), yaxis="y",
    ))
    fig_infra.update_layout(
        barmode="group", height=400, template="plotly_white",
        yaxis_title="Hours",
        legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5),
        margin=dict(l=40, r=20, t=20, b=60),
    )
    st.plotly_chart(fig_infra, use_container_width=True)

    st.markdown('<div class="section-header">Ventures & Other Projects</div>', unsafe_allow_html=True)

    projects = [
        ("Albo Tech SARL",
         "A cross-border digital agency operating in South Africa and the DRC, delivering full-stack web solutions, user engagement tracking, and conversion optimization for international markets."),
        ("Claudine Tech",
         "Technology company specializing in digital solutions, managing full-stack deployments and tracking business intelligence metrics across multiple markets."),
    ]

    for title, desc in projects:
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{title}</div>
            <div class="project-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SKILLS & TOOLS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Skills & Tools":
    st.markdown('<div class="section-header">Technical Skill Proficiency</div>', unsafe_allow_html=True)

    skills_data = pd.DataFrame({
        "Skill": ["Java", "PHP", "Python", "JavaScript", "SQL",
                   "Machine Learning", "Data Science", "Cybersecurity",
                   "API Integration", "Multi-threaded Apps", "Full-Stack Dev", "Cloud/HPC"],
        "Proficiency": [92, 88, 82, 78, 85,
                        80, 78, 82,
                        86, 88, 90, 70],
        "Category": ["Backend"] * 2 + ["Data & ML"] * 3 + ["Data & ML"] * 3 + ["Architecture"] * 4,
    })

    cat_colors = {
        "Backend": "#2c5364",
        "Data & ML": "#3d85c6",
        "Architecture": "#81b29a",
    }
    skills_data["Color"] = skills_data["Category"].map(cat_colors)

    fig_skills = go.Figure()
    for cat in skills_data["Category"].unique():
        subset = skills_data[skills_data["Category"] == cat]
        fig_skills.add_trace(go.Bar(
            y=subset["Skill"], x=subset["Proficiency"],
            orientation="h", name=cat,
            marker_color=cat_colors[cat],
            text=subset["Proficiency"].astype(str) + "%",
            textposition="outside",
        ))
    fig_skills.update_layout(
        barmode="group", height=520, template="plotly_white",
        xaxis=dict(range=[0, 105], title="Proficiency (%)"),
        legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5),
        margin=dict(l=140, r=40, t=20, b=60),
    )
    st.plotly_chart(fig_skills, use_container_width=True)

    st.markdown('<div class="section-header">Toolbox</div>', unsafe_allow_html=True)

    tools = [
        "Java", "PHP", "Python", "JavaScript", "SQL", "HTML/CSS",
        "Scikit-learn", "Pandas", "NumPy", "Matplotlib", "Plotly",
        "Spring Boot", "Laravel", "Node.js", "React",
        "MySQL", "PostgreSQL", "MongoDB",
        "Git", "GitHub", "Docker", "Linux",
        "Cisco Security", "SOS Protocols", "API Design",
        "Claude CLI", "HPC", "Streamlit",
    ]
    st.markdown(" ".join([f'<span class="skill-tag">{t}</span>' for t in tools]), unsafe_allow_html=True)

    st.markdown('<div class="section-header">Competency Radar</div>', unsafe_allow_html=True)

    categories = ["Backend Engineering", "Machine Learning", "Cybersecurity",
                   "Full-Stack Development", "Data Science", "System Architecture"]
    values = [92, 80, 82, 90, 78, 85]
    values_closed = values + [values[0]]
    categories_closed = categories + [categories[0]]

    fig_radar = go.Figure(go.Scatterpolar(
        r=values_closed, theta=categories_closed,
        fill="toself", fillcolor="rgba(44,83,100,0.2)",
        line=dict(color="#2c5364", width=2),
        marker=dict(size=6, color="#2c5364"),
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        height=420, margin=dict(l=60, r=60, t=40, b=40),
        template="plotly_white",
    )
    st.plotly_chart(fig_radar, use_container_width=True)


# ══════════════════════════════════════════════════════════════════════════════
# ACHIEVEMENTS & IMPACT
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Achievements & Impact":
    st.markdown('<div class="section-header">Key Accomplishments</div>', unsafe_allow_html=True)

    accomplishments = [
        ("🎓 Advanced Diploma in Computer Science",
         "Completed at Tshwane University of Technology, specializing in full-stack systems, machine learning, and predictive modeling."),
        ("🔬 CHPC 2026 Research Fellow",
         "Selected for the Coding Summer School at the University of Pretoria to master High-Performance Computing."),
        ("🏢 Founder — Albo Tech SARL & Claudine Tech",
         "Demonstrated ability to take research-level concepts and commercialize them into functional, cross-border digital agencies operating in South Africa and the DRC."),
        ("🔒 Cisco Certified in Cybersecurity",
         "Expert in implementing SOS protocols and secure user-data handling across enterprise systems."),
    ]

    for title, desc in accomplishments:
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{title}</div>
            <div class="project-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">Research & Quantitative Impact</div>', unsafe_allow_html=True)

    st.markdown("##### System Optimization — Script Performance Improvement")

    np.random.seed(10)
    iterations = list(range(1, 11))
    before_opt = [45, 42, 48, 44, 46, 43, 47, 45, 44, 46]
    after_opt = [45, 38, 32, 28, 24, 21, 19, 17, 16, 15]

    fig_perf = go.Figure()
    fig_perf.add_trace(go.Scatter(
        x=iterations, y=before_opt, name="Before Optimization",
        line=dict(color="#e07a5f", width=2.5), mode="lines+markers",
    ))
    fig_perf.add_trace(go.Scatter(
        x=iterations, y=after_opt, name="After Optimization",
        line=dict(color="#2c5364", width=2.5), mode="lines+markers",
        fill="tonexty", fillcolor="rgba(44,83,100,0.1)",
    ))
    fig_perf.update_layout(
        height=380, template="plotly_white",
        xaxis_title="Optimization Iteration",
        yaxis_title="Execution Latency (seconds)",
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        margin=dict(l=40, r=20, t=20, b=60),
    )
    st.plotly_chart(fig_perf, use_container_width=True)

    st.markdown("##### Cross-Border Business Intelligence Metrics (Simulated)")

    quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024", "Q1 2025", "Q2 2025"]
    sa_engagement = [320, 480, 620, 780, 950, 1150]
    drc_engagement = [150, 220, 340, 410, 530, 680]
    sa_conversion = [3.2, 3.8, 4.1, 4.5, 5.0, 5.4]
    drc_conversion = [2.1, 2.5, 3.0, 3.3, 3.8, 4.2]

    fig_biz = go.Figure()
    fig_biz.add_trace(go.Bar(x=quarters, y=sa_engagement, name="SA — User Engagement", marker_color="#2c5364"))
    fig_biz.add_trace(go.Bar(x=quarters, y=drc_engagement, name="DRC — User Engagement", marker_color="#81b29a"))
    fig_biz.add_trace(go.Scatter(
        x=quarters, y=[c * 100 for c in sa_conversion], name="SA — Conversion Rate (x100)",
        line=dict(color="#f2cc8f", width=2.5), yaxis="y",
    ))
    fig_biz.add_trace(go.Scatter(
        x=quarters, y=[c * 100 for c in drc_conversion], name="DRC — Conversion Rate (x100)",
        line=dict(color="#e07a5f", width=2.5, dash="dot"), yaxis="y",
    ))
    fig_biz.update_layout(
        barmode="group", height=420, template="plotly_white",
        yaxis_title="Users / Rate (x100)",
        legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5),
        margin=dict(l=40, r=20, t=20, b=60),
    )
    st.plotly_chart(fig_biz, use_container_width=True)

    st.markdown('<div class="section-header">Research Interests</div>', unsafe_allow_html=True)

    interests = {
        "High-Performance Computing": 92,
        "Predictive Modeling": 88,
        "Scalable Systems Architecture": 90,
        "Machine Learning": 85,
        "Infrastructure Analytics": 82,
        "Cybersecurity": 80,
        "Data Engineering": 78,
        "Cross-Border Tech Solutions": 75,
    }
    fig_int = go.Figure(go.Bar(
        x=list(interests.values()),
        y=list(interests.keys()),
        orientation="h",
        marker=dict(
            color=list(interests.values()),
            colorscale=[[0, "#b0d4e8"], [1, "#0f2027"]],
        ),
    ))
    fig_int.update_layout(
        height=350, template="plotly_white",
        xaxis=dict(title="Interest Level", range=[0, 100]),
        margin=dict(l=200, r=20, t=10, b=40),
    )
    st.plotly_chart(fig_int, use_container_width=True)


# ══════════════════════════════════════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Contact":
    st.markdown('<div class="section-header">Get in Touch</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="project-card">
            <div class="project-title">🎓 Affiliation</div>
            <div class="project-desc">
                Tshwane University of Technology<br>
                CHPC 2026 Research Fellow — University of Pretoria
            </div>
        </div>
        <div class="project-card">
            <div class="project-title">💼 Ventures</div>
            <div class="project-desc">
                Albo Tech SARL · Claudine Tech<br>
                <em>Cross-border digital agencies (SA & DRC)</em>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="project-card">
            <div class="project-title">🔗 Profiles</div>
            <div class="project-desc">
                <a href="https://github.com/Elienock" target="_blank">GitHub — Elienock</a><br>
                <a href="https://linkedin.com/" target="_blank">LinkedIn</a>
            </div>
        </div>
        <div class="project-card">
            <div class="project-title">📍 Location</div>
            <div class="project-desc">Pretoria, Gauteng, South Africa</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("##### Send a Message")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Thanks for reaching out! I'll get back to you soon.")


# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#6b7c8a; font-size:0.8rem; font-family:Inter,sans-serif;'>"
    "Built with Streamlit · © 2026 Elienock Lubaya Mulumba · Albo Tech SARL & Claudine Tech"
    "</div>",
    unsafe_allow_html=True,
)