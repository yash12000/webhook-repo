# 🎨 Frontend – GitHub Activity Dashboard

This is the **React-based UI** for the GitHub Webhook Activity Dashboard.  
It displays real-time GitHub events (Push, Pull Request, Merge) fetched from the backend API.

---

## 🚀 Features

- 📡 Fetches data from backend API
- 🔄 Auto-refresh every **15 seconds**
- 📊 Displays:
  - Push events
  - Pull Requests
  - Merge events
- 🧹 Clean and minimal UI
- ⚡ Fast performance using Vite

---

## 🛠 Tech Stack

- **React (Vite)**
- **JavaScript (ES6+)**
- **CSS**

---

## 📂 Folder Structure


frontend/

├── public/

├── src/

│ ├── App.jsx

│ ├── main.jsx

│ └── index.css
│

├── index.html

├── package.json

├── vite.config.js

└── README.md


---

## ⚙️ How It Works

1. Frontend calls backend API:

http://localhost:5000/events


2. Data is fetched every **15 seconds**

3. UI formats and displays events like:

- `yash12000 pushed to main on 01 Mar 2026`
- `yash12000 submitted a pull request from feature to main`
- `yash12000 merged branch feature to main`

---

## 🚀 Setup Instructions

### 🔹 Install dependencies

```bash
npm install

🔹 Run development server
npm run dev

🔹 Open in browser
http://localhost:5173

🔌 API Dependency

Make sure backend is running:

http://localhost:5000
💡 Notes

UI depends on backend API availability

Data auto-refreshes every 15 seconds

Duplicate events are filtered

👨‍💻 Author

Yash Janbandhu


---
