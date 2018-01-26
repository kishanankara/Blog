from database import Database
import uuid
import datetime

__author__='akishan'

class Post(object):
    def __init__(self, author, title, content,blog_id,date=datetime.datetime.utcnow(),id=None):
        self.title=title
        self.author=author
        self.content=content
        self.blog_id=blog_id
        self.id=uuid.uuid4().hex if id is None else id
        self.created_date=date

    def save_to_mongo(self):
        Database.insert(collection='posts',data=self.json())

    def json(self):
        return{
                'id':self.id,
                'blog_id':self.blog_id,
                'author':self.author,
                'content':self.content,
                'title':self.title,
                'created_date':self.created_date}

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts',query={'id': id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts',query={'blog_id': id})]


