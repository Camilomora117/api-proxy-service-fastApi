from typing import List

from app.config import config
from app.schemas.user_schema import User
from app.utils.http_request import HttpRequest
from fastapi import HTTPException
from app.utils.logger import get_logger


class UsersService:

    def __init__(self):
        self.api_client = HttpRequest()
        self.logger = get_logger("UsersService")

    def get_all_users(self) -> List[User]:
        """
        Get all Users
        """
        try:
            self.logger.info("Init get users service")
            users_data = self.api_client.get(config.API_USERS_URL)
            users = [User(**user) for user in users_data]
            self.logger.info(f"Response api {users}")
            return users
        except Exception as error:
            self.logger.error(f"Error get users service: {error}")
            raise HTTPException(status_code=502, detail="Failed to fetch users from external API")

    def filter_users(self, filter_key: str, filter_value: str) -> List[User]:
        """
        Filters users based on the provided key and value.
        """
        try:
            self.logger.info(f"Init get users filter service, Filter key: {filter_key}, Filter value: {filter_value}")
            users = self.get_all_users()

            # Validate key
            if filter_key not in User.model_fields:
                raise ValueError(f"Invalid filter key: {filter_key}")

            # Filter Data
            filtered_users = [
                user for user in users if str(getattr(user, filter_key, "")).lower() == str(filter_value).lower()
            ]
            self.logger.info(f"Filter data {filtered_users}")

            return filtered_users
        except ValueError as ve:
            self.logger.warning(f"Validation error: {ve}")
            raise ve
        except Exception as error:
            self.logger.exception(f"Error filtering users: {error}")
            raise Exception("Error filtering users")
