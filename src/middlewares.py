
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from log import logger
from metrics import HTTP_5XX_ERRORS_TOTAL_METRIC, REQUESTS_TOTAL_METRIC


class RequestCounterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        REQUESTS_TOTAL_METRIC.inc()
        if 500 <= response.status_code < 600:
            HTTP_5XX_ERRORS_TOTAL_METRIC.inc()
        return response

class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        logger.info(
            "access log",
            extra={
                "component": "api",
                "method": request.method,
                "url": str(request.url),
                "status_code": response.status_code,
            },
        )
        return response