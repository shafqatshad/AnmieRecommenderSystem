from anime_flask import app
from flask_socketio import *

socketio = SocketIO(app, logger=True)
socketio.run(app, debug=True)