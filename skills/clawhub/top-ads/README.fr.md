# Denote Top Ads

[EN](README.md) · [ZH](README.zh.md) · [JA](README.ja.md) · [KO](README.ko.md) · [ES](README.es.md) · [NL](README.nl.md) · [DE](README.de.md) · FR

Repérez des créations publicitaires à étudier pour votre prochaine campagne. Denote suit plus de 10 millions de publicités et actualise ses classements chaque semaine. Avec un compte gratuit, consultez trois classements de jeux ou d’applications pour la dernière semaine complète, avec jusqu’à dix publicités par classement. [Découvrir Denote Top Ads](https://denote.net/top-ads).

![Accédez aux trois classements hebdomadaires depuis le menu latéral.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/top-ads-navigation.jpg)

*Accédez aux trois classements hebdomadaires depuis le menu latéral.*

| Classement gratuit | Ce que vous y trouverez |
| --- | --- |
| Publicités populaires | Les créations qui ont suscité le plus d’intérêt la semaine dernière. |
| Publicités en progression | Celles dont la popularité a le plus augmenté par rapport à la semaine précédente. |
| Nouvelles publicités | Les créations repérées pour la première fois, classées selon leur popularité initiale. |

![Publicités de jeux les plus populaires du 9 au 15 novembre 2026, par popularité hebdomadaire.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/trending-ads.jpg)

*Publicités de jeux les plus populaires du 9 au 15 novembre 2026, par popularité hebdomadaire.*

![Publicités de jeux dont la popularité a le plus progressé par rapport à la semaine précédente.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/rising-ads.jpg)

*Publicités de jeux dont la popularité a le plus progressé par rapport à la semaine précédente.*

![Publicités de jeux nouvellement repérées, classées selon leur popularité initiale.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/new-ads.jpg)

*Publicités de jeux nouvellement repérées, classées selon leur popularité initiale.*

## Obtenir vos premiers classements

Exécutez cette commande dans votre espace de travail OpenClaw. Python 3 est nécessaire.

```sh
git clone https://github.com/Denote-Business/denote-top-ads.git skills/denote-top-ads
```

1. Ouvrez une nouvelle session et demandez « Quelles publicités puis-je découvrir avec Denote ? ».
2. [Créer un compte Denote gratuit](https://denote.net/user/register). Si vous avez déjà un compte, connectez-vous. Créez une clé API Denote avec l’autorisation `top_ads:read` ou ajoutez cette autorisation à une clé existante.
3. Enregistrez la clé sous le nom `DENOTE_API_KEY` dans le gestionnaire de secrets de votre agent. Demandez ensuite « Montre-moi les publicités d’applications de la semaine dernière ». Vous obtiendrez les trois classements. Par défaut, la catégorie choisie est celle des jeux.

**Rang · Titre · Annonceur · Format · Plateformes · Aperçu**

## Examiner une publicité en détail

Essayez « Ouvre la deuxième publicité en progression ». Avec Top Ads Pro ou Business, vous pouvez consulter les données disponibles sur les performances et l’audience. Les trois classements hebdomadaires sont gratuits.

![Vue d’ensemble de la création Vita Mahjong, avec son format et ses impressions estimées.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/overview.jpg)

*Vue d’ensemble de la création Vita Mahjong, avec son format et ses impressions estimées.*

![Évolution du score quotidien de Vita Mahjong par rapport aux courbes de référence.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/data-trend.jpg)

*Évolution du score quotidien de Vita Mahjong par rapport aux courbes de référence.*

![Publicités utilisant la même création, avec leurs annonceurs et leurs dates de diffusion.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/related-ads.jpg)

*Publicités utilisant la même création, avec leurs annonceurs et leurs dates de diffusion.*

![Couverture de Vita Mahjong par pays, âge et genre.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/audience.jpg)

*Couverture de Vita Mahjong par pays, âge et genre.*
