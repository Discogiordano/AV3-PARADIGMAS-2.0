from usuario_funcoes import (cadastrar_usuario, login_usuario, excluir_usuario, alterar_senha,
                             adicionar_preferencia, remover_preferencia, adicionar_historico, 
                             listar_conteudos, recomendar_conteudos)
from persistencia import salvar_dados, carregar_dados

def main():
    usuarios, conteudos = carregar_dados()
    usuario_logado = None

    while True:
        print("\nMenu:")
        print("1. Cadastrar Usuário")
        print("2. Login")
        print("3. Excluir Usuário")
        print("4. Alterar Senha")
        print("5. Listar Conteúdos")
        print("6. Assistir Conteúdo")
        print("7. Ver Tipo de Assinatura")
        print("8. Alterar Tipo de Assinatura")
        print("9. Ver Preferências")
        print("10. Alterar Preferências")
        print("11. Ver Histórico")
        print("12. Recomendação por preferência")
        print("13. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            tipo_assinatura = input("Tipo de Assinatura (básica, premium) (b/p): ")
            if cadastrar_usuario(usuarios, nome, email, senha, tipo_assinatura):
                print("Usuário cadastrado com sucesso!")
            else:
                print("Erro de cadastro")

        elif escolha == '2':
            email = input("Email: ")
            senha = input("Senha: ")
            usuario_logado = login_usuario(usuarios, email, senha)
            if usuario_logado:
                print("Login bem-sucedido!")
            else:
                print("Email ou senha incorretos.")

        elif escolha == '3':
            if usuario_logado and excluir_usuario(usuarios, usuario_logado):
                print("Usuário excluído com sucesso.")
                usuario_logado = None
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '4':
            if usuario_logado:
                nova_senha = input("Nova senha: ")
                alterar_senha(usuario_logado, nova_senha)
                print("Senha alterada com sucesso.")
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '5':
            conteudos_list = listar_conteudos(conteudos)
            for conteudo in conteudos_list:
                print(conteudo)

        elif escolha == '6':
            if usuario_logado:
                id_conteudo = int(input("ID do Conteúdo para assistir: "))
                if id_conteudo in conteudos:
                    adicionar_historico(usuario_logado, id_conteudo)
                    print(f"Assistido: {conteudos[id_conteudo].titulo}")
                else:
                    print("Conteúdo não encontrado.")
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '7':
            if usuario_logado:
                print(f"Tipo de Assinatura: {usuario_logado.tipo_assinatura}")
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '8':
            if usuario_logado:
                novo_tipo = input("Novo tipo de assinatura (básica, premium): (b/p)")
                if novo_tipo in ['b', 'p']:
                    usuario_logado.tipo_assinatura = 'básica' if novo_tipo == 'b' else 'premium'
                    print("Tipo de assinatura atualizado com sucesso.")
                else:
                    print("Falha ao atualizar tipo de assinatura.")
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '9':
            if usuario_logado:
                print("Preferências:", ', '.join(usuario_logado.preferencias))
                if not usuario_logado.preferencias:
                    print("Sem preferências")
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '10':
            if usuario_logado:
                genero = input("Gênero para adicionar ou remover: ").lower()
                acao = input("Adicionar ou Remover? (a/r): ").lower()

                # Verifica se o gênero existe nos conteúdos
                generos_existentes = set()
                for conteudo in conteudos.values():
                    generos_existentes.update(conteudo.generos)

                if genero not in generos_existentes:
                    print("Gênero inválido. Por favor, escolha um gênero existente.")
                else:
                    if acao == 'a':
                        adicionar_preferencia(usuario_logado, genero)
                        print("Preferência adicionada com sucesso.")
                    elif acao == 'r':
                        remover_preferencia(usuario_logado, genero)
                        print("Preferência removida com sucesso.")
                    else:
                        print("Ação inválida.")
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '11':
            if usuario_logado:
                historico = [conteudos[id].titulo for id in usuario_logado.historico]
                print("Histórico de visualizações:", ', '.join(historico))
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '12':
            if usuario_logado:
                recomendados = recomendar_conteudos(usuario_logado, conteudos)
                if recomendados:
                    print("Conteúdos recomendados:")
                    for rec in recomendados:
                        print(rec)
                else:
                    print("Nenhum conteúdo corresponde às suas preferências.")
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '13':
            salvar_dados(usuarios, conteudos)
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
