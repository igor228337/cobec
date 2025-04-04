from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin
import uvicorn
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.admin.historys import RequestHistoryAdmin
from src.enviroment import enviroment
from src.utils.auth_admin import BasicAuthBackend
from src.db.db import engine
from src.api.routers import all_routers


app = FastAPI(title="Cobec", forwarded_allow_ips="*", proxy_headers=True)
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

authentication_backend = BasicAuthBackend(secret_key=enviroment.ADMIN_KEY)
admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(RequestHistoryAdmin)


for router in all_routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        forwarded_allow_ips="*",
        proxy_headers=True,
        reload=True,
        loop="uvloop"
    )