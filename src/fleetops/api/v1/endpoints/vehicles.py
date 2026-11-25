from typing import List, Dict

from fastapi import APIRouter, HTTPException, Depends

from fleetops.dependencies.common import get_vehicle_service

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

@router.get("/dependency-check")
def dependency_check(service:Dict=Depends(get_vehicle_service)):
    return service