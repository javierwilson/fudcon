# -*- coding: utf-8 -*-
"""
fudcon.modules.sessions.models
~~~~~~~~~~~~~~~~~~~~~

Sessions models
"""

from fudcon.database import db

TALKS = 1
BARCAMPS = 2
WORKSHOPS = 3


class Session(db.Model):
    """
    Model for the speaker sessions, talks
    workshops or barcamps
    """
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    topic = db.Column(db.String(255))
    description = db.Column(db.Text())
    session_type = db.Column(db.SmallInteger())
    fas = db.Column(db.String(255))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    day = db.Column(db.Integer)
    time_start = db.Column(db.Time(timezone=False))
    time_end = db.Column(db.Time(timezone=False))
    active = db.Column(db.Boolean())
