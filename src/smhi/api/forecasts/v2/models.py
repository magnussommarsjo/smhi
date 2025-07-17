from pydantic import BaseModel, Field
from datetime import datetime

class ApprovedTime(BaseModel):
    approved_time: datetime = Field(alias="approvedTime")
    reference_time: datetime = Field(alias="referenceTime")

class ValidTime(BaseModel):
    valid_time: list[datetime] = Field(alias="validTime")


class Parameter(BaseModel):
    level: int
    level_type: str = Field(alias="levelType")
    name: str
    unit: str
    values: list[float | int]

class Geometry(BaseModel):
    coordinates: list[list[float]]
    type: str  # TODO: Enum / Literal(str)

class TimeSerie(BaseModel): # TODO: Change name? ParameterSet? Forecast?
    valid_time: datetime = Field(alias="validTime")
    parameters: list[Parameter]

class PointForecast(BaseModel):
    approved_time: datetime = Field(alias="approvedTime")
    reference_time: datetime = Field(alias="referenceTime")
    geometry: Geometry
    timeSeries: list[TimeSerie]
