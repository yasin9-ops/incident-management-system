# Incident Management System (IMS)

## Overview

This project is a scalable Incident Management System designed to handle high-throughput signal ingestion and manage incidents efficiently using modern SRE principles.

---

## Tech Stack

* FastAPI (Backend)
* PostgreSQL (Work Items - Source of Truth)
* MongoDB (Raw Signals - Audit Log)
* Redis (Caching Layer)
* Docker (Containerization)

---

## Architecture

User → FastAPI → Background Worker → Services Layer
↓
MongoDB | PostgreSQL | Redis

---

## Features

### High Throughput Ingestion

Handles multiple incoming signals using async processing.

### Debouncing Logic

Groups multiple signals (within 10 seconds) into a single incident.

### Incident Lifecycle

OPEN → INVESTIGATING → RESOLVED → CLOSED

### Mandatory RCA

Incident cannot be closed without Root Cause Analysis.

### Rate Limiting

Prevents system overload using request throttling.

### Caching

Redis used to optimize dashboard performance.

---

## How to Run

```bash
docker compose up --build
```

Then initialize database:

```bash
docker exec -it ims_backend python -m app.init_db
```


## if, To run the backend 
python -m uvicorn app.main:app --reload
---

## API Endpoints

* POST /signals
* GET /incidents
* POST /incident/{component_id}/status

---

## GitHub Link

https://github.com/yasin9-ops/incident-management-system


Backpressure Handling:
The system handles high-throughput signal ingestion using asynchronous background processing and rate limiting. This ensures that incoming traffic does not overwhelm the persistence layer, and the system remains stable under burst conditions.


Future Improvements:
- Kafka for event streaming
- Prometheus + Grafana for monitoring
- Kubernetes deployment


Design Patterns Used:

1. State Pattern:
Incident lifecycle (OPEN → CLOSED) is managed through controlled transitions.

2. Strategy Pattern:
Alerting and processing logic can be extended dynamically based on component severity.


Retry Logic:
Database operations can be extended with retry mechanisms to handle transient failures.