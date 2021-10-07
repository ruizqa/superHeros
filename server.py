from flask_app import app
from flask_app.controllers import superheroes
from dotenv import load_dotenv
# ...server.py



if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)
