from datetime import datetime
from ninja import Schema, ModelSchema
from ninja.orm import create_schema
from .models import Track


# class TrackSchema(Schema):
#     title: str
#     artist: str
#     duration: float
#     last_play: datetime

# class TrackSchema(ModelSchema):
#     class Config:
#         model = Track
#         model_fields = ["title", "artist", "duration", "last_play"]


TrackSchema = create_schema(Track, fields=["title", "artist", "duration", "last_play"])


class NotFoundSchema(Schema):
    message: str
