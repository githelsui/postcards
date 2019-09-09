from google.appengine.ext import ndb

class Tree(ndb.Model):
    lat = ndb.FloatProperty(required=True)
    long = ndb.FloatProperty(required=True)
    number = ndb.FloatProperty(required=True)
    user_id = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    date = ndb.StringProperty(required=True)

class SentPostcard(ndb.Model):
    # img = ndb.FloatProperty(required=True)
    user_id = ndb.StringProperty(required=True)
    message = ndb.StringProperty(required=False)
    to = ndb.StringProperty(required=False)
    date = ndb.StringProperty(required=True)

class ReceivedPostcard(ndb.Model):
    # img = ndb.FloatProperty(required=True)
    user_id = ndb.StringProperty(required=True)
    message = ndb.StringProperty(required=False)
    to = ndb.StringProperty(required=False)
    date = ndb.StringProperty(required=True)

class User(ndb.Model):
    user_id = ndb.StringProperty(required=True)
    username = ndb.StringProperty(required=True)
    numberOfTrees = ndb.FloatProperty(required=True)
