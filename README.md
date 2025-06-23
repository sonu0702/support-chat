
# 💬 RAG Support Chatbot

A **Retrieval-Augmented Generation (RAG)** chatbot built using **FastAPI** (Python) for the backend and **Next.js + TypeScript** for the frontend. This bot is trained on customer support documentation and answers only based on that information.

> ✅ If a query lies outside the documentation, the bot responds with **"I don't know"**.

---

## 📦 Project Structure

```
.
├── backend       # FastAPI server with RAG logic
└── frontend      # Next.js frontend chat interface
```

---

## 🚀 Features

* RAG-based chatbot trained on support docs.
* Will **not hallucinate** — returns "I don't know" for unsupported queries.
* Clean, responsive chat UI built with Next.js.
* Easily extensible with your own document store + vector DB setup.

---

## 🔧 Backend Setup (FastAPI + Python)

1. **Navigate to the backend directory**:

   ```bash
   cd backend
   ```

2. **Set up a virtual environment**:

   ```bash
   python3 -m venv support
   source ./support/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

4. **Check environment variables**:

   Ensure the `.env` file exists and contains:

   ```env
   GEMINI_API_KEY=your_key_here
   ```

5. **Run the FastAPI server**:

   ```bash
   uvicorn main:app --reload
   ```

6. **Test your APIs** at:

   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🌐 Frontend Setup (Next.js + TypeScript)

1. **Navigate to the frontend directory**:

   ```bash
   cd frontend
   ```

2. **Install dependencies**:

   ```bash
   npm install
   ```

3. **Start the development server**:

   ```bash
   npm run dev
   ```

4. Visit: [http://localhost:3000](http://localhost:3000)

---

## 📸 Demo Screenshot

Here’s a preview of the chatbot interface in action:

![Chatbot Screenshot](https://github.com/user-attachments/assets/1bb93b8f-7ba2-495b-98c6-b81520b40e9c)

---

## 📜 Notes

* Chatbot strictly answers based on support docs only.
* Easily extensible to integrate with Pinecone, ChromaDB, Weaviate, or other vector databases.

