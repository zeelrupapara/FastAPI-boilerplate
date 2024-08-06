# fastapi
from fastapi import FastAPI, Depends
from app.core.modules import init_routers, make_middleware
from app.core.logger import get_logger


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="FastAPI starter kit",
        description="FastAPI starter kit that is needed for every fastapi project.",
        version="1.0.0",
        docs_url="/api/v1/docs",
        dependencies=[Depends(get_logger)],
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    return app_


app = create_app()
