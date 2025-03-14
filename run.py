from app.core.config import get_settings

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.app:application",
        host=get_settings().HOST,
        port=get_settings().PORT,
        reload=get_settings().DEBUG,
    )