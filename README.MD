# DomainCheckr

**DomainCheckr** é uma ferramenta simples e eficaz que permite verificar a disponibilidade de domínios na internet. Este script suporta várias extensões populares, como `.com`, `.net`, `.org`, entre outras.

## Funcionalidade

A principal funcionalidade do **DomainCheckr** é permitir que o utilizador verifique se um determinado domínio está disponível para registo. Ele tenta registar o domínio em várias extensões populares e exibe se o domínio está disponível ou já foi registado.

## Instalação

### 1. Clone o repositório

Clone o repositório do GitHub com o seguinte comando:
git clone https://github.com/jcastroo/DomainCheckr.git


### 2. Navegue para a pasta do repositório

Depois de clonar, entre na pasta do repositório:
cd DomainCheckr


### 3. Instale as dependências

Instale as dependências com o comando:
pip install .



> **Nota**: Certifique-se de ter o Python 3.x instalado.

## Utilização

Depois de instalar o **DomainCheckr**, pode utilizar o comando `domaincheckr` diretamente na linha de comando para verificar a disponibilidade de um domínio.

### Sintaxe

domaincheckr <dominio>

Onde `<dominio>` é o nome do domínio que deseja verificar (sem a extensão).

### Exemplo

Se quiser verificar a disponibilidade do domínio `exemplo`, execute o seguinte comando:

domaincheckr exemplo

O script irá verificar as extensões seguintes: `.com`, `.net`, `.org`, `.info`, `.co`, `.io` e mostrar se o domínio está disponível ou já foi registado.

### Resultado

O **DomainCheckr** mostrará os domínios disponíveis a verde e os domínios já registados a vermelho.

## Contribuição

Se quiser contribuir para o **DomainCheckr**, sinta-se à vontade para abrir *issues* ou *pull requests*.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## Autor

- **João Castro** - [@jcastroo](https://github.com/jcastroo)


