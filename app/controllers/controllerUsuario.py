import hashlib
import os

from sqlalchemy.exc import IntegrityError

from app.database import get_session
from app.models import Usuario


class ControllerUsuario:
    @staticmethod
    def encriptar_senha(senha: str, salt: bytes):
        return hashlib.pbkdf2_hmac(
            'sha256', senha.encode('utf-8'), salt, 100000
        )

    @classmethod
    def add_usuario_database(cls, nome: str, email: str, senha: str) -> bool:
        with get_session() as session:
            try:
                salt = os.urandom(32)
                senha_encriptada = cls.encriptar_senha(senha=senha, salt=salt)
                usuario = Usuario(
                    nome=nome, email=email, senha=senha_encriptada, salt=salt
                )
                session.add(usuario)
                session.commit()
                return True
            except ValueError as error:
                print(f'ValueError: {error}')
                return False
            except IntegrityError as error:
                print('Email já existe')
                return False
            except Exception as e:
                print(f'erro {type(e)}')
                return False

    @classmethod
    def fazer_login(cls, email: str, senha: str):
        with get_session() as session:
            try:
                usuario = (
                    session.query(Usuario).filter(Usuario.email == email).one()
                )
                senha_encriptada = cls.encriptar_senha(
                    senha=senha, salt=usuario.salt
                )
                if senha_encriptada == usuario.senha:
                    return True
                else:
                    return False
            except Exception:
                return False
