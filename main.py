from sanic import Sanic
from sanic.response import json
from textwrap import dedent
from sanic_ext import Extend
from app.middlewares.auth_middleware import authenticate_request
from app.routes.v1 import v1_routes
from app.db import init_db


app = Sanic("MyApp")
Extend(app)
init_db(app)
for route in v1_routes:
    app.blueprint(route)

app.ext.openapi.describe(
    "Testing API",
    version="1.2.3",
    description=dedent(
        """
        # Info
        This is a description. It is a good place to add some _extra_ documentation.

        **MARKDOWN** is supported.
        """
    ),      
)
app.register_middleware(authenticate_request, "request")


@app.route("/")
async def hello(request):
    return json({"message": "Hello, Sanic!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002, debug=True)
