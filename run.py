from evotomasyon import app
import os

if __name__ == '__main__':
    # os.environ["FLASK_RUN_HOST"] = "0.0.0.0"
    # os.environ["FLASK_RUN_PORT"] = "5000"
    # os.environ["FLASK_ENV"] = "debug"
    app.run(ssl_context=('adhoc'))