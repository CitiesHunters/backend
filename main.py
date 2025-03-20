from fastapi import FastAPI
from app.core.middleware import add_middleware
from app.routers.auth import authentication_router
from app.routers.user import user_router

app = FastAPI(
    openapi_tags=[
        {
            "name": "Authentication",
            "description": "Endpoints per l'autenticazione degli utenti",
        },
        {
            "name": "Users",
            "description": "Endpoints per la gestione generica degli utenti",
        },

    ],
)


app = FastAPI()
add_middleware(app)
app.include_router(authentication_router)
app.include_router(user_router)



