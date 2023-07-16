from fastapi import FastAPI
from api.utils.dbUtils import database
from api.auth import router as auth_router
app=FastAPI(title="fastapi-docker",
            description="fastAPI fast and secure",
            version="1.0",
            docs_url="/docs",
            openapi_url="/openapi.json",
            redoc_url="/redocs"
            )


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(auth_router.router,tags=["Auth"])