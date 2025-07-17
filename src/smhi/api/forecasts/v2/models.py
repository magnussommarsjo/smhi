from pydantic import BaseModel, Field
from datetime import datetime

class ApprovedTime(BaseModel):
    approved_time: datetime = Field(alias="approvedTime")
    reference_time: datetime = Field(alias="referenceTime")

class ValidTime(BaseModel):
    valid_time: list[datetime] = Field(alias="validTime")