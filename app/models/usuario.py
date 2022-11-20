from sqlalchemy import BINARY, Column, Integer, String
from sqlalchemy.orm import validates

from .base import Base


class Usuario(Base):
    __tablename__ = 'usuario'

    id: int = Column(Integer, primary_key=True)
    nome: str = Column(String(50))
    email: str = Column(String(50), unique=True)
    senha: bytes = Column(BINARY)
    salt: bytes = Column(BINARY)

    @validates('nome')
    def validar_nome(self, chave, valor):
        if len(valor) < 4:
            raise ValueError('Nome pequeno demais.')
        return valor

    @validates('email')
    def validar_email(self, chave, valor):
        if '@' not in valor:
            raise ValueError('Email inválido.')
        return valor
