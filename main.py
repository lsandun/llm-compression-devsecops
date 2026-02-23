from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="LLM Compression API")

class CompressRequest(BaseModel):
    text: str

class CompressResponse(BaseModel):
    compressed_text: str
    original_length: int
    compressed_length: int

@app.post("/compress", response_model=CompressResponse)
async def compress_text(request: CompressRequest):
    # Mock compression: simply remove vowels for demonstration
    vowels = "aeiouAEIOU"
    compressed = "".join([char for char in request.text if char not in vowels])
    
    return CompressResponse(
        compressed_text=compressed,
        original_length=len(request.text),
        compressed_length=len(compressed)
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) # nosec B104
