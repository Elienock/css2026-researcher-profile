import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from datetime import datetime

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Jonathan L. Wangatia | Researcher Profile",
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

    /* Hide Streamlit branding */
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
        ["Home", "Research", "Skills & Tools", "Publications & Presentations", "Contact"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("##### Quick Links")
    st.markdown("[GitHub](https://github.com/) · [LinkedIn](https://linkedin.com/) · [Google Scholar](https://scholar.google.com/)")
    st.markdown("---")
    st.caption(f"Last updated: {datetime.now().strftime('%B %Y')}")


# ══════════════════════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════════════════════
if page == "Home":
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-name">Jonathan L. Wangatia</div>
        <div class="hero-title">MSc Industrial Engineering Candidate · ML Researcher · Data Analytics Entrepreneur</div>
        <div class="hero-bio">
            Bridging traditional industrial engineering with modern AI/ML to solve
            real-world problems across healthcare, logistics, and operations. My research
            focuses on building intelligent forecasting systems that help organisations
            make data-driven decisions — with a special emphasis on healthcare demand
            prediction in resource-constrained African settings.
        </div>
        <div style="margin-top:1rem;">
            <span class="contact-badge">📍 Pretoria, South Africa</span>
            <span class="contact-badge">🎓 University of Pretoria</span>
            <span class="contact-badge">🏢 CEO, JLWanalytics</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><div class="metric-value">3</div><div class="metric-label">ML Models Built</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><div class="metric-value">200+</div><div class="metric-label">Students Mentored</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><div class="metric-value">5+</div><div class="metric-label">Industry Certs</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><div class="metric-value">2</div><div class="metric-label">Countries</div></div>', unsafe_allow_html=True)

    # Education Timeline
    st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-year">2024 – Present</div>
        <div class="timeline-title">MSc Industrial Engineering</div>
        <div class="timeline-subtitle">University of Pretoria, South Africa</div>
        <div class="timeline-subtitle" style="margin-top:0.3rem; color:#4a5c6a;">
            Thesis: <em>HealthForecast AI – Machine Learning for Hospital Patient Arrival Prediction</em>
        </div>
    </div>
    <div class="timeline-item">
        <div class="timeline-year">Completed</div>
        <div class="timeline-title">BTech Electromechanical Engineering</div>
        <div class="timeline-subtitle">University of Lubumbashi, DRC</div>
    </div>
    """, unsafe_allow_html=True)

    # Certifications
    st.markdown('<div class="section-header">Certifications</div>', unsafe_allow_html=True)

    certs = [
        "Six Sigma Green Belt", "Azure Machine Learning", "CSCMP Supply Chain Management",
        "Microsoft Power Platform", "Fire Academy (2024)"
    ]
    tags_html = " ".join([f'<span class="skill-tag">{c}</span>' for c in certs])
    st.markdown(tags_html, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# RESEARCH
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Research":
    st.markdown('<div class="section-header">Flagship Research — HealthForecast AI</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
        <div class="project-title">HealthForecast AI: Machine Learning Platform for Predicting Hospital Patient Arrivals</div>
        <div class="project-desc">
            An end-to-end ML forecasting platform designed to help hospitals anticipate patient demand,
            optimise staff allocation, and reduce wait times. The system compares three complementary
            modelling approaches — <strong>ARIMA</strong> (statistical baseline), <strong>LSTM</strong>
            (deep-learning sequence model), and <strong>XGBoost</strong> (gradient-boosted trees) — and
            incorporates uncertainty quantification through prediction intervals so that decision-makers
            can plan for best- and worst-case scenarios.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("##### Research Architecture")

    # Architecture diagram
    fig_arch = go.Figure()

    boxes = [
        {"x": 0.5, "y": 0.9, "text": "Raw Hospital Data", "color": "#0f2027"},
        {"x": 0.5, "y": 0.72, "text": "Feature Engineering\n& Preprocessing", "color": "#203a43"},
        {"x": 0.15, "y": 0.5, "text": "ARIMA\n(Statistical)", "color": "#2c5364"},
        {"x": 0.5, "y": 0.5, "text": "LSTM\n(Deep Learning)", "color": "#2c5364"},
        {"x": 0.85, "y": 0.5, "text": "XGBoost\n(Ensemble)", "color": "#2c5364"},
        {"x": 0.5, "y": 0.28, "text": "Ensemble &\nUncertainty Quantification", "color": "#203a43"},
        {"x": 0.5, "y": 0.1, "text": "Streamlit Dashboard\n& Actionable Insights", "color": "#0f2027"},
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

    # Demo forecast
    st.markdown("##### Interactive Forecast Demo")
    st.caption("Simulated patient-arrival forecast to illustrate the modelling approach.")

    np.random.seed(42)
    days = 90
    t = np.arange(days)
    trend = 120 + 0.3 * t
    seasonal = 15 * np.sin(2 * np.pi * t / 7)
    noise = np.random.normal(0, 8, days)
    actual = trend + seasonal + noise

    forecast_start = 70
    pred_t = np.arange(forecast_start, days)
    pred_arima = trend[forecast_start:] + seasonal[forecast_start:] + np.random.normal(0, 4, len(pred_t))
    pred_lstm = trend[forecast_start:] + seasonal[forecast_start:] + np.random.normal(2, 3.5, len(pred_t))
    pred_xgb = trend[forecast_start:] + seasonal[forecast_start:] + np.random.normal(-1, 3, len(pred_t))
    ensemble = (pred_arima + pred_lstm + pred_xgb) / 3
    upper = ensemble + 18
    lower = ensemble - 18

    dates = pd.date_range("2025-01-01", periods=days, freq="D")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=actual, name="Actual Arrivals", line=dict(color="#1a2f3a", width=2)))
    fig.add_trace(go.Scatter(x=dates[forecast_start:], y=pred_arima, name="ARIMA", line=dict(color="#e07a5f", width=1.5, dash="dot")))
    fig.add_trace(go.Scatter(x=dates[forecast_start:], y=pred_lstm, name="LSTM", line=dict(color="#3d85c6", width=1.5, dash="dot")))
    fig.add_trace(go.Scatter(x=dates[forecast_start:], y=pred_xgb, name="XGBoost", line=dict(color="#81b29a", width=1.5, dash="dot")))
    fig.add_trace(go.Scatter(x=dates[forecast_start:], y=ensemble, name="Ensemble", line=dict(color="#f2cc8f", width=2.5)))
    fig.add_trace(go.Scatter(
        x=pd.concat([pd.Series(dates[forecast_start:]), pd.Series(dates[forecast_start:][::-1])]),
        y=np.concatenate([upper, lower[::-1]]),
        fill="toself", fillcolor="rgba(242,204,143,0.15)",
        line=dict(width=0), name="95% Prediction Interval", showlegend=True,
    ))
    fig.add_vline(x=dates[forecast_start], line_dash="dash", line_color="grey", annotation_text="Forecast start")
    fig.update_layout(
        height=400, template="plotly_white",
        yaxis_title="Daily Patient Arrivals",
        legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5),
        margin=dict(l=40, r=20, t=20, b=60),
    )
    st.plotly_chart(fig, use_container_width=True)

    # Other projects
    st.markdown('<div class="section-header">Other Projects</div>', unsafe_allow_html=True)

    projects = [
        ("JLWanalytics — Africa's Premier Data Refinery",
         "A data analytics startup offering end-to-end data engineering, ML modelling, and BI dashboard services targeting African enterprises."),
        ("PizzaOps Intelligence",
         "AI-powered delivery operations analytics for pizza chains — route optimisation, demand forecasting, and real-time KPI monitoring."),
        ("JusticeForecast SA",
         "Predictive analytics platform for South African courts to forecast case volumes and optimise judicial resource allocation."),
        ("TREKA's Services",
         "Professional translation company bridging French and English communication across business, legal, and technical domains."),
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
        "Skill": ["Python / ML", "Streamlit", "Pandas / NumPy", "Scikit-learn", "TensorFlow / Keras",
                   "SQL", "Power BI", "Excel / VBA", "Docker", "Git / GitHub",
                   "JavaScript / React", "Django / FastAPI"],
        "Proficiency": [92, 88, 90, 85, 78, 80, 82, 85, 65, 75, 55, 60],
        "Category": ["ML & Data Science"] * 5 + ["Data & BI"] * 3 + ["DevOps"] * 2 + ["Web Dev"] * 2,
    })

    cat_colors = {
        "ML & Data Science": "#2c5364",
        "Data & BI": "#3d85c6",
        "DevOps": "#81b29a",
        "Web Dev": "#e07a5f",
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
        barmode="group", height=500, template="plotly_white",
        xaxis=dict(range=[0, 105], title="Proficiency (%)"),
        legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5),
        margin=dict(l=120, r=40, t=20, b=60),
    )
    st.plotly_chart(fig_skills, use_container_width=True)

    # Toolbox Tag Cloud
    st.markdown('<div class="section-header">Toolbox</div>', unsafe_allow_html=True)

    tools = [
        "Python", "Streamlit", "Pandas", "NumPy", "Scikit-learn", "TensorFlow", "Keras",
        "XGBoost", "ARIMA", "LSTM", "Plotly", "Matplotlib", "SQL", "PostgreSQL",
        "Power BI", "Excel", "VBA", "Docker", "Git", "GitHub", "VS Code",
        "Azure ML", "Jupyter", "FastAPI", "Django", "React", "Next.js",
        "Six Sigma", "Supply Chain Mgmt", "SCADA", "PLC Programming",
    ]
    st.markdown(" ".join([f'<span class="skill-tag">{t}</span>' for t in tools]), unsafe_allow_html=True)

    # Radar chart – competency areas
    st.markdown('<div class="section-header">Competency Radar</div>', unsafe_allow_html=True)

    categories = ["Machine Learning", "Data Engineering", "Web Development",
                   "Statistical Analysis", "Industrial Engineering", "Project Management"]
    values = [90, 80, 60, 85, 82, 78]
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
# PUBLICATIONS & PRESENTATIONS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Publications & Presentations":
    st.markdown('<div class="section-header">Research Output</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
        <div class="project-title">📝 MSc Thesis (In Progress)</div>
        <div class="project-desc">
            <strong>HealthForecast AI: A Comparative Machine Learning Framework for Hospital
            Patient Arrival Prediction</strong><br>
            University of Pretoria · Department of Industrial & Systems Engineering<br><br>
            Investigating how ARIMA, LSTM, and XGBoost models can be combined with
            uncertainty quantification to produce reliable, actionable demand forecasts
            for hospitals in resource-constrained settings.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">Conference & Presentations</div>', unsafe_allow_html=True)

    st.info("Conference submissions planned for 2026 upon thesis completion. Areas of interest include SAIIE (Southern African Institute for Industrial Engineering) and related ML-in-healthcare venues.")

    st.markdown('<div class="section-header">Teaching & Mentorship</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
        <div class="project-title">🎓 Teaching Assistant — University of Pretoria</div>
        <div class="project-desc">
            Supporting 200+ undergraduate and postgraduate students in industrial engineering
            courses. Responsibilities include tutoring in operations research, statistics,
            and data analytics modules; grading assignments; and providing one-on-one
            academic mentorship.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Research interests word cloud via bar chart
    st.markdown('<div class="section-header">Research Interests</div>', unsafe_allow_html=True)

    interests = {
        "Time-Series Forecasting": 95,
        "Healthcare Analytics": 90,
        "MLOps & Deployment": 82,
        "Uncertainty Quantification": 88,
        "Operations Research": 80,
        "Supply Chain Optimisation": 75,
        "Deep Learning (LSTM/RNN)": 85,
        "Ensemble Methods": 83,
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
        margin=dict(l=180, r=20, t=10, b=40),
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
            <div class="project-title">📧 Email</div>
            <div class="project-desc">jonathan@jlwanalytics.com</div>
        </div>
        <div class="project-card">
            <div class="project-title">🏢 Affiliation</div>
            <div class="project-desc">
                University of Pretoria<br>
                Dept. of Industrial & Systems Engineering
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="project-card">
            <div class="project-title">💼 Venture</div>
            <div class="project-desc">
                JLWanalytics<br>
                <em>Africa's Premier Data Refinery</em>
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
    "Built with Streamlit · © 2026 Jonathan L. Wangatia · JLWanalytics"
    "</div>",
    unsafe_allow_html=True,
)
