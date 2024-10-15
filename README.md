# Video List API

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)

## Table of Contents
- [Project Description](#project-description)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [API Endpoint](#api-endpoint)

## Project Description

This project is a simple Django-based API that provides a list view for videos. Users can retrieve a paginated list of videos, which includes details such as the video URL, thumbnail, description, view count, user information, associated products, likes, and more.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- PostgreSQL (or another database of your choice)
- Docker (for Redis)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sasha643/Attyre_Backend_Assignment.git
   cd Attyre_Backend_Assignment
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
   
5. **Set up your database:**

   - Create a PostgreSQL database.
   - Update the database settings in `settings.py` with your database credentials.

6. **Run migrations:**

   ```bash
   python manage.py migrate
   ```
   
7. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

8. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

### Running the Project

8. **Run Redis in Docker (Make sure Docker is installed and running, then run the following command to start Redis):**

   ```bash
   docker run -d -p 6379:6379 redis
   ```
