from typing import Dict, Annotated

from fastapi import APIRouter, Depends

from fleetops.dependencies.common import get_current_user

router = APIRouter()

CurrentUser = Annotated[dict, Depends(get_current_user)]

@router.get("/auth/me")
def get_logged_in_user(current_user: CurrentUser) -> Dict:
    return current_user
