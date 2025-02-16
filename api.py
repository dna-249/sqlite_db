from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, reqparse , fields, Api, marshal_with ,abort
from flask_cors import cross_origin,CORS

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'
db = SQLAlchemy(app)
api = Api(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image =db.Column(db.String, unique = True, nullable= False)
    name =db.Column(db.String, unique = True, nullable= False)
    description =db.Column(db.String, unique = True, nullable= False)
    price =db.Column(db.String, unique = True, nullable= False)
    category =db.Column(db.String, unique = False, nullable= False)
    contact =db.Column(db.String, unique = True, nullable= False)
    whatsapp =db.Column(db.String, unique = True, nullable= False)
 
    def __repr__(self):
        
        return f"User(id = {self.id},image = {self.image},name = {self.name}, description = {self.description},price = {self.price},category = {self.category},contact = {self.contact},whatsapp = {self.whatsapp},)"
    
user_args = reqparse.RequestParser()
user_args.add_argument("image", type=str,required=True,help="name cannot be found")   
user_args.add_argument("name", type= str,required=True,help="email cannot be found")   
user_args.add_argument("description", type= str,required=True,help="email cannot be found")   
user_args.add_argument("price", type= str,required=True,help="email cannot be found")   
user_args.add_argument("category", type= str,required=True,help="email cannot be found")   
user_args.add_argument("contact", type= str,required=True,help="email cannot be found")   
user_args.add_argument("whatsapp", type= str,required=True,help="email cannot be found")   

userFields ={
    "id":fields.Integer,
    "image":fields.String,
    "name":fields.String,
    "description":fields.String,
    "price":fields.String,
    "category":fields.String,
    "contact":fields.String,
    "whatsapp":fields.String,
}

class User(Resource):
    
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users
    
    
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(image=args["image"],  name=args["name"], description=args["description"], price=args["price"], category=args["category"], contact=args["contact"], whatsapp=args["whatsapp"])
        db.session.add(user)
        db.session.commit()
        user=UserModel.query.all()
        return user, 201
    
api.add_resource(User,"/api/users")
        

        
@app.route("/")

def nur():
    return "hello"

if __name__ == "__main__":
    app.run()