import streamlit as st

st.set_page_config(
    page_title="Bulk SMS API",
    page_icon="📩",
    layout="wide"
)

st.title("Bulk SMS API")

st.markdown("""
A practical guide explaining how developers and businesses use a **Bulk SMS API** to integrate messaging into websites, mobile applications, CRM platforms, ERP systems, and enterprise software.

[Bulk SMS API](https://nigeriasms.net/services/bulk-sms) allow organizations to automate customer communication including notifications, OTP verification, appointment reminders, payment confirmations, delivery updates, and marketing campaigns.

---

## Why Use a Bulk SMS API

- Promotional SMS campaigns
- Transactional notifications
- OTP verification
- Appointment reminders
- Payment alerts
- Delivery tracking
- Marketing automation
- Customer support

---

## Key Features

- REST API Integration
- High-speed SMS Delivery
- JSON Requests
- Delivery Reports
- Secure Authentication
- Scalable Infrastructure
- Enterprise Ready

---

## Typical Workflow

```text
Website / Mobile App
        │
        ▼
Business Server
        │
        ▼
Bulk SMS API
        │
        ▼
SMS Gateway
        │
        ▼
Customer Mobile
        {
  "recipient": "+2348012345678",
  "sender": "Business",
  "message": "Welcome to our platform."
}
            POST /api/send-sms HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
  "recipient": "2348012345678",
  "message": "Welcome to our platform."
}
            Business Applications
Banking
FinTech
E-commerce
Healthcare
Education
Logistics
SaaS
Government
Bulk SMS API Resource

Businesses looking for enterprise messaging infrastructure can explore Bulk SMS API.

The platform provides REST API integration, promotional SMS, transactional messaging, OTP delivery, delivery reports, and scalable messaging infrastructure for businesses of every size.
""")