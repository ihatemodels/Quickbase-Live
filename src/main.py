from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from prometheus_client import make_asgi_app

app = FastAPI()
metrics_app = make_asgi_app()


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

app.mount("/metrics", metrics_app, name="metrics")
app.mount("/", StaticFiles(directory="/app/src/static", html=True), name="static")
