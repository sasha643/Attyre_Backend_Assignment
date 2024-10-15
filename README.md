# Video List API

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)

## Table of Contents
- [Project Description](#project-description)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [API Endpoint](#api-endpoint)
- [API Example](#api-example)

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

1. **Run Redis in Docker (Make sure Docker is installed and running, then run the following command to start Redis):**

   ```bash
   docker run -d -p 6379:6379 redis
   ```

2. **Start the Django development server:**

   ```bash
   python manage.py runserver
   ```

3. **Access the API:**

   - Open your browser and go to [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/) to access the API.


### API Endpoint

- GET /videos/ - Retrieves a paginated list of videos.

## API Example:

### Request

**GET** `http://127.0.0.1:8000/videos/?limit=10&page=1`

### Response

```json
{
  "videos": [
    {
      "id": 1,
      "video_url": "https://example.com/video1.mp4",
      "thumbnail_url": "https://example.com/thumbnail1.jpg",
      "description": "A great video about something interesting.",
      "view_count": 1000,
      "duration": 300,
      "created_at": "2024-10-15T12:00:00Z",
      "user": {
        "id": 1,
        "username": "john_doe",
        "display_name": "John Doe",
        "profile_picture_url": "https://example.com/profile.jpg",
        "bio": "Just a guy who likes making videos.",
        "followers_count": 150,
        "verified": true
      },
      "products": [
        {
          "id": 1,
          "name": "Cool Product",
          "price": 29.99,
          "original_price": 39.99,
          "discount_percentage": 25.0,
          "image_url": "https://example.com/product.jpg",
          "timestamp": "2024-10-10T12:00:00Z",
          "currency": "USD",
          "in_stock": true,
          "store": {
            "id": 1,
            "name": "Awesome Store",
            "logo_url": "https://example.com/store_logo.jpg"
          },
          "variants": [
            {
              "id": 1,
              "name": "Size",
              "options": ["S", "M", "L"]
            }
          ]
        }
      ],
      "likes_count": 150,
      "comments_count": 20,
      "shares_count": 5,
      "is_liked": true,
      "is_bookmarked": false,
      "music": {
        "id": 1,
        "name": "Cool Song",
        "artist": "Cool Artist",
        "cover_url": "https://example.com/album_cover.jpg"
      },
      "hashtags": ["cool", "video", "entertainment"]
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total_pages": 5,
    "total_videos": 50,
    "next_cursor": "http://127.0.0.1:8000/videos/?limit=10&page=2"
  }
}
