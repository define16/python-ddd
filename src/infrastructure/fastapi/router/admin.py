from typing import Union

from fastapi import APIRouter, Depends

from src.application.requests.item_request import Item

router = APIRouter(
    prefix="",
    tags=["admin"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def read_root():
    return {"Admin": "Admin"}
