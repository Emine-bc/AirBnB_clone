#!/usr/bin/python3

from models.base_model import BaseModel

'''Review '''


class Review(BaseModel):
    '''Review manage'''
    place_id = ""
    user_id = ""
    text = ""
