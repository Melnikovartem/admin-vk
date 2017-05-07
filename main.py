import time
import data_base
import vki
import config

posts = vki.get_posts(config._id)
while True:
    posts_now = vki.get_posts(config._id)
    if posts < posts_now:
        print("i")
        posts = posts_now
        vki.get_online(config._id)
    
    time.sleep(60)
