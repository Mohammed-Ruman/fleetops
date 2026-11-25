from typing import Dict

from fastapi import APIRouter
from fastapi import Depends
from fleetops.dependencies.common import get_app_info
from typing import Annotated
router = APIRouter()

AppInfo = Annotated[Dict,Depends(get_app_info)]

@router.get("/health")
def health(app_info: AppInfo) -> Dict:
    return {
        "status": "healthy",
        **app_info
    }

