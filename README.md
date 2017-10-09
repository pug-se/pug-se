pug-se
======

Este é o repositório do código-fonte do site do PUG-SE. O site estático é gerado pela biblioteca [Pelican](http://getpelican.com) a partir de arquivos texto no formato [Markdown](http://daringfireball.net/projects/markdown/).


## Requirements

- Python >= 2.7;
- [Cookiecutter](https://github.com/audreyr/cookiecutter);
- [Pelican 2.6](https://github.com/getpelican/pelican);
- Tema [Malt](https://github.com/pug-se/malt);



### Preparando o ambiente de desenvolvimento

Para facilitar o desenvolvimento, é recomendável criar um ambiente virtual separado utilizando o [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/). No exemplo a seguir, criamos um ambiente chamado `pug-se`:

    $ mkvirtualenv --python=python --no-site-packages pug-se

Uma vez criado o ambiente virtual com o comando acima, ele deve estar automaticamente ativado. Caso não esteja, e sempre que se quiser ativá-lo, fazemos:

    $ workon pug-se

> #### Utilizando o [Pyenv](https://github.com/pyenv/pyenv) + [Virtualenv](https://github.com/pyenv/pyenv-virtualenv)
> 
> Outra maneira de preparar o ambiente é utilizando o pyenv. Ele facilita bastante o gerenciamento de versões do python em uma única máquina e mais ainda quando a raiz do projeto tem um arquivo `.python-version` com o nome do ambiente virtual que criamos, pois o Pyenv automaticamente ativa esse ambiente quando estramos na pasta.


Em seguida, clonamos o repositório:

    (pug-se)$ git clone --recursive https://github.com/pug-se/pug-se.git

Será criada a cópia local na qual iremos trabalhar:

    (pug-se)$ cd pug-se

A instalação das dependências é feita utilizando o [pip](http://www.pip-installer.org/en/latest/):

    (pug-se)$ pip install -r requirements.txt

Após este passo, os módulos Pelican, Markdown e demais dependências necessárias estarão instalados no ambiente virtual criado previamente com o virtualenvwrapper.

### Testando a instalação e visualizando o site

O Pelican vem com um pequeno servidor de desenvolvimento para facilitar a atualização dos arquivos HTML estáticos gerados. Para iniciar o servidor, é recomendado utililzar o Makefile que acompanha o código. Entre outras, o Makefile disponibiliza regras como o `html` (que gera nosso site) e o `serve` (que inicia um servidor local para servir o site):

    (pug-se)$ make html serve

Neste ponto, a geração dos arquivos estáticos do site foi realizada (ver conteúdo do diretório pug-se.github.io) e o servidor deve estar rodando em background, aceitando requisições em [http://localhost:5100](http://localhost:5100).

### Criando e modificando conteúdo

A [documentação do Pelican](http://docs.getpelican.com/en/3.2/getting_started.html#writing-content-using-pelican) é bastante completa nesse ponto. Em caso de dúvidas, pedimos que poste sua pergunta nas [issues](https://github.com/pug-se/pug-se/issues) do projeto, de preferência marcando-a com o label *question*.

### Quer contribuir?

Escolha uma [issue](https://github.com/pug-se/pug-se/issues) para resolver ou então crie uma nova para reportar erros ou sugerir melhorias. Todas as sugestões são bem vindas!
