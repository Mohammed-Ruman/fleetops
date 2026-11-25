from fastapi import APIRouter
router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "FleetOps",
        "version": "1.0.0"
    }

