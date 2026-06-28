# Decoupled Full-Stack E-Commerce Catalog

A modern, production-ready decoupled application featuring a lightweight vanilla JavaScript user interface consuming data feeds from a secure Django REST Framework API engine.

## 🛠️ Technology Stack
- **Frontend Client:** HTML5, CSS3 (Custom Design Tokens), JavaScript Fetch API
- **Backend Service:** Python, Django REST Framework, Object-Relational Mapping (ORM)
- **Database Engine:** SQLite (Relational Storage)
- **Version Control & Security:** Git, GitHub, `.gitignore` Environment Shields

## 🔒 Security Features
- **IsAuthenticatedOrReadOnly Boundary:** The public storefront consumes generic `GET` requests seamlessly while critical write-level actions (`POST`, `PUT`, `DELETE`) are tightly locked behind admin credentials.
- **Enterprise Console Integration:** Includes out-of-the-box Django Admin Panel integration for graphical inventory and superuser management.
