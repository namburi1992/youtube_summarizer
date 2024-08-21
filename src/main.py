from fastapi import FastAPI, Request
import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transcript_gen.transcript import get_transcript
# from llm_utils.summarize import summarize
from llm_utils.mistral_trial import summarize

app = FastAPI()
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
@app.get("/")
def ping():
    return {"Hello": "World"}

class URLRequest(BaseModel):
    url: str

class PayloadRequest(BaseModel):
    transcript: str
    max_tokens: int = 100
    temperature: float = 0.7
    summary_length: str = "brief"
    focus_points: str = "main ideas"
    tone: str = "neutral"
    audience: str = "general public"
    additional_instructions: str = ""
    output_format: str = "paragraphs"

@app.post("/transcript")
def get_transcript_route(request: URLRequest):
    print(request)
    url = request.url
    return get_transcript(url)
    
@app.post("/generate")
def get_summary(request: PayloadRequest):
    try:
        transcript = request.transcript
        return summarize(transcript)   
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))