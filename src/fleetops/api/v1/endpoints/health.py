from typing import Dict

from fastapi import APIRouter
from fastapi import Depends
from fleetops.dependencies.common import get_app_info
router = APIRouter()

@router.get("/health")
def health(app_info: Dict = Depends(get_app_info)):
    return {
        "status": "healthy",
        **app_info
    }

