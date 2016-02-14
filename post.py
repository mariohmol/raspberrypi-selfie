from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
import os
print 


client = Client(os.environ['WP_LINK'],os.environ['WP_USER'],os.environ['WP_PASS'])
posts = client.call(posts.GetPosts())
# posts == [WordPressPost, WordPressPost, ...]
from wordpress_xmlrpc import WordPressPost

post = WordPressPost()
post.title = 'My post'
post.content = 'This is a wonderful blog post about XML-RPC.'
#post.id = client.call(posts.NewPost(post))
client.call(NewPost(post))

# whoops, I forgot to publish it!
#post.post_status = 'publish'
#client.call(posts.EditPost(post.id, post))
