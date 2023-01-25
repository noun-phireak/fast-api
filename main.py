import uvicorn
from fastapi import FastAPI
from routers.api_v1.api import router
from fastapi.middleware.cors import CORSMiddleware
# import dotenv
# dotenv.load_dotenv()
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8005, log_level="info", reload=True)

