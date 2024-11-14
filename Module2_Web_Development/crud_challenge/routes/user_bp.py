from flask import Blueprint
from controllers.UserController import allUsers,createUser,viewUser,updateUser, deleteUser

user_bp = Blueprint('user_bp', __name__)
user_bp.route('/', methods=['GET'])(allUsers)
user_bp.route('/<int:user_id>', methods=['GET'])(viewUser)
user_bp.route('/createUser', methods=['POST'])(createUser)
user_bp.route('/updateUser/<int:user_id>', methods=['PUT'])(updateUser)
user_bp.route('/deleteUser/<int:user_id>', methods=['DELETE'])(deleteUser)
