__author__='akishan'

from models.post import Post
from database import Database

Database.initialize()
posts = Post.from_blog('123')




for post in posts:
    print(post)

