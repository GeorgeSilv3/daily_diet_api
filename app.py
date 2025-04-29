from datetime import datetime
from flask import Flask, request, jsonify
from database import db
from models.meal import Meal

app = Flask(__name__)

app.config["SECRET_KEY"] = "my_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

@app.route("/meal", methods=["POST"])
def create_meal():

    data = request.json
    name = data.get("name")
    description = data.get("description")
    date_time = datetime.fromisoformat(data.get("date_time"))
    on_diet = (True if data.get("on_diet").lower() == "true" else False)
    
    if name and description and date_time:
        try:
            meal = Meal(name=name, description=description, date_time=date_time, on_diet=on_diet)

            db.session.add(meal)
            db.session.commit()

        except NameError as error:
            return jsonify({"message": "Error to register on database"}), 500
        return jsonify({"message": "Meal registered with successfull"})

    return jsonify({"message": "Something goes wrong!"}), 400

if __name__ == "__main__":
    app.run(debug=True)