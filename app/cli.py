import typer

from .controllers import ControllerUsuario

main = typer.Typer()


@main.command('add')
def cadastrar(nome: str, email: str, senha: str):
    """Cria um novo usuário com acesso ao sistema."""
    if ControllerUsuario.add_usuario_database(
        nome=nome, email=email, senha=senha
    ):
        print('Usuário cadastrado com sucesso.')
    else:
        print('Erro ao cadastrar o usuário.')


@main.command('login')
def login(email: str, senha: str):
    """Acessar o sistema."""
    if ControllerUsuario.fazer_login(email=email, senha=senha):
        print('Conectado.')
    else:
        print('Usuário ou senha inválido.')
