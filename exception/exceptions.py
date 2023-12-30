from fastapi import HTTPException
from starlette import status


class CricketExceptions():
    def get_exceptions(self, model):
        if model is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Details Not Found"
            )
