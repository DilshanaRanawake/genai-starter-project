from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
generator = pipeline("text-generation", model="gpt2")

class Prompt(BaseModel):
    text: str
    max_tokens: int = 100
    tone: str = None
    keywords: list[str] = []

@app.post("/generate")
def generate_text(prompt: Prompt):
    prompt_text = prompt.text

    if prompt.tone:
        prompt_text = f"Write in a {prompt.tone} tone: {prompt_text}"
    
    if prompt.keywords:
        prompt_text += " Include the following keywords: " + ", ".join(prompt.keywords)

    output = generator(prompt.text, max_length=100, num_return_sequences=1)
    return {"result": output[0]["generated_text"]}
