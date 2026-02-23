from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_compress_endpoint():
    payload = {"text": "Automated Unit Testing with Pytest and HTTPX"}
    response = client.post("/compress", json=payload)
    
    assert response.status_code == 200
    
    data = response.json()
    assert "compressed_text" in data
    assert "original_length" in data
    assert "compressed_length" in data
    
    # "Auomae Uni Tesing wh Pyes and HTTPX" without vowels "a e i o u" (case-insensitive)
    expected_original = "Automated Unit Testing with Pytest and HTTPX"
    expected_compressed = "tmtd nt Tstng wth Pytst nd HTTPX"
    
    assert data["original_length"] == len(expected_original)
    assert data["compressed_text"] == expected_compressed
    assert data["compressed_length"] == len(expected_compressed)
