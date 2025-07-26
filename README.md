# 🚀 Portfolio Builder

A frictionless, no-authentication timeline portfolio generator built with Django. This application allows users to instantly create, edit, and share a beautiful, interactive career timeline without the need for registration or passwords.

---

## ✨ Key Features

*   **Instant Portfolio Creation:** Go from landing page to a shareable portfolio in under a minute. No signup required.
*   **Session-Based Editing:** Securely edit your portfolio using your browser session. Just bookmark your unique edit link.
*   **Interactive Centered Timeline:** A visually engaging, responsive timeline that groups events by year and allows for nested expansion of details.
*   **Rich Content Uploads:** Add a profile picture and include images or embed YouTube videos for each timeline event.
*   **Dynamic and Shareable:** Every portfolio gets a unique, public URL that can be shared with recruiters, clients, or colleagues.
*   **Simple & Clean UI:** Built with Bootstrap 5 for a modern, responsive, and mobile-first design.

---

## 🛠️ Technology Stack

*   **Backend:** Django 5, Python 3
*   **Frontend:** HTML5, CSS3, Bootstrap 5
*   **Database:** SQLite3 (default for development)
*   **Image Processing:** Pillow

---

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### Prerequisites

*   Python 3.8+
*   `pip` package manager

### Installation Guide

1.  **Clone the repository:**
    ```bash
    git clone https://your-repository-url.com/
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

3.  **Install the required packages:**
    (First, ensure you have a `requirements.txt` file by running `pip freeze > requirements.txt` in your project's terminal)
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    This will create the database schema based on the models.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The application will now be running at `http://127.0.0.1:8000/`.

---

## 📊 Project Structure & Diagrams

### UML Class Diagram

This diagram shows the relationship between the `Portfolio` and `TimelineEvent` models in the database.

*   **[View UML Class Diagram (PDF)](/assets/pdfs/UML%20Digram.pdf)**
    *(Note: For a direct view, convert the PDF to a PNG or JPG and use the image tag below.)*
*   `![UML Class Diagram](/assets/images/UML%20Digram-1.jpg)`

### User Story & Sequence Diagrams

These documents outline the intended user flow and interactions within the system.

1.  **[View User Story Flow (PDF)](/assets/pdfs/1.%20Sequence%20Diagram%20Create%20a%20New%20Portfolio.pdf)**
*   `![View User Story Flow](/assets/images/1.%20Sequence%20Diagram%20Create%20a%20New%20Portfolio-1.jpg)`

2.  **[View Sequence Diagram (PDF)](/assets/pdfs/2.%20Sequence%20Diagram%20Add%20a%20Timeline%20Event%20with%20an%20Image.pdf)**
*   `![View Sequence Diagram](/assets/images/2.%20Sequence%20Diagram%20Add%20a%20Timeline%20Event%20with%20an%20Image-1.jpg)`


### Page Wireframes

Here are the visual blueprints for the key pages in the application.

#### 1. Landing Page
*   ![landing page](/assets/images/wireframe-landing.png)

#### 2. Portfolio Dashboard
*   ![Dashboard Wireframe](/assets/images/wireframe-dashboard.png)

#### 3. Add/Edit Event Page
*   ![Add/Edit Event Wireframe](/assets/images/wireframe-event-form.png)

#### 4. Edit Profile Page
*   ![Edit Profile Wireframe](/assets/images/wireframe-profile-form.png)

#### 5. Public Portfolio Page
*   ![Public Portfolio Wireframe](/assets/images/wireframe-public-portfolio.png)

---

## 🔮 Future Enhancements

*   **Custom Themes:** Allow users to choose from different color schemes and timeline layouts.
*   **Analytics:** Provide simple view counts for public portfolios.
*   **Data Export:** Enable users to export their portfolio data as a JSON or PDF file.
*   **Optional Authentication:** Add an option to link a portfolio to a permanent user account.

---

## 📄 License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
