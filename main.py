import time
import data_base
import vki
import config

posts = vki.get_posts(config._id)
while True:
    posts_now = vki.get_posts(config._id)
    if posts < posts_now:
        posts = posts_now
        data_base.new_write(vki.get_online(config._id))
    time.sleep(config.sleep)

