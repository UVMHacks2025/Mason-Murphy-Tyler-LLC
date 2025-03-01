from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from hackathonMarketplace.backend import User, Item

app = Flask(__name__)
CORS(app)

def home():
    return render_template("../frontend/public/index.html")

@app.route('/signup', methods=['POST'])
def createUserAccount():
    try:
        data = request.get_json()

        if not data or 'email' not in data or 'password' not in data:
            return jsonify({"success": False, "message": "Missing email or password"}), 400
        
        email = data['email']
        password = data['password']
        role = "student" if email.endswith('.edu') else "notStudent"

        print(f"Creating user: {email} with role {role}")

        user = User(None, password, email, role)
        user.add_user()

        return jsonify({"success": True, "message": "Signup successful!"}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# Separate endpoints for listings and users
@app.route('/createListing', methods=['POST'])
def createListing():
    form = request.form
    newListing = Item(form.name, form.image, form.price, form.type, form.email, form.password, None)
    newListing.add_item_to_db()
    return newListing

@app.route('/createUser', methods=['POST'])
def createNewUser():
    try:
        form = request.get_json()
        user = User(None, form["password"], form["email"])
        user.add_user()
        return jsonify({"success": True, "message": "User created successfully!"}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
