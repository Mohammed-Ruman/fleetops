from typing import List

from fastapi import APIRouter, HTTPException

router = APIRouter()

vehicles=['v1','v2','v3','v4','v5','v6']

@router.get("/vehicles")
def get_vehicles() -> List[str]:
    return vehicles

@router.get("/vehicles/{id}")
def get_vehicle(id: int) -> str:
    if id > len(vehicles):
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicles[id]
