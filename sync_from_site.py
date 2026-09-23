#!/usr/bin/env python3
"""Gera as páginas de privacy.raptrak.me a partir do build do site (raptrak.me).

Cada página antiga vira uma cópia da página nova com redirect imediato pra raptrak.me
(preservando ?token=&email= dos links de e-mail). O HTML mantém o texto completo, então
quem não segue redirect (ex.: o robô do Google Play) continua lendo a política atual.

Uso: (cd ../raptrak-site && npm run build) && python3 sync_from_site.py
"""
import pathlib
import re

SITE = 'https://raptrak.me'
DIST = pathlib.Path(__file__).resolve().parent.parent / 'raptrak-site' / 'dist'
OUT = pathlib.Path(__file__).resolve().parent

# página antiga -> caminho no site novo
MAP = {
    'index.html': '/',
    'privacy-policy/index.html': '/privacy-policy',
    'index-data-deletion.html': '/data-deletion',
    'verified-data-deletion.html': '/data-deletion/verify',
}


def build(target: str) -> str:
    src = DIST / target.strip('/') / 'index.html' if target != '/' else DIST / 'index.html'
    html = src.read_text(encoding='utf-8')
    # URLs relativas à raiz passam a apontar pro site novo.
    html = re.sub(r'(href|src)="/(?!/)', rf'\1="{SITE}/', html)
    url = SITE + (target if target != '/' else '/')
    redirect = (
        f'<meta http-equiv="refresh" content="0; url={url}">'
        f'<script>location.replace({url!r} + location.search + location.hash)</script>'
    )
    return html.replace('<head>', '<head>' + redirect, 1)


def main() -> None:
    for old, target in MAP.items():
        dest = OUT / old
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(build(target), encoding='utf-8')
        print(f'{old} -> {SITE}{target}')


if __name__ == '__main__':
    main()
