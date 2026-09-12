import os
import pytest

def test_hub_structure():
    assert os.path.exists("index.html") or os.path.exists("public/index.html")
    target = "index.html" if os.path.exists("index.html") else "public/index.html"
    with open(target, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Tanush Khare" in content
    assert "Vector RAG Retrieval Pipeline" in content
    assert "MLOps Drift & Retraining Control Plane" in content
    assert "High-Throughput Spatial Geofencing" in content
    assert "High-Concurrency Microservices" in content
    assert "ai-resume-analyzer" in content
    assert "realtime-chatbot" in content
