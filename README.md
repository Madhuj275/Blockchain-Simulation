
# BLOCKCHAIN SIMULATOR

A full-stack blockchain implementation with Django backend and React frontend, demonstrating core blockchain concepts including Proof-of-Work, hashing, and tamper detection.


## Features

### Blockchain Core
- Secure block creation with cryptographic hashing (SHA-256)
- Proof-of-Work consensus algorithm
- Tamper-evident chain validation
- Genesis block initialization
- Transaction recording system

### Frontend Visualization
- Interactive blockchain explorer
- Real-time block visualization
- Transaction submission form
- Tamper demonstration interface
- Chain validation status indicator

### Backend API
- RESTful endpoints for blockchain operations
- PostgreSQL database integration
- Django admin interface
- Secure API authentication
- Data serialization

## Tech Stack

### Frontend
- React.js
- Axios for API calls
- CSS3 with modern styling
- Responsive design
- Nginx web server

### Backend
- Django REST Framework
- PostgreSQL database
- Gunicorn production server
- Python cryptography
- Docker containerization

## Prerequisites

Before you begin, ensure you have installed:
- Docker Desktop 
- Node.js (v18 or higher)
- Python 3.9+

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/blockchain-simulation.git
cd blockchain-simulation
```

2. Set up environment variables:
Create `.env` file in project root:
```ini
# Django
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=0

# Database
DB_NAME=blockchain
DB_USER=blockchain
DB_PASSWORD=blockchain
DB_HOST=db
DB_PORT=5432
```

3. Build and run with Docker:
```bash
docker-compose up --build
```

4. Initialize the database:
```bash
docker-compose exec backend python manage.py migrate
```

## Running the Application

1. Start all services:
```bash
docker-compose up
```

2. Access the application:
- Frontend: http://localhost
- Backend API: http://localhost:8000/api
- Admin Panel: http://localhost:8000/admin

3. Create admin user (optional):
```bash
docker-compose exec backend python manage.py createsuperuser
```


![image](https://github.com/user-attachments/assets/d1a4a11f-923b-45ba-b9f9-dee09980144c)



