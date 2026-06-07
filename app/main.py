from fastapi import FastAPI

from app.routers import posts, users


app = FastAPI(title="Social Media API", version="1.0.0")
app.include_router(users.router)
app.include_router(posts.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
