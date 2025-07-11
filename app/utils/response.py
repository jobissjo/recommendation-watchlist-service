from sanic.response import json
from typing import Any, Optional, Dict, List
from datetime import datetime
import uuid
import json as native_json

class UUIDEncoder(native_json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

class APIResponse:
    """Helper class for creating consistent API responses"""
    
    @staticmethod
    async def success(message: str = "Success", data: Any = None, status: int = 200):
        """Create a successful response"""
        response_data = {
            "success": True,
            "message": message,
            "data": data
        }
        return json(response_data, status=status, cls=UUIDEncoder)
    
    @staticmethod
    async def error(message: str = "Error", error: Optional[str] = None, status: int = 400):
        """Create an error response"""
        response_data = {
            "success": False,
            "message": message
        }
        if error:
            response_data["error"] = error
        return json(response_data, status=status)
    
    @staticmethod
    async def created(message: str = "Created successfully", data: Any = None):
        """Create a 201 Created response"""
        return await APIResponse.success(message, data, 201)
    
    @staticmethod
    async def not_found(message: str = "Resource not found"):
        """Create a 404 Not Found response"""
        return await APIResponse.error(message, status=404)
    
    @staticmethod
    async def unauthorized(message: str = "Unauthorized"):
        """Create a 401 Unauthorized response"""
        return await APIResponse.error(message, status=401)
    
    @staticmethod
    async def forbidden(message: str = "Forbidden"):
        """Create a 403 Forbidden response"""
        return await APIResponse.error(message, status=403)
    
    @staticmethod
    async def validation_error(message: str = "Validation error", errors: Dict = None):
        """Create a 422 Validation Error response"""
        response_data = {
            "success": False,
            "message": message
        }
        if errors:
            response_data["errors"] = errors
        return json(response_data, status=422)
    
    @staticmethod
    async def server_error(message: str = "Internal server error", error: Optional[str] = None):
        """Create a 500 Internal Server Error response"""
        return await APIResponse.error(message, error, 500)
    
    @staticmethod
    async def paginated(
        message: str = "Data retrieved successfully",
        data: List = None,
        page: int = 1,
        per_page: int = 10,
        total: int = 0,
        total_pages: int = 0
    ):
        """Create a paginated response"""
        response_data = {
            "success": True,
            "message": message,
            "data": data or [],
            "pagination": {
                "page": page,
                "per_page": per_page,
                "total": total,
                "total_pages": total_pages,
                "has_next": page < total_pages,
                "has_prev": page > 1
            }
        }
        return json(response_data)
