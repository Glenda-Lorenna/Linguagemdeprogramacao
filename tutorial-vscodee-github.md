# 🚀 Guia Iniciante: Configurando VS Code + GitHub

Este tutorial foi criado para quem está começando na **Linguagem de Programação** e precisa aprender a salvar seus códigos (como os exercícios de Python) de forma segura e organizada no GitHub.

---

## 🛠️ 1. Instalação das Ferramentas Essenciais
Para começar, você precisa de dois programas instalados no seu Windows:

1. **Visual Studio Code (VS Code):** É o seu editor de texto.
   * [Baixe aqui](https://code.visualstudio.com/)
2. **Git:** É o sistema que registra as versões do seu código e faz a ponte com a internet.
   * [Baixe aqui](https://git-scm.com/)
   * *Dica:* Na instalação, pode clicar em "Next" em todas as opções padrão.

## 💡 Entenda a Diferença: Git versus GitHub

Para não se confundir:
* **Git (Download):** É o software que instalamos no Windows. Ele controla as versões dos seus arquivos localmente.
* **GitHub (Online):** É o site onde hospedamos nossos códigos. Você não baixa o "GitHub", você cria uma conta nele para sincronizar seus projetos.
* **VS Code (Ferramenta):** É onde você escreve o código e usa o Terminal para "conversar" com o Git.

---

## 👤 2. Configurando sua Identidade
O Git precisa saber quem é o autor do código. Abra o terminal do VS Code (`Ctrl + '`) e digite os comandos abaixo (substitua pelo seu nome e e-mail do GitHub):

```bash
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu-email@exemplo.com"

--- 
```

## 🔗 3. Conectando o VS Code ao GitHub (Online)

O **GitHub** funciona de forma 100% online (na nuvem). Para que o **VS Code** consiga enviar seus arquivos para o site sem erros, você precisa "apresentar" um ao outro.

1. **Acesso Online:** Certifique-se de que você já criou sua conta no [github.com](https://github.com).
2. **Login pelo VS Code:** 
   * No canto inferior esquerdo do VS Code, clique no ícone de **Contas** (bonequinho).
   * Selecione **Sign in to Sync Settings** ou tente realizar o seu primeiro `push`.
   * O VS Code abrirá uma janela no seu navegador padrão. Clique em **Authorize GitHub**.
3. **Confirmação:** Uma mensagem aparecerá perguntando se deseja abrir o VS Code. Clique em **Abrir**. Agora seu editor tem permissão para "conversar" com sua conta online.

---

## 🔁 4. O Fluxo de Trabalho (Comandos no Terminal)

Agora que as ferramentas estão ligadas, este é o "ritual" que você fará sempre que terminar um exercício de programação. Abra o terminal (`Ctrl + '`) e siga estes passos:

### 🔄 Passo 1: Sincronizar (`git pull`)
Antes de enviar qualquer coisa, você deve baixar o que existe no site para o seu computador. Isso evita conflitos de versão.
```bash
git pull origin main 

```

### ➕ Passo 2: Adicionar arquivos ('git add')
Nesse passo é informado os arquivos que vão ser enviados ao repositório.

O ponto utilizado no final informa que todos os arquivos da pasta serão adicionados.
```bash
git add .

```

### 💾 Passo 3: Criar um Commit ('git commit')
O commit é o registro das alterações feitas, logo deve informar entre aspas normais o que foi alterado. 

O comando abaixo demonstra em forma de exemplo.
```bash
git commit -m "Adiciona exercícios de repetição"

```

### 🚀 Passo 4: Enviar para o GitHub ('git push')
Por último se envia as alterações para o repositório no GitHub.
```bash
git push origin main

```

* 📌 Observação: Para enviar uma alteração da pasta para o repositório segue os mesmos passos acima, apenas é recomendável antes do passo 1, que execute no terminal VScode o comando ('git status'), para visualizar as alterações realizadas.


## 🎯 Conclusão

Através desse tutorial foi possível desenvolver as seguintes práticas:

- ✔️ Configurar o VS Code e o Git
- ✔️ Conectar ao GitHub
- ✔️ Utilizar o fluxo básico de versionamento
- ✔️ Enviar seus códigos para a nuvem com segurança

Com esses conhecimentos, o estudante consegue organizar seus exercícios e construir seu portfólio no GitHub.