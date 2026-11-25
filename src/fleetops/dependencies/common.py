from typing import Dict
def get_app_info() -> Dict :
    return {
        "application": "Fleetops",
        "version": "1.0.0",
    }

def get_current_user() -> Dict:
    return {
    "user_id": 1,
    "username": "admin",
    "role": "TENANT_ADMIN"
}