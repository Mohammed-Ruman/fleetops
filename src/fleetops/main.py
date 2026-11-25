from fastapi import FastAPI
from fleetops.api.v1.endpoints.health import router as health_router
from fleetops.api.v1.endpoints.vehicles import router as vehicle_router
from fleetops.api.v1.endpoints.auth import router as auth_router
app = FastAPI(
    title="FleetOps",
    version="1.0.0"
)

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)

app.include_router(
    vehicle_router,
    prefix="/api/v1",
    tags=["Vehicles"]
)

app.include_router(
    auth_router,
    prefix="/api/v1",
    tags=["Authentication"]
)
