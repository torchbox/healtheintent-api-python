from requests import HTTPError


class HealthEIntentAPIError(HTTPError):
    """There was an error communicating with the Health E Intent API"""
    pass


class HealthEIntentAccessNotPermittedError(HealthEIntentAPIError):
    """The API returned a 401 (Unauthorized) or 403 (Forbidden) error response"""
    pass


class HealthEIntentBadRequestError(HealthEIntentAPIError):
    """The API returned a 400 (Bad Request) response"""
    pass


class HealthEIntentResourceNotFoundError(HealthEIntentAPIError):
    """The API returned a 404 (Resource not found) response"""
    pass


class HealthEIntentResourceConflictError(HealthEIntentAPIError):
    """The API returned a 409 (Conflict) response"""
    pass
