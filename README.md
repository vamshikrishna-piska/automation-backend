# Automation Backend - Django REST API

Automation Backend is a Django REST API that handles automation requests with end-to-end lifecycle tracking, error handling, and service-layer business logic separation.
The system is designed to simulate real-world backend processing workflows, where requests are created, processed, and tracked asynchronously-ready with clear status transitions.
This project showcases production-ready backend practices using Django and Django REST Framework.

## Tech Stack:
Python, Django, DRF, PostgreSQL, REST APIs, JSON Processing
## Request Lifecycle:
PENDING → PROCESSING → COMPLETED or FAILED

## API Endpoints:
=====Create Request=====
POST /requests/

Request Body:{
  "request_type": "summary",
  "payload": {
    "name": "Sample",
    "value": 10
  }
}

Expected Response:201 Created-{
  "request_id": "uuid",
  "status": "COMPLETED",
  "preview": {
    "summary": {
      "name": "Sample",
      "value": 10
    },
    "field_count": 2
  }
}

=====Get Request=====
GET /requests/<uuid>/
{
  "request_id": "uuid",
  "request_type": "summary",
  "status": "COMPLETED",
  "error_message": null,
  "created_at": Timestamp,
  "updated_at": Timestamp
}

## Design:
- UUID-based request tracking
- Service-layer for business logic
- JSONField support for dynamic payloads
- Safe status transitions with error persistence
- Clean separation of models, serializers, services, and views

## Desined for easy extention:
- External API calls, Data validation or Background jobs like Celery / Redis

## Clone Repository
- git clone https://github.com/vamshikrishna-piska/automation-backend.git
- cd automation-backend

Thank you!
Vamshi Krishna Piska
Backend Developer | Python | Django | REST APIs | Automation
