
def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

perfil_usuario = input("Digite seu perfil (admin, usuário, etc.): ")

loginUsuario(perfil_usuario)
