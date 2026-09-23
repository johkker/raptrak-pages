# raptrak-pages

`privacy.raptrak.me` redireciona para o site oficial, **raptrak.me** (repo `johkker.github.io`, pasta local `raptrak-site`).

Cada página antiga é uma cópia da nova com redirect imediato, preservando `?token=&email=` dos links de e-mail. O texto completo continua no HTML, então quem não segue redirect (ex.: o robô do Google Play) lê a política atual.

Para atualizar depois de mudar o site:

```sh
(cd ../raptrak-site && npm run build) && python3 sync_from_site.py
```
