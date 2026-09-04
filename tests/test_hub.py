import os

def test_hub_structure():
    index_file = os.path.join(os.path.dirname(__file__), "..", "frontend", "index.html")
    assert os.path.exists(index_file)
    with open(index_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Tanush Khare" in content
    assert "Distributed Systems & AI Engineering Portfolio" in content
