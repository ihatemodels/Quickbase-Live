import json
import logging
from logging import Formatter


class JsonFormatter(Formatter):
    def __init__(self):
        super(JsonFormatter, self).__init__()

    def format(self, record):
        json_record = {}
        json_record["message"] = record.getMessage()
        if "method" in record.__dict__:
            json_record["method"] = record.__dict__["method"]

        if "url" in record.__dict__:
            json_record["url"] = record.__dict__["url"]
       
        if "status_code" in record.__dict__: 
            json_record["status_code"] = record.__dict__["status_code"]

        if "component" in record.__dict__:
            json_record["component"] = record.__dict__["component"]
          
        if record.levelno == logging.ERROR and record.exc_info:
            json_record["err"] = self.formatException(record.exc_info)
        return json.dumps(json_record)

logger = logging.root
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.handlers = [handler]
logger.setLevel(logging.DEBUG)
logging.getLogger("uvicorn.access").disabled = True