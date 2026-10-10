from typing import Any

from fastapi.responses import JSONResponse


def success_response(data: Any = None, status_code: int = 200) -> JSONResponse:
    """
    Return the standard success envelope::

        {"success": true, "data": <data>}
    """
    return JSONResponse(
        status_code=status_code,
        content={"success": True, "data": data},
    )


def error_response(
    code: str,
    message: str,
    status_code: int = 400,
    details: Any = None,
) -> JSONResponse:
    """
    Return the standard error envelope::

        {"success": false, "error": {"code": "...", "message": "..."}}
    """
    body: dict = {
        "success": False,
        "error": {"code": code, "message": message},
    }
    if details is not None:
        body["error"]["details"] = details  # type: ignore[index]
    return JSONResponse(status_code=status_code, content=body)
