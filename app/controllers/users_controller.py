from typing import List

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from app.schemas.user_schema import User, UserFilter
from app.services.users_service import UsersService
from app.utils.logger import get_logger

user_controller = APIRouter()
logger = get_logger("UserController")

@user_controller.get(
    path="/external-data-users",
    summary="Get User for de external API",
    tags=["User"],
    response_model=List[User])
def get_users():
    """Endpoint GET all users"""
    try:
        logger.info("Init get users controller")
        service = UsersService()
        users = service.get_all_users()
        users_dict = [user.model_dump() for user in users]
        logger.info(f"End get users controller {users_dict}")
        return JSONResponse(content={"users": users_dict}, status_code=status.HTTP_200_OK)
    except Exception as err:
        logger.exception(f"Unexpected error occurred while retrieving users: {err}")
        raise HTTPException(status_code=500, detail="Internal server error")


@user_controller.post(
    path="/external-data-users/filter",
    summary="Get User to filter",
    tags=["User", "Filter"],
    response_model=List[User])
def filter_users(filter_data: UserFilter):
    """Endpoint POST to filter users by a specific key and value."""
    try:
        logger.info(f"Filtering users by {filter_data.filter_key}={filter_data.filter_value}")
        service = UsersService()
        filtered_users = service.filter_users(filter_data.filter_key, filter_data.filter_value)

        if not filtered_users:
            raise HTTPException(status_code=404, detail="No users found matching the criteria")

        users_dict = [user.model_dump() for user in filtered_users]
        return JSONResponse(content={"users": users_dict}, status_code=status.HTTP_200_OK)
    except Exception as err:
        logger.exception(f"Error filtering users: {err}")
        raise HTTPException(status_code=500, detail="Internal server error")