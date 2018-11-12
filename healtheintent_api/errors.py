from requests import HTTPError


class HealthEIntentHttpError(HTTPError):
    """There was an error communicating with the Health E Intent API"""
    pass


class BadRequestError(HealthEIntentHttpError):
    """The API returned a 400 (Bad Request) error response"""
    pass


class UnauthorizedError(HealthEIntentHttpError):
    """The API returned a 401 (Unauthorized) error response"""
    pass


class NotPermittedError(HealthEIntentHttpError):
    """The API returned a 403 (Forbidden) error response"""
    pass


class ResourceNotFoundError(HealthEIntentHttpError):
    """The API returned a 404 (Resource not found) error response"""
    pass


class ResourceConflictError(HealthEIntentHttpError):
    """The API returned a 409 (Conflict) error response"""
    pass
