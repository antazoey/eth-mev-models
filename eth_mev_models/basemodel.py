from typing import Any

from pydantic import BaseModel as RootBaseModel


class BaseModel(RootBaseModel):
    def model_dump(
        self, *, by_alias: bool = True, mode: str = "json", **kwargs: Any
    ) -> dict:
        return super().model_dump(by_alias=by_alias, mode=mode, **kwargs)

    def model_dump_json(
        self,
        *,
        by_alias: bool = True,
        **kwargs: Any,
    ) -> str:
        return super().model_dump_json(by_alias=by_alias, **kwargs)
