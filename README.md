# 📦 Trackify — Smart Parcel Tracking & Delivery Management System

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-black)
![License](https://img.shields.io/badge/License-Educational-green)

**Trackify** is a role-based parcel tracking and delivery management system developed as a **final project** for  
**TBC IT Academy (TechSchool) × GeoLab** — Web Development (Back End: Python).

It demonstrates practical usage of **Flask**, **databases**, authentication, and **role-based access control** in a real-world logistics scenario.

---

## 🎯 Project Goal

Parcel delivery systems often lack transparency and structured communication.  
Trackify provides a centralized platform where:
- Clients can create and track shipments
- Companies can process deliveries
- Admins can manage the entire system

---

## 👥 Target Audience
- Individual users sending parcels
- Delivery companies
- Platform administrators

---

## 💡 Key Insight
- Role-based access (Client / Company / Admin)
- Shipment-specific and general chat
- Shipment timeline history
- Saved addresses and mock payment system
- Clean backend architecture

---

## 🚀 Features

### 🌐 Public
- Homepage, About, Pricing, FAQ, Contact
- Public shipment tracking

### 👤 Client
- Create shipments
- Track and chat per shipment
- Saved addresses
- Mock payment methods

### 🏢 Company
- Accept/reject shipments
- Update delivery status
- Chat with clients

### 🛠️ Admin
- Full system management
- View statistics and chats

---

## 🧱 Tech Stack
- Flask, SQLAlchemy, Flask-Migrate
- HTML, Bootstrap, Jinja2
- SQLite / PostgreSQL

---

## 🧭 System Roles Diagram

```
Admin
 │
 ├── manages ──► Users
 │
 ├── manages ──► Companies
 │
 └── monitors ─► Shipments & Chats

Client ◄──────────► Company
        Shipments & Chat
```

---

## 🛠️ Installation

```bash
git clone https://github.com/EsmoAghamedova/Trackify
cd trackify
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db migrate
flask db upgrade
flask run
```

---

## 📝 Academic Note
Developed for **GeoLab / TechSchool** educational purposes.

---

🚀 Trackify — Smart logistics, simplified.
