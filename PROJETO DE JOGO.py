print("Ao chegar do seu curso noturno de Engenharia da computação na Fiap, você faz suas últimas tarefas do dia e se "
      "deita para dormir. Porêm ao acordar, algo esta diferente. Você está em  mundo completamente novo com uma grande "
      "opção em sua visão"
      )
escolha1 = input(" Escolha seu sexo: (homem/mulher/nerdola)")
print("Seu sexo ira mudar a continuidade da historia")

if escolha1 == "homem":
    print("Ao realizar sua escolha, voce percebe estar em um quarto de motel, você se levanta, caminha ate a porta"
          " e sai do quarto a procura de outros humanos.")
    print(" Apos descer 2 lances de escada, voce se encontra na praça de alimentação do motel, e descobre que esta em"
          "mundo quase igual ao seu antigo, porem com diversos aspectos magicos.")
    print(" voce se direciona a imagem feminina que estava atras de um grande balcão para perguntar como chegou la,"
          " e depois uma longa conversa, sem resultados, você descobre que para ganhar dinheiro e conseguir sobreviver"
          " você precisaria aprender lutar ou trabalhar como lixeiro")
    escolha2 = input("Você deseja: (aprender a lutar/trabalhar como lixeiro)?")
    if escolha2 == "trabalhar como lixeiro":
        print("A moça te da uma vassoura, um rodo e um balde, e manda voce ir catar lixo na rua, e assim voce faz.")
        print("Depois de um longo dia trabalhando, recebendo ao que se parecia cinco reais. voce se questiona")
        escolha2 = input("Sera que eu quero: (continuar como lixeiro/aprender a lutar)?")
    if escolha2 == "aprender a lutar":
        print("Qual acha mais interessante?")
        escolha3 = input("Voce deseja: (aprender magia/luta corpo a corpo)?")
        if escolha3 == "aprender magia":
            print("Apos falar que queria aprender magia, a moça te da um mapa com um caminho marcado, que levava ate a"
                  "escola de magia da cidade.")
            print("Quando finalmente voce chega a escola de magia, voce realiza sua matricula e se direciona ate"
                  "os dormitorios da escola, e deita em sua cama para relaxar, porem acaba dormindo.")
        if escolha3 == "lutar corpo a corpo":
            print("Apos falar que queria aprender a lutar corpo a corpo, a moça te da um mapa com um caminho "
                  "marcado, que levava ate a academia da cidade, tinha um nome que voce conhecia estampado na "
                  "frente da loja. Estava estanpado 'Renato Cariani's point'")
            print("Quando finalmente voce chega a academia, voce realiza sua matricula e se direciona ate"
                  "os vestiarios, e observa uns homems muito fortes cheirando um pó branco, voce se aproxima e pede"
                  "um pouco, e apos dar uma cheirada em uma grande linha do pó branco, voce apaga.")

if escolha1 == "mulher":
    print("Voce acorda em um grande quarto de luxo, parecia ser uma mansao, sem entender nada, voc desce as escadas"
          ", chega na sala e se encontra com um casal, que te tratavam como filha.")
    print("Sem entender nada, voce questiona eles de como vc foi parar la, porem eles nao sabem responder."
          "apenas dizem que se tinha alguem que conseguiria responder, seria o grande profeta das longiquas terras"
          "'Escobar's Land', porem para chegar la, voce precisaria aprender magia ou lutar corpo a corpo")
    escolha2 = input("deseja aprender: (magia/lutar)?")
    if escolha2 == "magia":
        print("Vamos contratar um professor particular agora, amanha começa suas aulas")
        print("Voce se direciona a imensa biblioteca da mansão e apos passar o dia todo lendo, voce percebe que "
              "nao sabe o nome de seus pais")
        print("No caminho do quarto de seus pais, voces se econtram no corredor, e ao perguntar o nome, ele responde"
              "'Eu sou o Renato Cariani filha, e sua mae se chama Julio Balestrin nao se recorda?' ")
        print('Depois de descobrir o nome deles, voce se direciona ao mesmo quarto em que acordou e deita para dormir,'
              " acordando somento no outro dia")
    if escolha2 == "lutar":
        print("Entao amanha mesmo iremos a minha academia e voce ira aprender tudo filha.")
        print("Voce se direciona ao imenso jardim da mansão e apos passar o dia todo dando soquinhos em um saco de boxe"
              ", voce percebe que nao sabe o nome de seus pais")
        print("No caminho do quarto de seus pais, voces se econtram no corredor, e ao perguntar o nome, ele responde"
              "'Eu sou o Renato Cariani filha, e sua mae se chama Julio Balestrin nao se recorda?' ")
        print('Depois de descobrir o nome deles, voce se direciona ao mesmo quarto em que acordou e deita para dormir,'
              " acordando somento no outro dia")

if escolha1 == "nerdola":
    print("Voce acorda em uma caverna, fria, molhada e humida, com um pilha de livros em sua volta")
    print("Como era sua unica opção, voce le todos os livros repetidamente, alguns livros eram de magias iniciantes"
          "outros eram sobre tecnicas de combate, e outros eram sobre historia e geografia.")
    print('depois de passar semanas lendo as mesmas coisas, voce decide colocar em pratica, e percebe que '
          'consegue lutar muito bem, e utilizar magias melhor ainda.')
    print("Voce decide se dar 1 semana de ferias, entao deita sobre uma cama de paplah improvisada feita por voce mesmo"
          "com uma cesta de palha cheia de frutas ao lado, e dorme.")

        