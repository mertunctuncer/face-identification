

import uvicorn
from app.core.config import get_settings


log_config = uvicorn.config.LOGGING_CONFIG
log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"

if __name__ == "__main__":
    uvicorn.run(
        "app.app:application",
        host=get_settings().HOST,
        port=get_settings().PORT,
        reload=get_settings().DEBUG,
        log_config=log_config
    )