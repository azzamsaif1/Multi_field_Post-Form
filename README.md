# Multi-Field HTTP Form (Raw Socket)

This project demonstrates how to build a raw HTTP server using Python sockets  
that accepts and processes a form with **multiple fields**: name, age, and email.

---

## Features

- Accepts HTTP `POST` requests
- Parses multiple fields manually from the raw HTTP body
- Displays the submitted data dynamically in the response HTML

---

## How it works

1. User opens the form in browser (`GET /`)
2. User fills in name, age, email and submits (`POST /`)
3. Server:
   - Parses the HTTP body (e.g. `name=Azzam&age=25&email=azzam@mail.com`)
   - Splits by `&`, then by `=`, then decodes values
   - Renders a custom HTML response showing the values

---

## Technologies

- Python 3
- socket
- Basic HTML (embedded)

---

## Sample Usage

```bash
python multi_field_http_form.py
