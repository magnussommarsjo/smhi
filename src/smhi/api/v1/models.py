from __future__ import annotations

from pydantic import BaseModel, Field
import datetime


class Link(BaseModel):
    href: str
    rel: str
    type: str


class BaseInfo(BaseModel):
    key: str
    updated: datetime.datetime
    title: str
    summary: str
    link: list[Link]


class CategoryResponse(BaseInfo):
    version: list[BaseInfo]


class ParameterResponse(BaseInfo):
    unit: str
    value_type: str = Field(alias="valueType")
    station_set: list[dict] = Field(alias="stationSet")  # TODO: more definitions
    station: list[Station]  # TODO: Replace with Station


class Station(BaseModel):
    name: str
    owner: str
    owner_category: str = Field(alias="ownerCategory")
    measuring_stations: str = Field(alias="measuringStations")
    id: int
    height: float
    latitude: float
    longitude: float
    active: bool
    _from: datetime.datetime
    to: datetime.datetime
