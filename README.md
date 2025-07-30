# 🚀 Portfolio Builder

A frictionless, no-authentication timeline portfolio generator built with Django. This application allows users to instantly create, edit, and share a beautiful, interactive career timeline — no registration or passwords needed.

[![Live Demo](https://img.shields.io/badge/Live_Demo-View_Project-brightgreen?style=for-the-badge)](https://portfoliobuilder-production.up.railway.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

![Public Portfolio Wireframe](/assets/images/wireframe-public-portfolio.png)

---

## ✨ Key Features

* **Zero-Friction Start:** Go from landing page to a shareable portfolio in under a minute. No signup required.
* **Session-Based Management:** Securely edit your portfolio using a unique, private link tied to your browser session.
* **Interactive Timeline:** A clean, centered timeline grouped by year with expandable nested event details.
* **Rich Content Integration:** Upload a profile picture and add images or YouTube videos to each timeline event.
* **Instant Sharing:** Each portfolio gets a public URL ideal for recruiters, clients, or social links.
* **Responsive & Clean UI:** Built with Bootstrap 5 for a mobile-first, modern design.

---

## 🎯 How It Works

The experience is tailored for both portfolio creators and public viewers like recruiters.

### For Portfolio Creators

* **Instant Creation:** Start building directly from the landing page by entering your name and title.
* **Complete Your Profile:** Add a bio, contact email, and LinkedIn link.
* **Personalize:** Upload a profile picture to create a professional identity.
* **Build Your Timeline:** Add work, education, or project events with descriptions.
* **Showcase Your Work:** Embed images and YouTube videos for each event.
* **Keep It Updated:** Edit and delete events anytime using your private dashboard link.
* **Simple Access:** No login needed — just save your unique dashboard URL.

### For Public Visitors (e.g., Recruiters)

* **Strong First Impression:** The creator’s profile picture appears as a full-page background.
* **Efficient Navigation:** Expandable timeline organized by year for quick browsing.
* **Dive into Details:** Click years and event titles to reveal full content and media.
* **Device Friendly:** Optimized for all screen sizes.
* **Quick Contact:** Email and LinkedIn links are easy to find.

---

## 🛠️ Technology Stack

* **Backend:** Django 5, Python 3
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
* **Database:** SQLite3 (default for development)
* **Image Handling:** Pillow

---

## ⚙️ Installation

Get the project running locally by following these steps:

### Prerequisites

* Python 3.8+
* `pip` installed

### Setup Guide

```bash
# Clone the repository
git clone https://github.com/your-username/portfolio-builder.git
cd portfolio-builder

# Create and activate a virtual environment
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Access the app at: `http://127.0.0.1:8000/`

---

## 📊 System Design & Architecture

### UML Class Diagram

Relationship between `Portfolio` and `TimelineEvent` models:

* 📄 [View UML Class Diagram (PDF)](/assets/pdfs/UML%20Diagram.pdf)
* ![UML Class Diagram](/assets/images/UML%20Diagram-1.jpg)

### Sequence Diagrams

1. **Create a New Portfolio**
   [PDF](/assets/pdfs/1.%20Sequence%20Diagram%20Create%20a%20New%20Portfolio.pdf)
   ![](/assets/images/1.%20Sequence%20Diagram%20Create%20a%20New%20Portfolio-1.jpg)

2. **Add Timeline Event with Image**
   [PDF](/assets/pdfs/2.%20Sequence%20Diagram%20Add%20a%20Timeline%20Event%20with%20an%20Image.pdf)
   ![](/assets/images/2.%20Sequence%20Diagram%20Add%20a%20Timeline%20Event%20with%20an%20Image-1.jpg)

### Wireframes

|                Landing Page               |                  Dashboard                  |                Add/Edit Event                |
| :---------------------------------------: | :-----------------------------------------: | :------------------------------------------: |
| ![](/assets/images/wireframe-landing.png) | ![](/assets/images/wireframe-dashboard.png) | ![](/assets/images/wireframe-event-form.png) |

|                  Edit Profile                  |                  Public Portfolio                  |
| :--------------------------------------------: | :------------------------------------------------: |
| ![](/assets/images/wireframe-profile-form.png) | ![](/assets/images/wireframe-public-portfolio.png) |

---

## 🔮 Future Enhancements

* 🎨 Theme Customization
* 📊 Simple Analytics (view count)
* 🧾 Export Portfolio (PDF/JSON)
* 🔐 Optional Authentication for long-term access

---

## 🔗 Live Website

👉 [https://portfoliobuilder-production.up.railway.app/](https://portfoliobuilder-production.up.railway.app/)

---

## 📄 License

This project is licensed under the MIT License. See [`LICENSE.md`](LICENSE.md) for details.