from fastapi import APIRouter, Depends, HTTPException, status
from app.core.dependencies import get_db
from app.core.logger import get_logger, logging
from sqlalchemy.orm import Session


health_module = APIRouter()


@health_module.get("/healthz")
async def health(logger: logging.Logger = Depends(get_logger)):
    logger.debug("Health check")
    return {"status": "ok"}


@health_module.get("/healthdb")
async def healthdb(db: Session = Depends(get_db), logger: logging.Logger = Depends(get_logger)):
    try:
        logger.debug("database health check init")
        db.execute("SELECT 1")
        logger.debug("database health check done")
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=f"Database connection error: {e}")
    
