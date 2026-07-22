from fastapi import APIRouter
from pydantic import BaseModel
from forge_ai.api.schemas.health import HealthData
from forge_ai.api.schemas.common import SuccessResponse

router = APIRouter()
@router.get("/health",response_model=SuccessResponse[HealthData])
async def health()-> SuccessResponse[HealthData]:
    return SuccessResponse(
        message="Health check completed successfully.",
        data= HealthData(
            status="healthy"
        )
    )