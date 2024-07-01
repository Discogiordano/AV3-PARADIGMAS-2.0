"""
from usuario_funcoes import (cadastrar_usuario, login_usuario, excluir_usuario, alterar_senha,
                             adicionar_preferencia, remover_preferencia, adicionar_historico, 
                             listar_conteudos, recomendar_conteudos, buscar_usuario_por_email,
                             alterar_dados_usuario, adicionar_conteudo, alterar_conteudo, excluir_conteudo, obter_proximo_id)
from persistencia import salvar_dados, carregar_dados

def main():
    print("Iniciando o sistema...")
    usuarios, conteudos, conteudos_2 = carregar_dados()
    print("Dados carregados com sucesso.")
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
        print("13. Listar Conteúdos Premium")
        print("14. Gerenciamento de Usuários (Admin)")
        print("15. Gerenciamento de Conteúdos (Admin)")
        print("16. Sair")
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
            if usuario_logado and excluir_usuario(usuarios, usuario_logado.id):
                print("Usuário excluído com sucesso.")
                usuario_logado = None
            else:
                print("Erro: Usuário não logado ou não autorizado.")

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
                elif usuario_logado.tipo_assinatura == 'premium' and id_conteudo in conteudos_2:
                    adicionar_historico(usuario_logado, id_conteudo)
                    print(f"Assistido: {conteudos_2[id_conteudo].titulo}")
                else:
                    print("Conteúdo não encontrado ou acesso não permitido.")
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
                for conteudo in conteudos_2.values():
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
                historico = [conteudos[id].titulo for id in usuario_logado.historico if id in conteudos]
                historico += [conteudos_2[id].titulo for id in usuario_logado.historico if id in conteudos_2]
                print("Histórico de visualizações:", ', '.join(historico))
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '12':
            if usuario_logado:
                recomendados = recomendar_conteudos(usuario_logado, conteudos)
                if usuario_logado.tipo_assinatura == 'premium':
                    recomendados += recomendar_conteudos(usuario_logado, conteudos_2)
                if recomendados:
                    print("Conteúdos recomendados:")
                    for rec in recomendados:
                        print(rec)
                else:
                    print("Nenhum conteúdo corresponde às suas preferências.")
            else:
                print("Erro: Usuário não logado.")

        elif escolha == '13':
            if usuario_logado and usuario_logado.tipo_assinatura == 'premium':
                conteudos_list = listar_conteudos(conteudos_2)
                for conteudo in conteudos_list:
                    print(conteudo)
            else:
                print("Acesso negado. Apenas para usuários com assinatura premium.")

        elif escolha == '14':
            if usuario_logado and usuario_logado.tipo_user == 'administrador':
                while True:
                    print("\nGerenciamento de Usuários (Admin):")
                    print("1. Buscar Usuário por Email")
                    print("2. Alterar Dados de Usuário")
                    print("3. Adicionar Novo Usuário")
                    print("4. Excluir Usuário")
                    print("5. Voltar")
                    opcao_admin_usuarios = input("Escolha uma opção: ")

                    if opcao_admin_usuarios == '1':
                        email = input("Email do usuário: ")
                        usuario_encontrado = buscar_usuario_por_email(usuarios, email)
                        if usuario_encontrado:
                            print(f"Usuário encontrado: {usuario_encontrado.__dict__}")
                        else:
                            print("Usuário não encontrado.")

                    elif opcao_admin_usuarios == '2':
                        email = input("Email do usuário para alterar: ")
                        usuario_encontrado = buscar_usuario_por_email(usuarios, email)
                        if usuario_encontrado:
                            nome = input("Novo Nome (deixe em branco para manter o atual): ")
                            novo_email = input("Novo Email (deixe em branco para manter o atual): ")
                            senha = input("Nova Senha (deixe em branco para manter a atual): ")
                            tipo_assinatura = input("Novo Tipo de Assinatura (básica, premium) (deixe em branco para manter o atual): ")
                            tipo_user = input("Novo Tipo de Usuário (usuário, administrador) (deixe em branco para manter o atual): ")
                            alterar_dados_usuario(usuario_encontrado, nome, novo_email, senha, tipo_assinatura, tipo_user)
                            print("Dados do usuário alterados com sucesso.")
                        else:
                            print("Usuário não encontrado.")

                    elif opcao_admin_usuarios == '3':
                        nome = input("Nome: ")
                        email = input("Email: ")
                        senha = input("Senha: ")
                        tipo_assinatura = input("Tipo de Assinatura (básica, premium) (b/p): ")
                        if cadastrar_usuario(usuarios, nome, email, senha, tipo_assinatura):
                            print("Usuário cadastrado com sucesso!")
                        else:
                            print("Erro de cadastro")

                    elif opcao_admin_usuarios == '4':
                        email = input("Email do usuário para excluir: ")
                        usuario_encontrado = buscar_usuario_por_email(usuarios, email)
                        if usuario_encontrado and excluir_usuario(usuarios, usuario_encontrado.id):
                            print("Usuário excluído com sucesso.")
                        else:
                            print("Erro ao excluir usuário.")

                    elif opcao_admin_usuarios == '5':
                        break

                    else:
                        print("Opção inválida. Tente novamente.")
            else:
                print("Acesso negado. Apenas para administradores.")

        elif escolha == '15':
            if usuario_logado and usuario_logado.tipo_user == 'administrador':
                while True:
                    print("\nGerenciamento de Conteúdos (Admin):")
                    print("1. Adicionar Novo Conteúdo")
                    print("2. Alterar Conteúdo")
                    print("3. Excluir Conteúdo")
                    print("4. Voltar")
                    opcao_admin_conteudos = input("Escolha uma opção: ")

                    if opcao_admin_conteudos == '1':
                        escolha_conteudo = input("Adicionar conteúdo em (1) conteudos ou (2) conteudos_2: ")
                        titulo = input("Título: ")
                        descricao = input("Descrição: ")
                        tipo = input("Tipo (filme, série, etc.): ")
                        generos = input("Gêneros (separados por vírgula): ").split(",")
                        if escolha_conteudo == '1':
                            adicionar_conteudo(conteudos, titulo, descricao, tipo, generos)
                        elif escolha_conteudo == '2':
                            adicionar_conteudo(conteudos_2, titulo, descricao, tipo, generos)
                        else:
                            print("Opção inválida.")
                            continue
                        print("Conteúdo adicionado com sucesso.")

                    elif opcao_admin_conteudos == '2':
                        id_conteudo = int(input("ID do Conteúdo para alterar: "))
                        if id_conteudo in conteudos:
                            titulo = input("Novo Título (deixe em branco para manter o atual): ")
                            descricao = input("Nova Descrição (deixe em branco para manter a atual): ")
                            tipo = input("Novo Tipo (deixe em branco para manter o atual): ")
                            generos = input("Novos Gêneros (separados por vírgula, deixe em branco para manter os atuais): ")
                            generos = generos.split(",") if generos else None
                            alterar_conteudo(conteudos, id_conteudo, titulo, descricao, tipo, generos)
                            print("Conteúdo alterado com sucesso.")
                        elif id_conteudo in conteudos_2:
                            titulo = input("Novo Título (deixe em branco para manter o atual): ")
                            descricao = input("Nova Descrição (deixe em branco para manter a atual): ")
                            tipo = input("Novo Tipo (deixe em branco para manter o atual): ")
                            generos = input("Novos Gêneros (separados por vírgula, deixe em branco para manter os atuais): ")
                            generos = generos.split(",") if generos else None
                            alterar_conteudo(conteudos_2, id_conteudo, titulo, descricao, tipo, generos)
                            print("Conteúdo alterado com sucesso.")
                        else:
                            print("Conteúdo não encontrado.")

                    elif opcao_admin_conteudos == '3':
                        id_conteudo = int(input("ID do Conteúdo para excluir: "))
                        if excluir_conteudo(conteudos, id_conteudo):
                            print("Conteúdo excluído com sucesso.")
                        elif excluir_conteudo(conteudos_2, id_conteudo):
                            print("Conteúdo excluído com sucesso.")
                        else:
                            print("Erro ao excluir conteúdo.")

                    elif opcao_admin_conteudos == '4':
                        break

                    else:
                        print("Opção inválida. Tente novamente.")
            else:
                print("Acesso negado. Apenas para administradores.")

        elif escolha == '16':
            salvar_dados(usuarios, conteudos, conteudos_2)
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main() 
"""

    
import streamlit as st
from usuario_funcoes import (cadastrar_usuario, login_usuario, excluir_usuario, alterar_senha,
                             adicionar_preferencia, remover_preferencia, adicionar_historico, 
                             listar_conteudos, recomendar_conteudos, buscar_usuario_por_email,
                             alterar_dados_usuario, adicionar_conteudo, alterar_conteudo, excluir_conteudo)
