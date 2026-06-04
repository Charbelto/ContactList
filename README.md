# ContactList: Simple Contacts Directory Manager

ContactList is a simple, lightweight Django web application designed for storing and managing a directory list of personal and professional contacts. The application demonstrates standard CRUD (Create, Read, Update, Delete) database operations using Django’s Model-View-Template (MVT) architecture and a SQLite relational backend.

---

## 📋 Table of Contents
1. [Core Features](#-core-features)
2. [Tech Stack](#-tech-stack)
3. [Database Model](#-database-model)
4. [Routing & Views](#-routing--views)
5. [Installation & Setup](#-installation--setup)

---

## 🎯 Core Features
*   **Contacts Directory Listing**: Display all contacts in a clean tabular view.
*   **Create Contacts**: Add new contacts using validation forms.
*   **Edit/Update Details**: Modify existing fields (address, profession, email, phone) dynamically.
*   **Delete Entries**: Instantly remove contact records from the database directory.
*   **Model Validation**: Built-in validation checks for email fields and integer-only fields for phone numbers.

---

## 💻 Tech Stack
*   **Frontend**: HTML5, Bootstrap CSS
*   **Backend**: Django (Python web framework)
*   **Database**: SQLite3

---

## 🗄 Database Model

The relational schema maps to a single model:

### `Contact`
*   `name`: CharField (max_length=100) — Name of the contact.
*   `address`: CharField (max_length=200) — Location or street address.
*   `profession`: CharField (max_length=100) — Job title or industry.
*   `phone`: IntegerField — Main phone number contact.
*   `email`: EmailField — validated email address.

---

## 🛠 Routing & Views

The application implements four views in `mycontacts/views.py`:
*   **`index`** (`/`): Queries all contact records and renders `index.html`.
*   **`add_contact`** (`/add/`): Renders the contact creation form; handles POST data to validate and save.
*   **`edit_contact`** (`/edit/<int:pk>/`): Retrieves a contact by primary key and updates it.
*   **`delete_contact`** (`/delete/<int:pk>/`): Removes a contact by primary key and redirects.

---

## 🚀 Installation & Setup

### Prerequisites
*   Python 3.8+

### 1. Setup Environment
```bash
cd github_repos/ContactList

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install Django and dependencies
pip install -r requirements.txt
```

### 2. Apply Migrations & Start Server
Apply database migrations to set up the SQLite schema:
```bash
# Run database migrations
python manage.py migrate

# Start the Django development server
python manage.py runserver
```
The application will run on `http://127.0.0.1:8000/`.
Open your browser and navigate to the link to start managing your contacts!
