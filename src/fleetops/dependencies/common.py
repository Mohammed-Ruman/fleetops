from typing import Dict

from fastapi import Depends


def get_app_info() -> Dict :
    return {
        "application": "Fleetops",
        "version": "1.0.0",
    }

def get_current_user() -> Dict:
    print("Executing get_current_user")
    return {
    "user_id": 1,
    "username": "admin",
    "role": "TENANT_ADMIN"
}

def get_current_tenant(user:Dict = Depends(get_current_user)) -> Dict:
    print("Executing get_current_tenant")
    user_id=user["user_id"]
    return {
        "tenant_id": 101,
        "tenant_name": "Acme Transport",
        "user_id": user_id
    }

def get_vehicle_service(tenant:Dict=Depends(get_current_tenant)) -> Dict:
    print("Executing get_vehicle_service")
    return {
        "service":"VehicleService",
        "tenant_id": tenant["tenant_id"],
        "tenant_name": tenant["tenant_name"]
    }