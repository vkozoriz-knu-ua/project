from flask import Flask

from .data.dbpedia import DBpediaDataSource
from .routes import init_routes

app = Flask(__name__)

init_routes(app)
