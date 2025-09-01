TaskForge
TaskForge is a scalable, microservices-based task management platform built with Django, PostgreSQL, Redis, Celery, RabbitMQ, and Docker. It supports user authentication, project/task management, real-time updates, and background processing.
Setup Instructions

Clone the repository:
git clone <repository-url>
cd taskforge


Set up environment variables:Create a .env file in auth_service/:
DJANGO_SECRET_KEY=your-secret-key-here
POSTGRES_DB=auth_db
POSTGRES_USER=auth_user
POSTGRES_PASSWORD=auth_password
POSTGRES_HOST=postgres
DEBUG=True


Run with Docker Compose:
docker-compose up --build


Apply migrations:
docker-compose exec auth_service python manage.py migrate


Access the service:

Auth Service: http://localhost:8000
RabbitMQ Management: http://localhost:15672 (user: guest, password: guest)



Project Structure

auth_service/: Handles user authentication and registration.
More services (e.g., Project, Notification) to be added.

Technologies

Django, Django REST Framework
PostgreSQL, Redis, RabbitMQ
Celery for async tasks
Docker for containerization

