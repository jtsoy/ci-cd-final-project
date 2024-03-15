"""
Service Package
"""
from flask import Flask

app = Flask(__name__)

from service import routes
from service.common import log_handlers

log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("SERVICE RUNNING".center(70, "*"))
app.logger.info(70 * "*")
