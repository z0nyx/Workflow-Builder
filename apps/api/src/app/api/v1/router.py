from fastapi import APIRouter

from app.api.v1.users import router as users_router

router = APIRouter()


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


router.include_router(users_router)