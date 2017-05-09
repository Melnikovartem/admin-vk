import config
import data_base
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        admin = data_base.get_inf()
        self.render('index.html', id_ = "https://vk.com/club" + config._id, admin = admin, x = "width: 75%;")



settings = [
    (r"/", MainHandler),
]

app = tornado.web.Application(settings)
app.listen(8000)
tornado.ioloop.IOLoop.current().start()
