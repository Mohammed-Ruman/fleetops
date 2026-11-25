from typing import Dict

from fastapi import APIRouter, Depends

from fleetops.dependencies.common import get_current_user

router = APIRouter()

@router.get("/auth/me")
def get_logged_in_user(current_user:Dict = Depends(get_current_user)) -> Dict:
    return current_user
