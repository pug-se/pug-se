pug-se
======

Este é o repositório do código-fonte do site do PUG-SE. O site estático é gerado pela biblioteca [Pelican](http://getpelican.com) a partir de arquivos texto no formato [Markdown](http://daringfireball.net/projects/markdown/).

### Preparando o ambiente de desenvolvimento

Para facilitar o desenvolvimento, é recomendável criar um ambiente virtual separado utilizando o [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/). No exemplo a seguir, criamos um ambiente chamado `pug-se`:

    $ mkvirtualenv --python=python3 --no-site-packages pug-se

Como forma de incentivar o uso, o site foi criado para rodar em **[Python 3](http://docs.python.org/3/)** por padrão. Por isso, note que estamos dizendo ao virtualenv que queremos usar Python 3 para criar o ambiente. Uma vez criado o ambiente virtual com o comando acima, ele deve estar automaticamente ativado. Caso não esteja, e sempre que se quiser ativá-lo, fazemos:

    $ workon pug-se

Em seguida, clonamos o repositório:

    (pug-se)$ git clone https://github.com/pug-se/pug-se.git

Será criada a cópia local na qual iremos trabalhar:

    (pug-se)$ cd pug-se

A instalação das dependências é feita utilizando o [pip](http://www.pip-installer.org/en/latest/):

    (pug-se)$ pip install -r requirements.txt

Após este passo, os módulos Pelican, Markdown e demais dependências necessárias estarão instalados no ambiente virtual criado previamente com o virtualenvwrapper.

### Testando a instalação e visualizando o site

O Pelican vem com um pequeno servidor de desenvolvimento para facilitar a atualização dos arquivos HTML estáticos gerados. Para iniciar o servidor, é recomendado utililzar o Makefile que acompanha o código. Entre outras, o Makefile disponibiliza uma regra chamada `devserver`:

    (pug-se)$ make devserver

Neste ponto, a geração dos arquivos estáticos do site foi realizada (ver conteúdo do diretório pug-se.github.io) e o servidor deve estar rodando em background, aceitando requisições em [http://localhost:8000](http://localhost:8000). Para parar o servidor, fazemos:

	(pug-se)$ ./develop_server.sh stop

Caso ocorra algum problema ao iniciar o servidor, certifique-se de que o ambiente virtual foi criado com a opção `--python=python3`. Se por acaso desejar testar o site com o Python 2, procure nos arquivos `Makefile` e `develop_server.sh` a linha:
    
    PY=python3

E, assumindo que a versão padrão do Python no seu sistema é a 2.x, substitua por:

    PY=python

### Criando e modificando conteúdo

A [documentação do Pelican](http://docs.getpelican.com/en/3.2/getting_started.html#writing-content-using-pelican) é bastante completa nesse ponto. Em caso de dúvidas, pedimos que poste sua pergunta nas [issues](https://github.com/pug-se/pug-se/issues) do projeto, de preferência marcando-a com o label *question*.

### Quer contribuir?

Escolha uma [issue](https://github.com/pug-se/pug-se/issues) para resolver ou então crie uma nova para reportar erros ou sugerir melhorias. Todas as sugestões são bem vindas!
