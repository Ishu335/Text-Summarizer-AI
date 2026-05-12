# 🧠 Text Summarizer AI

An AI-powered Text Summarization application built using **Transformer Models (T5)** and **FastAPI**.  
This project generates concise and meaningful summaries from large text inputs using Natural Language Processing (NLP).


## 📸 Project Preview

### T5 Transformer Architecture

![T5 Transformer](https://github.com/Ishu335/Text-Summarizer-AI/blob/82ca228939fe9443d35d4f2faa5c70e789c444de/img/T5.png)

### Application Screenshot

![Project Screenshot](https://github.com/Ishu335/Text-Summarizer-AI/blob/d0a240eaf7b469dbf3c0b9fa3bab01919d714588/img/Screenshot.png)

---
---

## 🚀 Features

- ✨ AI-based text summarization
- 🤖 Powered by Transformer Architecture
- 🧠 Uses `T5ForConditionalGeneration`
- ⚡ FastAPI backend
- 📊 NLP preprocessing pipeline
- 🌐 REST API support
- 🔥 Real-time summary generation
- 📦 Easy deployment

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI

### Machine Learning / NLP
- Transformers
- T5 Model
- PyTorch
- Hugging Face

### Other Libraries
- Pydantic
- Uvicorn
- Regex (Text preprocessing)

---

## 📂 Project Structure

```bash
Text-Summarizer-AI/
│
├── data/
├── img/
├── results/
├── main.py
├── requirements.txt
├── README.md
└── text_summrizer.ipynb
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Ishu335/Text-Summarizer-AI.git
```

### 2️⃣ Navigate to Project

```bash
cd Text-Summarizer-AI
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
uvicorn main:app --reload
```

Server will run on:

```bash
http://127.0.0.1:8000
```

---

## 🧠 Model Used

This project uses:

```python
T5ForConditionalGeneration
```

from Hugging Face Transformers.

Transformer-based summarization enables:
- Better contextual understanding
- Human-like summaries
- Improved sequence-to-sequence learning

---

---

## 📌 API Example

### Request

```json
{
  "text": "Artificial Intelligence is transforming industries..."
}
```

### Response

```json
{
  "summary": "AI is transforming industries."
}
```

---

## 📊 Future Improvements

- Add multilingual summarization
- Deploy using Docker
- Add React frontend
- Improve model accuracy
- Add authentication

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch
3. Commit changes
4. Push to branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

### Ishwar Sonawane

- GitHub: https://github.com/Ishu335

---

## ⭐ Support

If you like this project:

- Give it a ⭐ on GitHub
- Share it with others
- Follow for more AI/ML projects

---
