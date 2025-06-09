def main():
    print("Sistema de Cadastro")

    # 
    perfil_usuario = {}

    # coleta de informação de usuario
    perfil_usuario['nome_usuario'] = input("Digite seu nome de usuário: ")
    perfil_usuario['nome_perfil'] = input("Digite seu nome de perfil: ")
    perfil_usuario['email'] = input("Digite seu e-mail: ")
    perfil_usuario['telefone'] = input("Digite seu telefone: ")
    perfil_usuario['senha'] = input("Digite sua senha: ")

    # dados coletados
    print("\nDados Cadastrados")
    print(f"Nome de usuário: {perfil_usuario['nome_usuario']}")
    print(f"Nome de perfil: {perfil_usuario['nome_perfil']}")
    print(f"E-mail: {perfil_usuario['email']}")
    print(f"Telefone: {perfil_usuario['telefone']}")
    print("Senha: ********")  # coloquei o print para borrar a senha

# esse vai apresentar os dados 
if __name__ == "__main__":
    main()
