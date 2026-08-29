import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Tanush Khare — 23-Microservice Architecture Portfolio",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
    .main-header { font-size: 2.2rem; font-weight: 800; margin-bottom: 0.2rem; color: #0f172a; }
    .sub-header { font-size: 1.1rem; color: #475569; margin-bottom: 1.5rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🚀 Tanush Khare — Systems & AI Portfolio Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Unified control plane connecting all 23 verified backend engines, distributed microservices, and AI models.</div>', unsafe_allow_html=True)

# Metrics Strip
m1, m2, m3, m4 = st.columns(4)
m1.metric("Production Services", "23 Repositories")
m2.metric("Test Assertion Pass", "100% Passing")
m3.metric("Core AI/ML Stack", "RAG, MLOps, NLP")
m4.metric("Distributed Stack", "FastAPI, PySpark, WS")

st.divider()

# Master Dataset
projects = [
    {"id": "01", "name": "AI Resume Analyzer", "category": "AI & NLP", "desc": "spaCy NER PDF resume parser with cosine similarity matching.", "repo": "ai-resume-analyzer"},
    {"id": "02", "name": "Autonomous Research Assistant", "category": "Agentic AI", "desc": "Agentic multi-hop research pipeline with source validation.", "repo": "autonomous-research-assistant"},
    {"id": "03a", "name": "Realtime Chatbot", "category": "WebSockets", "desc": "Asynchronous WebSocket streaming session assistant.", "repo": "realtime-chatbot"},
    {"id": "03b", "name": "Vector RAG Q&A System", "category": "Vector Search", "desc": "Dense vector retrieval engine with text chunking and similarity search.", "repo": "vector-rag-qa-system"},
    {"id": "04a", "name": "AI Meeting Summarizer", "category": "AI & NLP", "desc": "Audio transcript summarization and action item extractor.", "repo": "ai-meeting-summarizer"},
    {"id": "04b", "name": "Real-Time ETL Dashboard", "category": "DataOps", "desc": "Stream data ingestion pipeline with transformation metrics.", "repo": "etl-dashboard"},
    {"id": "05", "name": "Fake News Classifier", "category": "AI & NLP", "desc": "Linguistic cue credibility scoring engine.", "repo": "fake-news-classifier"},
    {"id": "06", "name": "Collaborative Whiteboard", "category": "WebSockets", "desc": "Multi-client real-time canvas synchronization via WebSockets.", "repo": "collaborative-realtime-whiteboard"},
    {"id": "07", "name": "Placement Management Portal", "category": "Fullstack", "desc": "Academic eligibility screening and career application tracker.", "repo": "placement-management-portal"},
    {"id": "08", "name": "Voice to SQL Query Engine", "category": "DataOps", "desc": "AST SQL sandboxing and safe relational query synthesis.", "repo": "voice-to-sql-query-engine"},
    {"id": "09", "name": "E-Commerce Microservices", "category": "Distributed Systems", "desc": "Atomic mutex-locked multi-tier checkout microservices.", "repo": "ecommerce-microservices"},
    {"id": "10", "name": "Financial Sentiment Streaming", "category": "Fintech & Data", "desc": "Market sentiment polarity stream analyzer.", "repo": "financial-sentiment-streaming"},
    {"id": "11", "name": "PySpark Log Analyzer", "category": "Big Data & PySpark", "desc": "Distributed log partitioning and error surge detection.", "repo": "pyspark-log-analyzer"},
    {"id": "12", "name": "Fintech Fraud Detection", "category": "Fintech & Data", "desc": "Behavioral anomaly risk evaluation engine.", "repo": "fintech-fraud-detection"},
    {"id": "13", "name": "MLOps Retraining Pipeline", "category": "MLOps", "desc": "PSI and Kolmogorov-Smirnov drift detection control plane.", "repo": "mlops-retraining-pipeline"},
    {"id": "14", "name": "Packet Sniffer Anomaly Detector", "category": "Cybersecurity", "desc": "Socket frame capture and volumetric surge classification.", "repo": "packet-sniffer-anomaly-detector"},
    {"id": "15", "name": "Phishing URL Threat Detector", "category": "Cybersecurity", "desc": "Lexical Shannon entropy scoring and domain threat scanner.", "repo": "phishing-detector"},
    {"id": "16", "name": "DevOps Telemetry Dashboard", "category": "DevOps & Zero-Trust", "desc": "Zero-Trust IAM origin verification and cluster harvester.", "repo": "devops-telemetry-dashboard"},
    {"id": "17", "name": "Serverless File Pipeline", "category": "Cloud & Serverless", "desc": "S3 event-driven automated execution pipeline.", "repo": "serverless-file-pipeline"},
    {"id": "18a", "name": "Smart Face Attendance", "category": "Computer Vision", "desc": "Biometric face verification and attendance database.", "repo": "smart-face-attendance"},
    {"id": "18b", "name": "Smart Factory IoT Telemetry", "category": "IoT & Smart Grid", "desc": "ISO 10816 vibration analytics and RUL degradation curves.", "repo": "Smart-Factory-IOT"},
    {"id": "19", "name": "Spatial Asset Geofencing", "category": "GIS & Spatial AI", "desc": "Shapely Point-in-Polygon containment calculation.", "repo": "spatial-asset-geofencing"},
    {"id": "20", "name": "IoT Energy Monitoring", "category": "IoT & Smart Grid", "desc": "Smart grid harmonic power telemetry and load balancer.", "repo": "iot-energy-monitoring"}
]

# Quick Jump Dropdown
st.subheader("⚡ Quick Jump Launchpad")
c1, c2 = st.columns([3, 1])

with c1:
    selected_name = st.selectbox(
        "Select a Project to Inspect",
        [f"Project {p['id']}: {p['name']} ({p['category']})" for p in projects]
    )
    selected_proj = next(p for p in projects if f"Project {p['id']}: {p['name']}" in selected_name)

with c2:
    st.write("")
    st.write("")
    st.link_button(f"Open {selected_proj['name']} ↗", f"https://github.com/tanushkhare/{selected_proj['repo']}", type="primary")

st.divider()

# Category Filter & Grid
st.subheader("📦 Full Ecosystem Directory")
categories = ["All"] + sorted(list(set(p["category"] for p in projects)))
selected_category = st.pills("Filter by Domain", categories, default="All")

filtered_projects = projects if selected_category == "All" else [p for p in projects if p["category"] == selected_category]

cols = st.columns(3)
for idx, p in enumerate(filtered_projects):
    with cols[idx % 3]:
        with st.container(border=True):
            st.caption(f"PROJECT {p['id']} • {p['category']}")
            st.markdown(f"**{p['name']}**")
            st.write(p["desc"])
            st.link_button("View on GitHub →", f"https://github.com/tanushkhare/{p['repo']}")
