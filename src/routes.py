from flask import jsonify, render_template

from .data.dbpedia import DBpediaDataSource


def init_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/api")
    def api():
        return jsonify(DBpediaDataSource().get_data())
