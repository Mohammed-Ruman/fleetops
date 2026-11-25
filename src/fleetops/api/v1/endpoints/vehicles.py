from typing import List

from fastapi import APIRouter

router = APIRouter()

vehicles=['v1','v2','v3','v4','v5','v6']

@router.get("/vehicles")
def get_vehicles() -> List[str]:
    return vehicles

@router.get("/vehicles/{id}")
def get_vehicle(id: int) -> str:
    return vehicles[id]
