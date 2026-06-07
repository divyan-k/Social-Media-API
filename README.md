# Social Media API

A small RESTful social media API built with FastAPI, SQLAlchemy, Alembic, and JWT authentication.

## Features

- User registration
- User login with JWT access tokens
- Current user lookup
- Create posts
- List posts
- Fetch a single post
- Delete your own posts
- Auto-generated API docs

## Tech Stack

- FastAPI
- SQLAlchemy
- Alembic
- SQLite for local development
- PostgreSQL-ready database configuration
- `python-jose` for JWT handling
- `passlib` with bcrypt for password hashing

## Project Structure

```text
app/
  __init__.py
  auth.py
  database.py
  main.py
  models.py
  schemas.py
  routers/
    __init__.py
    posts.py
    users.py
alembic/
  env.py
  script.py.mako
  versions/
```

## Setup

1. Create a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy the sample environment file if needed:

   ```bash
   copy .env.example .env
   ```

4. Run the database migration:

   ```bash
   alembic upgrade head
   ```

5. Start the app:

   ```bash
   uvicorn app.main:app --reload
   ```

## Environment Variables

The app uses these values from `.env`:

```env
DATABASE_URL=sqlite:///./social.db
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## API Endpoints

| Method | Path | Auth | Description |
|---|---|---|---|
| GET | `/health` | No | Health check |
| POST | `/auth/register` | No | Create account |
| POST | `/auth/login` | No | Get JWT token |
| GET | `/auth/me` | Yes | Get current user |
| POST | `/posts/` | Yes | Create a post |
| GET | `/posts/` | No | List posts |
| GET | `/posts/{post_id}` | No | Get one post |
| DELETE | `/posts/{post_id}` | Yes | Delete your own post |

## Example Requests

### Register

```http
POST /auth/register
Content-Type: application/json

{
  "username": "alice",
  "email": "alice@example.com",
  "password": "password123"
}
```

### Login

```http
POST /auth/login
Content-Type: application/x-www-form-urlencoded

username=alice&password=password123
```

### Create a Post

```http
POST /posts/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "title": "Hello World",
  "content": "My first post"
}
```

## Docs

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Notes

- `.env` is ignored by git.
- Local SQLite data is stored in `social.db`.
- To switch to PostgreSQL later, update `DATABASE_URL` in `.env`.
