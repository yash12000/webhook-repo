# GitHub Webhook Activity Dashboard

## 📌 Overview
This project captures GitHub events (Push, Pull Request, Merge) via webhooks, stores them in MongoDB, and displays them in a real-time UI.

## 🚀 Features
- GitHub Webhook Integration
- MongoDB Storage
- Real-time UI (refresh every 15 seconds)
- Clean minimal design

## 🛠 Tech Stack
- Backend: Flask
- Frontend: React
- Database: MongoDB

## 🔗 Repositories
- action-repo: triggers events
- webhook-repo: main implementation

## ⚙️ How it works
1. GitHub sends webhook events
2. Flask API processes and stores data
3. React UI fetches data every 15 seconds

## 📊 Event Formats
- PUSH → {author} pushed to {branch}
- PR → {author} submitted PR from {from} to {to}
- MERGE → {author} merged {from} to {to}