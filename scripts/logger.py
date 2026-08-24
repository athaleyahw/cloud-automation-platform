import logging
import os

from config import LOG_PATH


os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)


logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger(__name__)