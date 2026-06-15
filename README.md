# Automation Backend - Django REST API

Automation Backend is a Django REST API that handles automation requests with end-to-end lifecycle tracking, error handling, and service-layer business logic separation.
The system is designed to simulate real-world backend workflows where requests are created, processed asynchronously via Celery, and tracked through clear status transitions.
This project showcases production-ready backend practices using Django and Django REST Framework.

## Tech Stack:
Python, Django, DRF, PostgreSQL, REST APIs, JWT Authentication, JSON Processing, Redis, Celery, Docker & Docker Compose

## Request Lifecycle:
PENDING → PROCESSING → COMPLETED or FAILED

## API Endpoints:
=====Register=====
POST /api/register/
Body: { "username": "your_username", "password": "your_password" }

Response: { "message": "User registered successfully." }


=====Get JWT tokens=====
POST /api/token/
Body:{ "username": "your_username", "password": "your_password" }

Response:{ "refresh": "token", "access": "token" }


=====Create Request=====
POST /api/requests/

Request Body:{
  "request_type": "summary",
  "payload": {
    "name": "Sample",
    "value": 10
  }
}

Expected Response:{"request_id": "uuid","status": "PENDING"}

=====Get Request=====
GET /requests/<request_id>/
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
- JWT protected endpoints
- Async processing via Celery and Redis
- Service-layer for business logic
- JSONField support for dynamic payloads
- Safe status transitions with error persistence
- Clean separation of models, serializers, services, views and tasks

## ## Clone Repository & Run locally with Docker:
git clone https://github.com/vamshikrishna-piska/automation-backend.git
cd automation-backend
cp .env.example .env 
docker-compose up --build

API will be available at http://localhost:8000

Thank you!
Vamshi Krishna Piska
Backend Developer | Python | Django | REST APIs | Automation