from persistencia import salvar_dados, carregar_dados

def main():
    st.title("Sistema de Gerenciamento de Usuários e Conteúdos")

    # Carregar dados
    usuarios, conteudos, conteudos_2 = carregar_dados()
    st.sidebar.title("Menu")
    menu = ["Cadastrar Usuário", "Login", "Excluir Usuário", "Alterar Senha", "Listar Conteúdos", 
            "Assistir Conteúdo", "Ver Tipo de Assinatura", "Alterar Tipo de Assinatura",
            "Ver Preferências", "Alterar Preferências", "Ver Histórico", 
            "Recomendação por Preferência", "Listar Conteúdos Premium", 
            "Gerenciamento de Usuários (Admin)", "Gerenciamento de Conteúdos (Admin)", "Sair"]
    escolha = st.sidebar.selectbox("Escolha uma opção", menu)

    if 'usuario_logado' not in st.session_state:
        st.session_state.usuario_logado = None

    if escolha == "Cadastrar Usuário":
        st.subheader("Cadastrar Usuário")
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        senha = st.text_input("Senha", type='password')
        tipo_assinatura = st.selectbox("Tipo de Assinatura", ["básica", "premium"])
        if st.button("Cadastrar"):
            if cadastrar_usuario(usuarios, nome, email, senha, tipo_assinatura[0]):
                st.success("Usuário cadastrado com sucesso!")
            else:
                st.error("Erro de cadastro")

    elif escolha == "Login":
        st.subheader("Login")
        email = st.text_input("Email")
        senha = st.text_input("Senha", type='password')
        if st.button("Login"):
            usuario_logado = login_usuario(usuarios, email, senha)
            if usuario_logado:
                st.session_state.usuario_logado = usuario_logado
                st.success("Login bem-sucedido!")
            else:
                st.error("Email ou senha incorretos.")

    elif escolha == "Excluir Usuário":
        st.subheader("Excluir Usuário")
        if st.session_state.usuario_logado and st.button("Excluir"):
            if excluir_usuario(usuarios, st.session_state.usuario_logado.id):
                st.success("Usuário excluído com sucesso.")
                st.session_state.usuario_logado = None
            else:
                st.error("Erro: Usuário não logado ou não autorizado.")

    elif escolha == "Alterar Senha":
        st.subheader("Alterar Senha")
        if st.session_state.usuario_logado:
            nova_senha = st.text_input("Nova senha", type='password')
            if st.button("Alterar"):
                alterar_senha(st.session_state.usuario_logado, nova_senha)
                st.success("Senha alterada com sucesso.")
        else:
            st.error("Erro: Usuário não logado.")

    elif escolha == "Listar Conteúdos":
        st.subheader("Listar Conteúdos")
        conteudos_list = listar_conteudos(conteudos)
        for conteudo in conteudos_list:
            st.write(conteudo)

    elif escolha == "Assistir Conteúdo":
        st.subheader("Assistir Conteúdo")
        if st.session_state.usuario_logado:
            id_conteudo = st.number_input("ID do Conteúdo para assistir", min_value=1, step=1)
            if st.button("Assistir"):
                if id_conteudo in conteudos:
                    adicionar_historico(st.session_state.usuario_logado, id_conteudo)
                    st.success(f"Assistido: {conteudos[id_conteudo].titulo}")
                elif st.session_state.usuario_logado.tipo_assinatura == 'premium' and id_conteudo in conteudos_2:
                    adicionar_historico(st.session_state.usuario_logado, id_conteudo)
                    st.success(f"Assistido: {conteudos_2[id_conteudo].titulo}")
                else:
                    st.error("Conteúdo não encontrado ou acesso não permitido.")
        else:
            st.error("Erro: Usuário não logado.")

    elif escolha == "Ver Tipo de Assinatura":
        st.subheader("Ver Tipo de Assinatura")
        if st.session_state.usuario_logado:
            st.write(f"Tipo de Assinatura: {st.session_state.usuario_logado.tipo_assinatura}")
        else:
            st.error("Erro: Usuário não logado.")

    elif escolha == "Alterar Tipo de Assinatura":
        st.subheader("Alterar Tipo de Assinatura")
        if st.session_state.usuario_logado:
            novo_tipo = st.selectbox("Novo tipo de assinatura", ["básica", "premium"])
            if st.button("Alterar"):
                st.session_state.usuario_logado.tipo_assinatura = novo_tipo
                st.success("Tipo de assinatura atualizado com sucesso.")
        else:
            st.error("Erro: Usuário não logado.")

    elif escolha == "Ver Preferências":
        st.subheader("Ver Preferências")
        if st.session_state.usuario_logado:
            st.write("Preferências:", ', '.join(st.session_state.usuario_logado.preferencias))
            if not st.session_state.usuario_logado.preferencias:
                st.write("Sem preferências")
        else:
            st.error("Erro: Usuário não logado.")

    elif escolha == "Alterar Preferências":
        st.subheader("Alterar Preferências")
        if st.session_state.usuario_logado:
            genero = st.text_input("Gênero para adicionar ou remover").lower()
            acao = st.selectbox("Adicionar ou Remover?", ["Adicionar", "Remover"])

            # Verifica se o gênero existe nos conteúdos
            generos_existentes = set()
            for conteudo in conteudos.values():
                generos_existentes.update(conteudo.generos)
            for conteudo in conteudos_2.values():
                generos_existentes.update(conteudo.generos)

            if genero not in generos_existentes:
                st.error("Gênero inválido. Por favor, escolha um gênero existente.")
            else:
                if acao == 'Adicionar' and st.button("Confirmar"):
                    adicionar_preferencia(st.session_state.usuario_logado, genero)
                    st.success("Preferência adicionada com sucesso.")
                elif acao == 'Remover' and st.button("Confirmar"):
                    remover_preferencia(st.session_state.usuario_logado, genero)
                    st.success("Preferência removida com sucesso.")
        else:
            st.error("Erro: Usuário não logado.")

    elif escolha == "Ver Histórico":
        st.subheader("Ver Histórico")
        if st.session_state.usuario_logado:
            historico = [conteudos[id].titulo for id in st.session_state.usuario_logado.historico if id in conteudos]
            historico += [conteudos_2[id].titulo for id in st.session_state.usuario_logado.historico if id in conteudos_2]
            st.write("Histórico de visualizações:", ', '.join(historico))
        else:
            st.error("Erro: Usuário não logado.")

    elif escolha == "Recomendação por Preferência":
        st.subheader("Recomendação por Preferência")
        if st.session_state.usuario_logado:
            recomendados = recomendar_conteudos(st.session_state.usuario_logado, conteudos)
            if st.session_state.usuario_logado.tipo_assinatura == 'premium':
                recomendados += recomendar_conteudos(st.session_state.usuario_logado, conteudos_2)
            if recomendados:
                st.write("Conteúdos recomendados:")
                for rec in recomendados:
                    st.write(rec)
            else:
                st.write("Nenhum conteúdo corresponde às suas preferências.")
        else:
            st.error("Erro: Usuário não logado.")

    elif escolha == "Listar Conteúdos Premium":
        st.subheader("Listar Conteúdos Premium")
        if st.session_state.usuario_logado and st.session_state.usuario_logado.tipo_assinatura == 'premium':
            conteudos_list = listar_conteudos(conteudos_2)
            for conteudo in conteudos_list:
                st.write(conteudo)
        else:
            st.error("Acesso negado. Apenas para usuários com assinatura premium.")

    elif escolha == "Gerenciamento de Usuários (Admin)":
        st.subheader("Gerenciamento de Usuários (Admin)")
        if st.session_state.usuario_logado and st.session_state.usuario_logado.tipo_user == 'administrador':
            admin_menu = ["Buscar Usuário por Email", "Alterar Dados de Usuário", "Adicionar Novo Usuário", "Excluir Usuário"]
            admin_escolha = st.selectbox("Escolha uma opção", admin_menu)

            if admin_escolha == "Buscar Usuário por Email":
                email = st.text_input("Email do usuário")
                if st.button("Buscar"):
                    usuario_encontrado = buscar_usuario_por_email(usuarios, email)
                    if usuario_encontrado:
                        st.write(f"Usuário encontrado: {usuario_encontrado.__dict__}")
                    else:
                        st.error("Usuário não encontrado.")

            elif admin_escolha == "Alterar Dados de Usuário":
                email = st.text_input("Email do usuário para alterar")
                if st.button("Buscar"):
                    usuario_encontrado = buscar_usuario_por_email(usuarios, email)
                    if usuario_encontrado:
                        nome = st.text_input("Novo Nome", value=usuario_encontrado.nome)
                        novo_email = st.text_input("Novo Email", value=usuario_encontrado.email)
                        senha = st.text_input("Nova Senha", type='password')
                        tipo_assinatura = st.selectbox("Novo Tipo de Assinatura", ["", "básica", "premium"])
                        tipo_user = st.selectbox("Novo Tipo de Usuário", ["", "usuário", "administrador"])
                        if st.button("Alterar"):
                            alterar_dados_usuario(usuario_encontrado, nome, novo_email, senha, tipo_assinatura if tipo_assinatura else None, tipo_user if tipo_user else None)
                            st.success("Dados do usuário alterados com sucesso.")
                    else:
                        st.error("Usuário não encontrado.")

            elif admin_escolha == "Adicionar Novo Usuário":
                nome = st.text_input("Nome")
                email = st.text_input("Email")
                senha = st.text_input("Senha", type='password')
                tipo_assinatura = st.selectbox("Tipo de Assinatura", ["básica", "premium"])
                if st.button("Cadastrar"):
                    if cadastrar_usuario(usuarios, nome, email, senha, tipo_assinatura[0]):
                        st.success("Usuário cadastrado com sucesso!")
                    else:
                        st.error("Erro de cadastro")

            elif admin_escolha == "Excluir Usuário":
                email = st.text_input("Email do usuário para excluir")
                if st.button("Buscar"):
                    usuario_encontrado = buscar_usuario_por_email(usuarios, email)
                    if usuario_encontrado and st.button("Excluir"):
                        if excluir_usuario(usuarios, usuario_encontrado.id):
                            st.success("Usuário excluído com sucesso.")
                        else:
                            st.error("Erro ao excluir usuário.")
                    else:
                        st.error("Usuário não encontrado ou erro ao excluir.")

        else:
            st.error("Acesso negado. Apenas para administradores.")

    elif escolha == "Gerenciamento de Conteúdos (Admin)":
        st.subheader("Gerenciamento de Conteúdos (Admin)")
        if st.session_state.usuario_logado and st.session_state.usuario_logado.tipo_user == 'administrador':
            admin_conteudo_menu = ["Adicionar Novo Conteúdo", "Alterar Conteúdo", "Excluir Conteúdo"]
            admin_conteudo_escolha = st.selectbox("Escolha uma opção", admin_conteudo_menu)

            if admin_conteudo_escolha == "Adicionar Novo Conteúdo":
                escolha_conteudo = st.selectbox("Adicionar conteúdo em", ["conteudos", "conteudos_2"])
                titulo = st.text_input("Título")
                descricao = st.text_input("Descrição")
                tipo = st.text_input("Tipo (filme, série, etc.)")
                generos = st.text_input("Gêneros (separados por vírgula)").split(",")
                if st.button("Adicionar"):
                    if escolha_conteudo == "conteudos":
                        adicionar_conteudo(conteudos, titulo, descricao, tipo, generos)
                    elif escolha_conteudo == "conteudos_2":
                        adicionar_conteudo(conteudos_2, titulo, descricao, tipo, generos)
                    st.success("Conteúdo adicionado com sucesso.")

            elif admin_conteudo_escolha == "Alterar Conteúdo":
                id_conteudo = st.number_input("ID do Conteúdo para alterar", min_value=1, step=1)
                if st.button("Buscar"):
                    conteudo_encontrado = conteudos.get(id_conteudo) or conteudos_2.get(id_conteudo)
                    if conteudo_encontrado:
                        titulo = st.text_input("Novo Título", value=conteudo_encontrado.titulo)
                        descricao = st.text_input("Nova Descrição", value=conteudo_encontrado.descricao)
                        tipo = st.text_input("Novo Tipo", value=conteudo_encontrado.tipo)
                        generos = st.text_input("Novos Gêneros (separados por vírgula)", value=", ".join(conteudo_encontrado.generos)).split(",")
                        if st.button("Alterar"):
                            if id_conteudo in conteudos:
                                alterar_conteudo(conteudos, id_conteudo, titulo, descricao, tipo, generos)
                            else:
                                alterar_conteudo(conteudos_2, id_conteudo, titulo, descricao, tipo, generos)
                            st.success("Conteúdo alterado com sucesso.")
                    else:
                        st.error("Conteúdo não encontrado.")

            elif admin_conteudo_escolha == "Excluir Conteúdo":
                id_conteudo = st.number_input("ID do Conteúdo para excluir", min_value=1, step=1)
                if st.button("Excluir"):
                    if excluir_conteudo(conteudos, id_conteudo) or excluir_conteudo(conteudos_2, id_conteudo):
                        st.success("Conteúdo excluído com sucesso.")
                    else:
                        st.error("Erro ao excluir conteúdo.")

        else:
            st.error("Acesso negado. Apenas para administradores.")

    elif escolha == "Sair":
        salvar_dados(usuarios, conteudos, conteudos_2)
        st.success("Saindo do sistema...")
        st.stop()

if __name__ == "__main__":
    main()
