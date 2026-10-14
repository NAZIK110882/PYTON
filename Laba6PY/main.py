from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import auth_router, items_router

# Створення таблиць у БД
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lab 6 API", description="Basic REST API with Authentication")

# Налаштування CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшені варто вказувати конкретні домени
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Підключення роутерів
app.include_router(auth_router.router)
app.include_router(items_router.router)

@app.get("/")
def root():
    return {"message": "Welcome to Lab 6 API! Go to /docs for Swagger UI"}