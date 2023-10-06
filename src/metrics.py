from prometheus_client import Counter

REQUESTS_TOTAL_METRIC        = Counter("http_requests_total", "Total number of HTTP requests.")
HTTP_5XX_ERRORS_TOTAL_METRIC = Counter("http_5xx_errors_total", "Total number of HTTP 5xx responses.")
HTTP_404_ERRORS_TOTAL_METRIC = Counter("http_404_errors_total", "Total number of HTTP 404 responses.")