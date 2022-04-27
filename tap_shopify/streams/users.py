import shopify

from tap_shopify.context import Context
from tap_shopify.streams.base import Stream

class Users(Stream):
    name = 'users'
    replication_object = shopify.Users

Context.stream_objects['users'] = Users
