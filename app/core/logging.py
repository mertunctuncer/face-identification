import logging
import sys
from logging import getLogger

from app.core.config import get_settings

logger = getLogger(__name__)
logger.setLevel(get_settings().LOG_LEVEL)

face_id_formatter = logging.Formatter("%(asctime)s [FaceIDService] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s")

face_id_stream_handler = logging.StreamHandler(sys.stdout)
face_id_stream_handler.setFormatter(face_id_formatter)
file_handler = logging.FileHandler("system.log")
file_handler.setFormatter(face_id_formatter)

logger.addHandler(face_id_stream_handler)
logger.addHandler(file_handler)