from flask import Blueprint
from controllers.UserController import index,store,update,destroy,show

user_bp = Blueprint('user_bp', __name__)
user_bp.route('/', method='GET')(index)
user_bp.route('/create', method='POST')(store)
user_bp.route('/delete/<int:user_id>', method='DELETE')(destroy)
user_bp.route('/update/<int:user_id>', method='PUT')(update)
user_bp.route('/<int:user_id>', method='GET')(show)
