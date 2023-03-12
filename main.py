# main rounter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import chatgpt_api

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

app.include_router(chatgpt_api.router)
