#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from baseconf import *
from collections import OrderedDict

# Configurações Base
SITENAME = u'Grupy-SE'
AUTHOR = u'Grupy-SE'
THEME = "themes/malt"
MALT_BASE_COLOR = "light-blue"

# Referências à Github
GITHUB_REPO = "http://github.com/pug-se/pug-se"
GITHUB_BRANCH = "master"

# Imagens
ARTICLE_BANNERS_FOLDER = "images/banners"
SITE_LOGO = "images/logo.png"
SITE_LOGO_MOBILE = "images/logo-mobile.png"

# Home settings
WELCOME_TITLE = "Seja bem vindo ao {}".format(SITENAME)
WELCOME_TEXT = "Grupo de usuários da linguagem Python em Sergipe."
SITE_BACKGROUND_IMAGE = "images/banners/background.png"
FOOTER_ABOUT = "O Grupy-SE (anteriormente PUG-SE) é uma iniciativa " +\
               "comunitária que tem o objetivo de reunir os desenvolvedores " +\
               "e demais interessados na linguagem de programação Python " +\
               "e em suas tecnologias associadas."

# Tema do Syntax Hightlight
PYGMENTS_STYLE = "perldoc"

# Navbar Links da Home Page
NAVBAR_HOME_LINKS = [
    {
        "title": "Comunidade",
        "href": "comunidade",
    },
    {
        "title": "Membros",
        "href": "membros",
    },
    {
        "title": "Blog",
        "href": "blog",
    },
]

# Navbar Links do Blog
NAVBAR_BLOG_LINKS = NAVBAR_HOME_LINKS + [
    {
        "title": "Categorias",
        "href": "blog/categorias",
    },
    {
        "title": "Autores",
        "href": "blog/autores",
    },
    {
        "title": "Tags",
        "href": "blog/tags",
    },
]

# Links sociais do rodapé
SOCIAL_LINKS = (
    {
        "href": "https://telegram.me/joinchat/Acry5z79kyPZDqK4Bgu9FQ",
        "icon": "fa-paper-plane",
        "text": "Telegram",
    },
    {
        "href": "https://www.meetup.com/pug-se",
        "icon": "fa-meetup",
        "text": "Meetup",
    },
    {
        "href": "https://github.com/pug-se",
        "icon": "fa-github",
        "text": "GitHub",
    },
    {
        "href": "https://www.facebook.com/groups/pugse",
        "icon": "fa-facebook",
        "text": "Facebook",
    },
    {
        "href": "https://groups.google.com/forum/#!forum/pug-se",
        "icon": "fa-envelope",
        "text": "Mailing List",
    },
)

# Links úteis
USEFUL_LINKS = (
  {
      "href": "http://wiki.python.org.br/",
      "icon": "fa-globe",
      "text": "Python Brasil",
  },
  {
      "href": "https://python.org",
      "icon": "fa-globe",
      "text": "Python",
  },
  {
    "href": "http://2017.pythonbrasil.org.br/",
    "icon": "fa-globe",
    "text": "Python Brasil 2017"
  }
)

# Membros do Grupy
MEMBROS = OrderedDict((
    ("Rodrigo Amaral", {
        "twitter": "@rodrigoamaral",
        "github": "rodrigoamaral",
        "site": {
            "nome": "Rodrigo Amaral",
            "href": "http://rodrigoamaral.net",
            }
        }),
    ("Erick Mendonça", {
        "twitter": "@erickmagnus",
        "github": "erickmendonca",
        "site": {
            "nome": "Erick Mendonça",
            "href": "https://medium.com/@erickmendonca",
            }
        }),
    ("Gabriel Araujo", {
        "email": "gabrielaraujof@outlook.com",
        "twitter": "@gabrielfeear",
        "github": "gabrielaraujof",
        "site": {
            "nome": "Gabriel Araujo",
            "href": "http://blog.gbiel.com",
            }
        }),
    ("Wagner Macedo", {
        "email": "wagnerluis1982@gmail.com",
        "github": "wagnerluis1982",
        }),
))

MALT_HOME = [
    {
        "color": "blue-grey lighten-5",
        "title": "O que Fazemos?",
        "items": [
            {
                "title": "Comunidade",
                "icon": "fa-comments",
                "text": "Nos comunicamos através de mailing " +\
                    "lists e redes sociais além de que são " +\
                    "promovidos encontros diversos, como encontros casuais, " +\
                    "<em>coding dojos</em> e palestras. ",
                "buttons": [
                    {
                        "text": "Saiba Mais",
                        "href": "comunidade",
                    },
                ],
            },
            {
                "title": "Membros",
                "icon": "fa-users",
                "text": "A comunidade Grupy-SE possui alguns " +\
                        "colaboradores principais, responsáveis por organizar " +\
                        "eventos, manter a comunicação ativa, divulgar eventos, " +\
                        "redes sociais e etc. ",
                "buttons": [
                    {
                        "text": "Conheça",
                        "href": "membros",
                    },
                ],
            },
            {
                "title": "Chamada de trabalhos",
                "icon": "fa-puzzle-piece",
                "text": "Estamos selecionando palestras e sugestões de atividades para " +\
                        "os próximos encontros do Grupy-SE. Sinta-se convidado para " +\
                        "compartilhar com a nossa comunidade.",
                "buttons": [
                    {
                        "text": "Submeta",
                        "href": "http://goo.gl/forms/rFvQ3BkSGQ",
                    },
                ],
            },
        ]
    },
    ]

MALT_COMUNITY = [
    {
        "color": "blue-grey lighten-5",
        "items": [
            {
                "title": "Mídias sociais",
                "text": "Siga o Grupy-SE nas mídias sociais para ficar por dentro " +\
                        "dos encontros, novidades e postagens do nosso blog.",
                "buttons": [
                    {
                        "text": "Meetup",
                        "icon": "fa-meetup",
                        "href": "https://www.meetup.com/pug-se/",
                    },
                    {
                        "text": "Facebook",
                        "icon": "fa-facebook",
                        "href": "http://www.facebook.com/groups/pugse/",
                    },
                ],
            },
            {
                "title": "Telegram",
                "text": "Possuimos também um grupo no Telegram. " +\
                        "Para participar é só clicar no link abaixo.",
                "buttons": [
                    {
                        "text": "Telegram",
                        "icon": "fa-paper-plane",
                        "href": "https://telegram.me/joinchat/Acry5z79kyPZDqK4Bgu9FQ",
                    },
                ],
            },
            {
                "title": "Lista de emails",
                "text": "Para quem curte o bom e velho email, temos a lista " +\
                        "de discussão oficial do Grupy-SE no google groups.",
                "buttons": [
                    {
                        "text": "Lista",
                        "icon": "fa-envelope",
                        "href": "https://groups.google.com/forum/#!forum/pug-se",
                    },
                ],
            },
        ]
    },
    ]

from themes.malt.functions import *
