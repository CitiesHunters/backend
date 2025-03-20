from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def add_middleware(app : FastAPI):
    """
    Add middleware to FastAPI app
    
    Gestione dei CORS, da cambiare sicuramente per la 
    production, ma intanto mettiamo tutto aperto
    """

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],        
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],

)