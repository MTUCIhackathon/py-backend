from fastapi import HTTPException, status


def with_errors(*errors: HTTPException):
    errors_data = {}
    for err in errors:
        if err.status_code in errors_data:
            errors_data[err.status_code]["description"] += f"\n\n{err.detail}"
        else:
            errors_data[err.status_code] = {"description": err.detail}
    return errors_data


def invalid_credentials():
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail="Invalid credentials")


def expired_token():
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail="Token was expired")


def invalid_token():
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail="Invalid token")


def unauthorized():
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail="User is not authorized")


def already_exists(object_for_error: str):
    if object_for_error is not None:
        return HTTPException(status_code=status.HTTP_409_CONFLICT,
                             detail=f"{object_for_error} already exists")
    else:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="Already exists")


def forbidden():
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                         detail="User has not access")


def bad_request():
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                         detail="Wrong data of request")


def iternal_server():
    return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                         detail="Internal server error")


def not_found(object_for_error: str):
    if object_for_error is not None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"{object_for_error} not found")
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Not found")
