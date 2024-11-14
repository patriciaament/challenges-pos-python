from flask import Response, request
from models.User import User
from models.User import db
import json 


def allUsers():
    session = db.session()
    users = session.query(User).all()
    user_json = [user.serialize() for user in users]
    session.close()
    return Response(json.dumps(user_json))

def createUser():
    body = request.get_json()
    session = db.session()
    try:
        user = User(name=body['name'],phone=body['phone'],
                    address=body['address'],cpf=body['cpf'])
        session.add(user)
        session.commit()
        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        session.rollback()
    finally:
        session.close()

def viewUser(user_id):
    session = db.session()
    try:
        user = session.query(User).get(user_id)
        return Response(json.dumps([user.serialize()]))
    except Exception as e:
        session.rollback()
        return {"erro": "usuario nao encontrado"}
    finally:
        session.close()

def updateUser(user_id):
    session = db.session()
    try:
        body = request.get_json()
        user = session.query(User).get(user_id)
        if body and body['name']:
            user.name = body['name']
        if body and body['phone']:
            user.phone = body['phone']
        if body and body['address']:
            user.address = body['address']
        if body and body['cpf']:
            user.cpf = body['cpf']
        session.commit()
        return {"sucesso": "usuario alterado"}
    except Exception as e:
        session.rollback()
        return {"erro": "Dados informados incorretamente ou faltantes"}
    finally:
        session.close()

def deleteUser(user_id):
    session = db.session()
    try:
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return {"sucesso": "usuario deletado"}
    except Exception as e:
        session.rollback()
        return {"erro": "nao foi possivel deletar usuario"}
    finally:
        session.close()
