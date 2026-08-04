import logging

from config.config import (
    LOG_FILE,
    LOG_LEVEL,
    LOG_FORMAT,
)

logging.basicConfig(
    filename=LOG_FILE,
    level=getattr(logging, LOG_LEVEL),
    format=LOG_FORMAT,
)

logger = logging.getLogger(__name__)