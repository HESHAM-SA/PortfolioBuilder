# 🚀 Portfolio Builder

A frictionless, no-authentication timeline portfolio generator built with Django. This application allows users to instantly create, edit, and share a beautiful, interactive career timeline without the need for registration or passwords.

<div align="center">

[![Live Demo](https://img.shields.io/badge/Live_Demo-View_Project-brightgreen?style=for-the-badge&logo=rocket)](https://portfoliobuilder-production.up.railway.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

![Public Portfolio Wireframe](/PortfolioBuilder/assets/images/rea-land-page.png)

---

## ✨ Key Features

*   **Zero-Friction Start:** Go from landing page to a shareable portfolio in under a minute. No signup required.
*   **Session-Based Management:** Securely edit your portfolio using a unique, private link tied to your browser session. No passwords to remember.
*   **Interactive Timeline:** A visually engaging, centered timeline that groups events by year and allows for nested expansion of details.
*   **Rich Content Integration:** Enhance your timeline by uploading a profile picture and embedding images or YouTube videos for each event.
*   **Instantly Shareable:** Every portfolio receives a unique, public URL perfect for sharing with recruiters, clients, or colleagues.
*   **Clean & Responsive UI:** Built with Bootstrap 5 for a modern, mobile-first design that looks great on any device.

---

## 🎯 How It Works

This project is designed with two primary user experiences in mind: the creator building their portfolio and the visitor (like a recruiter) viewing it.

### For the Portfolio Creator:
*   **Instantly Create:** Start building your portfolio directly from the landing page by entering your name and title.
*   **Build Your Profile:** Add a detailed bio, contact email, and a link to your LinkedIn profile to create a complete professional identity.
*   **Personalize:** Upload a professional profile picture to make your portfolio stand out.
*   **Document Your Journey:** Add individual events (work experience, education, projects) to build a comprehensive career timeline.
*   **Showcase Your Work:** Attach images and embed YouTube videos to provide visual proof of your accomplishments.
*   **Stay Updated:** Easily edit and delete timeline events from your private dashboard to keep your history accurate.
*   **Secure & Simple Access:** Use your secret dashboard link to manage your portfolio anytime, without the hassle of a login system.

### For the Public Visitor (e.g., a Recruiter):
*   **Visually Impressive:** The creator's profile picture is used as a personalized, full-page background for a unique first impression.
*   **Easy Navigation:** A clean, centered timeline with clearly marked years allows for a quick grasp of a candidate's career span.
*   **Scan & Dive Deep:** Click a year to see event titles, then click a specific title to expand its full details, images, and videos.
*   **Fully Responsive:** The portfolio is designed to be perfectly readable and navigable on any device, from desktop to mobile.
*   **Clear Calls-to-Action:** Easily find links to the creator's email and professional profiles to take the next step.

---

## 🛠️ Technology Stack

*   **Backend:** Django 5, Python 3
*   **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
*   **Database:** SQLite3 (default for development)
*   **Image Handling:** Pillow

---

## ⚙️ Local Setup and Installation

Follow these steps to get the project running on your local machine for development and testing purposes.

### Prerequisites
*   Python 3.8+
*   `pip` (Python package manager)

### Installation Guide

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/HESHAM-SA/PortfolioBuilder.git
    cd portfolio-builder-project
    ```

2.  **Create and activate a virtual environment:**
    *   On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If a `requirements.txt` file is not present, you can generate one in your own project with `pip freeze > requirements.txt`)*

4.  **Apply database migrations:**
    This command creates the necessary database tables based on the Django models.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will now be accessible at `http://127.0.0.1:8000/`.

---

## 📊 System Design & Architecture

### UML Class Diagram
This diagram illustrates the relationship between the `Portfolio` and `TimelineEvent` models.

*   **[View UML Class Diagram (PDF)](/assets/pdfs/UML%20Digram.pdf)**
*   ![UML Class Diagram](/PortfolioBuilder/assets/images/UML%20Digram-1.jpg)

### Sequence Diagrams
These diagrams outline the user flow for key system interactions.

1.  **Create a New Portfolio**
    *   **[View Sequence Diagram (PDF)](/assets/pdfs/1.%20Sequence%20Diagram%20Create%20a%20New%20Portfolio.pdf)**
    *   ![Create a New Portfolio Sequence Diagram](/PortfolioBuilder/assets/images/1.%20Sequence%20Diagram%20Create%20a%20New%20Portfolio-1.jpg)

2.  **Add a Timeline Event with an Image**
    *   **[View Sequence Diagram (PDF)](/assets/pdfs/2.%20Sequence%20Diagram%20Add%20a%20Timeline%20Event%20with%20an%20Image.pdf)**
    *   ![Add an Event Sequence Diagram](/PortfolioBuilder/assets/images/2.%20Sequence%20Diagram%20Add%20a%20Timeline%20Event%20with%20an%20Image-1.jpg)

### Page Wireframes
Visual blueprints for the application's key pages.

| Landing Page | Portfolio Dashboard | Add/Edit Event Form |
| :---: | :---: | :---: |
| ![Landing Page Wireframe](/PortfolioBuilder/assets/images/wireframe-landing.png) | ![Dashboard Wireframe](/PortfolioBuilder/assets/images/wireframe-dashboard.png) | ![Add/Edit Event Wireframe](/PortfolioBuilder/assets/images/wireframe-event-form.png) |

| Edit Profile Form | Public Portfolio Page |
| :---: | :---: |
| ![Edit Profile Wireframe](/PortfolioBuilder/assets/images/wireframe-profile-form.png) | ![Public Portfolio Wireframe](/PortfolioBuilder/assets/images/wireframe-public-portfolio.png) |

---

## 🔮 Future Enhancements

*   **Custom Themes:** Allow users to choose from different color schemes and timeline layouts.
*   **Simple Analytics:** Provide view counts for public portfolios.
*   **Data Export:** Enable users to export their portfolio data as a JSON or PDF file.
*   **Optional Authentication:** Add an option to link a portfolio to a permanent user account for easier management across devices.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE.md` file for details.
