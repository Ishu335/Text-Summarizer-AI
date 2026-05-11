from fastapi import FastAPI,Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration ,T5Tokenizer
import re
import torch

from fastapi.templating  import Jinja2Templates #Ui Part
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# initallize our fastapi 
app=FastAPI(title="Text Summarizer App",description="Test Summarizer using T5",version="1.0 ")

#model and Tokenizer
model=T5ForConditionalGeneration.from_pretrained("./save_summary_model")
tokenizer=T5Tokenizer.from_pretrained("./save_summary_model")

#device select
if torch.backends.mps.is_available():
    device=torch.device("mps")
elif torch.cuda.is_available():
    device=torch.device("cuda")
else:
    device=torch.device("cpu")
model.to(device)

#templeating
templates=Jinja2Templates(directory="templates")

#input Schema for dialogue => string type 
class DialogueInput(BaseModel):
    dialogue:str  #<= here we define the input is come is dialogue string datatype


#clean data
def clean_data(text):
    text = re.sub(r'\s+', ' ', text) #space
    text = re.sub(r'\r\n', '', text) #line
    text = re.sub(r'<.*?>', '', text) # Remove HTMl Tags
    text = text.strip().lower() #Remove extra space and convert into lower case
    return text

#summarization logic code   
def summarize_dialogue(dialogue:str)-> str:

    dialogue = clean_data(dialogue)   # Clean data

    # Tokenize the dialogue
    inputs = tokenizer(
        dialogue,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    )

    model.to(device)

    # Move tensors to device
    input_ids = inputs["input_ids"].to(device)
    attention_mask = inputs["attention_mask"].to(device)

    # Generate summary
    targets = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_length=150,
        num_beams=4,
        early_stopping=True
    )

    # Decode token ids to text
    summary = tokenizer.decode(
        targets[0],
        skip_special_tokens=True
    )

    return summary

#API Endpoints
@app.post("/summarize/")
async def summarize(dialogue_input:DialogueInput):
    summary=summarize_dialogue(dialogue_input.dialogue)
    return {"summary":summary}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return  templates.TemplateResponse(
        request=request,
        name="index.html"
    )