🖥️ Table Booking Backend (FastAPI)

This is a lightweight FastAPI backend service for handling table booking submissions. It is a part of [TheGreenSprout - A small restaurant website](https://github.com/Tushar-Metrani/greensprout). It exposes a  POST endpoint /submit that accepts form data and sends a booking confirmation email to users via the Brevo API.

---

## 📌 Use Case

- This service is meant to power the table booking form on the [TheGreenSprout](https://github.com/Tushar-Metrani/greensprout) website. When a user fills out the booking form, the data is sent to this backend, which:

- Accepts the form data

- Sends a confirmation email using Brevo

- Responds with success or error status

---

## 🐍 Tech Stack

- Python

- FastAPI – Modern, fast web framework

- Brevo API – For sending transactional emails

---

## 🛠️ Setup & Run Instructions

Follow these steps to get the Python backend running locally:

1. Clone the repo:

```bash
git clone https://github.com/tushar-metrani/book-table-fastapi.git
cd book-table-fastapi
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Brevo setup:

- create template

- In the payload structure, you'll see the following line:

`"templateId": 1,`

* replace 1 with your own email template ID.

* Make sure the keys in "params" match the placeholders in your template.

4. Configure `.env` file with your Brevo API key and sender email:

```env

BREVO_API_KEY=your_brevo_api_key_here

EMAIL=your_email_connected_with_brevo_here

```

5. Run the app:

```bash
uvicorn main:app --reload
```

---

## 🚀 Endpoint Summary

### `POST /submit`

Accepts booking form data via POST request (form data) and sends a confirmation email.

---
