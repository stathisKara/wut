from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_restful import Api, Resource, reqparse


# engine = create_engine('sqlite:///tutorial.db', echo=True)

variablaae = 5
app = Flask(__name__)
api = Api(app)
# app.secret_key = os.urandom(12)


# users = [{"name": "Nicholas", "age": 42, "occupation": "Network Engineer"}]


# class User(Resource):
#
#     def get(self, name):
#         for user in users:
#             if name == user["username"]:
#                 return user, 200
#         return "user not found 404"
#
#     def post(self, name):
#         parser = reqparse.RequestParser()
#         parser.add_argument("email")
#         parser.add_argument("username")
#         args = parser.parse_args()
#
#         for user in users:
#             if name == user["username"]:
#                 return "user with name {} already exists".format(name), 400
#
#         user = {
#             "username": name,
#             "email": args["email"],
#             "name": args["name"]
#         }
#         users.append(user)
#         return user, 201
#
#     def put(self, name):
#         parser = reqparse.RequestParser()
#         parser.add_argument("email")
#         parser.add_argument("username")
#         args = parser.parse_args()
#
#         for user in users:
#             if name == user["username"]:
#                 if name == user["username"]:
#                     user["email"] = args["email"]
#                     user["name"] = args["name"]
#                     return user, 200
#
#         user = {
#             "username": name,
#             "email": args["email"],
#             "name": args["name"]
#         }
#         users.append(user)
#         return user, 200
#
#     def delete(self, name):
#         global users
#         users = [user for user in users if user["username"] != name]
#         return "{} is delete.".format(name), 200


# api.add_resource(User, "/user/<string:name>")

# s = Session()
sessionn = {}
@app.route('/')
def home(origin=""):
    print(variablaae)
    if sessionn.get('logged_in') and origin == "logout":
        return "Hello "  + "!  <a href='/logout'>Logout</a>"
    else:
        return "hi"


@app.route('/login', methods=['POST'])
def do_admin_login():
    variablaae = 5
    # POST_USERNAME = str(request.form['username'])
    # POST_PASSWORD = str(request.form['password'])
    #
    # Session = sessionmaker(bind=engine)

    # query2 = s.query(User)
    # s.add(User("lala", "lala", "kaska"))
    # s.commit()
    # query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    # result = query.first()
    result = 0
    if result:
        sessionn['logged_in'] = True
    else:
        flash('wrong password!')
    return home("logout")


@app.route("/logout")
def logout():
    # if not session['logged_in']:
    #     return home()
    variablaae = 5
    sessionn['logged_in'] = False
    return home("logout")


if __name__ == "__main__":

    # importing required libraries
    app.run(debug=True, host='0.0.0.0', port=4000)
