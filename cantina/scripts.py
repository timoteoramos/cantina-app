import uvicorn
from cantina.core import settings


def devserver():
    uvicorn.run(
        "cantina.core.asgi:application",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )
