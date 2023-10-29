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


class GeoBox(BaseModel):
    min_latitude: int = Field(alias="minLatitude")
    min_longitude: int = Field(alias="minLongitude")
    max_latitude: int = Field(alias="maxLatitude")
    max_longitude: int = Field(alias="maxLongitude")


class Resource(BaseInfo):
    unit: str
    geo_box: GeoBox = Field(alias="geoBox")


class VersionResponse(BaseInfo):
    resource: list[Resource]


class Position(BaseModel):
    _from: datetime.datetime
    to: datetime.datetime
    height: float
    latitude: float
    longitude: float


class Station(Position):
    name: str
    owner: str
    owner_category: str = Field(alias="ownerCategory")
    measuring_stations: str = Field(alias="measuringStations")
    id: int


class ParameterResponse(BaseInfo):
    unit: str
    value_type: str = Field(alias="valueType")
    station_set: list[BaseInfo] = Field(alias="stationSet")
    station: list[Station]


class StationResponse(BaseInfo):
    owner: str
    owner_category: str = Field(alias="ownerCategory")
    measuring_stations: str = Field(alias="measuringStations")
    active: bool
    _from: datetime.datetime
    to: datetime.datetime
    position: list[Position]
    period: list[BaseInfo]


class StationSetResponse(StationResponse):
    # TODO: Should we remove if its the same?
    pass
