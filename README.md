# Meu Site

Site estático gerado com [Pelican](https://getpelican.com/).

## Desenvolvimento local

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

pelican content -o output -s pelicanconf.py -listen
```

Acesse `http://localhost:8000`.

## Build de produção

```bash
pelican content -o output -s publishconf.py
```

O deploy para o GitHub Pages é automatizado via GitHub Actions (`.github/workflows/pages.yml`) a cada push na branch `main`.

## Estrutura

```
content/
├── articles/   # posts do blog
├── pages/      # páginas estáticas (ex: Sobre)
└── images/     # imagens usadas no conteúdo
pelicanconf.py  # configuração de desenvolvimento
publishconf.py  # configuração de produção
```
