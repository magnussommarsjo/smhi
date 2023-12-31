from __future__ import annotations
from typing import Optional

from pydantic import BaseModel, Field
import datetime


class Link(BaseModel):
    href: str
    rel: str
    type: str


class MetaData(BaseModel):
    key: Optional[str]
    updated: datetime.datetime
    title: str
    summary: str
    link: list[Link]


class CategoryResponse(MetaData):
    version: list[MetaData]


class GeoBox(BaseModel):
    min_latitude: int = Field(alias="minLatitude")
    min_longitude: int = Field(alias="minLongitude")
    max_latitude: int = Field(alias="maxLatitude")
    max_longitude: int = Field(alias="maxLongitude")


class Resource(MetaData):
    unit: str
    geo_box: GeoBox = Field(alias="geoBox")


class VersionResponse(MetaData):
    resource: list[Resource]


class Position(BaseModel):
    _from: datetime.datetime
    to: datetime.datetime
    height: float
    latitude: float
    longitude: float


class StationInfo(BaseModel):
    owner: str
    owner_category: str = Field(alias="ownerCategory")
    measuring_stations: str = Field(alias="measuringStations")


class Station(Position, StationInfo):
    id: int
    name: str


class ParameterResponse(MetaData):
    unit: str
    value_type: str = Field(alias="valueType")
    station_set: list[MetaData] = Field(alias="stationSet")
    station: list[Station]


class StationResponse(MetaData, StationInfo):
    active: bool
    _from: datetime.datetime
    to: datetime.datetime
    position: list[Position]
    period: list[MetaData]


class StationSetResponse(StationResponse):
    # TODO: Should we remove if its the same?
    pass


class PeriodResponse(MetaData):
    _from: datetime.datetime
    to: datetime.datetime
    data: list[MetaData]


class Value(BaseModel):
    date: datetime.datetime
    value: float
    quality: str


class Parameter(BaseModel):
    key: str
    name: str
    summary: str
    unit: str


class Period(BaseModel):
    key: str
    _from: datetime.datetime
    to: datetime.datetime
    summary: str
    sampling: str


class StationData(StationInfo):
    key: str
    name: str
    height: float


class DataStationResponse(BaseModel):
    value: list[Value]
    updated: datetime.datetime
    parameter: Parameter
    station: StationData
    period: Period
    position: list[Position]
    link: list[Link]
