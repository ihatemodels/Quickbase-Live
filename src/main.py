from datetime import datetime

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from prometheus_client import generate_latest
from starlette.status import HTTP_404_NOT_FOUND

from responses import HealthzResponse, HireMeResponse

# Get the start time when the application initializes
start_time = datetime.now()

SITE_VERSION=""

with open("VERSION", "r", encoding='utf-8') as f:
    SITE_VERSION = f.read().strip()

description= """
`Why did the developer go to Quickbase Live?`
<br>
`--> Because their API was so good, it had its own fanbase!"`

While the API is not that useful, it is a good example
<br>
of why you should hire me.
"""

app = FastAPI(
    title="Quickbase Live API",
    docs_url="/swagger",
    description=description,
    version=SITE_VERSION,
    license_info={
        "name": "MIT",
        "url": "https://github.com/ihatemodels/Quickbase-Live/blob/main/LICENSE",
    },
    contact={
        "name": "Gergin Darakov",
        "url": "https://github.com/ihatemodels",
        "email": "example@yahoo.com",
    },
)

app.mount("/static", StaticFiles(directory="/app/static"), name="static")

templates = Jinja2Templates(directory="/app/templates")

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "site_version": SITE_VERSION}
    )

@app.get("/api/metrics", tags=["Health"])
async def metrics():
    # Return some dummy metrics as an example
    return PlainTextResponse(generate_latest())

@app.get("/api/healthz", tags=["Health"], response_model=HealthzResponse)
async def healthz():
    """
    Retrieve the health of the API.

    ## Description

    """
    uptime = datetime.now() - start_time
    # Basic health check endpoint
    return {"status": "ok", "uptime": str(uptime)}

@app.get("/api/hire-me", tags=["Hire Me"], response_model=HireMeResponse)
async def hire_me():
    """
    Retrieve the reasons why you should hire me.

    ## Method Docs
    This endpoint returns a list of reasons why you should hire me.
    The output should be validated with
    an external sofware 
    or human eyes.

    ## Usage
    ```bash
    curl -X GET "https://quickbase-live/api/hire-me" -H  "accept: application/json"
    ```
    """
    return {
        "reasons": [
            "I am a hard worker",
            "I am a quick learner",
            "I am a team player",
            "I am a good communicator",
            "I am a good problem solver",
            "I am a good leader",
            "I am a good listener",
            "I am a good teacher",
            "I am a good writer",
            "I am a good speaker",
            "I am a good programmer",
            "I am a good tester",
            "I have low self esteem",
        ] 
    }

@app.exception_handler(HTTP_404_NOT_FOUND)
async def custom_404_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse(
        "404.html", {"request": request, "site_version": SITE_VERSION}
    )
