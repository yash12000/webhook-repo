# GitHub Webhook Activity Dashboard

## 📌 Overview

This project captures GitHub repository events (Push, Pull Request, Merge) using webhooks, stores them in MongoDB, and displays them in a real-time dashboard UI.

---

## 🚀 Features

- GitHub Webhook Integration (Push, Pull Request, Merge)
- Flask Backend API
- MongoDB Database Storage
- Real-time UI updates (polling every 15 seconds)
- Clean and minimal user interface
- Duplicate event handling using request_id

---

## 🛠 Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** React (Vite)
- **Database:** MongoDB
- **Integration:** GitHub Webhooks
- **Tunneling:** Ngrok

---

## 📂 Project Structure


webhook-repo/
│
├── backend/
│ ├── app.py
│ ├── config.py
│ ├── models.py
│ ├── requirements.txt
│
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── main.jsx
│ │ └── index.css
│ ├── index.html
│ ├── package.json
│ ├── vite.config.js
│
├── .gitignore
└── README.md


---

## ⚙️ How It Works

1. GitHub repository (action-repo) triggers events:

   - Push
   - Pull Request
   - Merge

2. GitHub sends webhook payload to Flask backend (`/webhook`)

3. Backend processes and stores event data in MongoDB

4. Frontend fetches data every 15 seconds from `/events`

5. UI displays formatted activity logs

---

## 📊 Event Format

### 🔹 PUSH

{author} pushed to {branch} on {timestamp}


### 🔹 PULL REQUEST

{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}


### 🔹 MERGE

{author} merged branch {from_branch} to {to_branch} on {timestamp}


---

## 🔗 API Endpoints

- `POST /webhook` → Receives GitHub events
- `GET /events` → Fetches stored events

---

## ▶️ Run Locally

### Backend

cd backend

pip install -r requirements.txt

python app.py


### Frontend

cd frontend

npm install

npm run dev


---

## 🔄 Webhook Setup

- Use Ngrok:

ngrok http 5000


- Add webhook in action-repo:

https://<ngrok-url>/webhook


- Content Type: `application/json`
- Events: Push + Pull Requests

---

## 💡 Notes

- UI refreshes every 15 seconds
- MongoDB stores only required fields
- Clean and minimal design as per requirements

---

## 👨‍💻 Author

Yash Janbandhu
