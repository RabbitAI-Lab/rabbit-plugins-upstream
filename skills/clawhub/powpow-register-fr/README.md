# powpow-register

Assistant d'inscription à PowPow Bulle (édition OpenClaw) : accompagne un nouvel utilisateur depuis « je ne
sais pas ce qu'est Bulle » jusqu'à « compte activé, connecté en un clic, on joue » — présentation du produit
(captures d'écran comprises), inscription déléguée à l'agent (upload de l'avatar compris), commande
d'abonnement Alipay et suivi de l'encaissement, connexion en un clic à double lien, diagnostic des erreurs.

**Depuis la v2.0.0, mode prise en charge déléguée par l'agent** : le script principal `scripts/powpow-register.mjs` est
zéro dépendance (Node ≥ 18), l'utilisateur ne quitte jamais la conversation, à part deux courtes sorties :
aller chercher le code dans sa boîte mail, et payer à la caisse Alipay. Sans Node, ou si l'utilisateur
préfère faire lui-même, repli automatique en mode guide pure.

## Installation

```
openclaw skills install @durenzidu/powpow-register
```

## Fonctionnalités

1. **Présentation du produit** : ouverture en ~120 caractères + captures d'écran embarquées dans le paquet
   (`assets/screenshots/`, 6 images : page de la carte, page de détail d'un post, etc. ; choisir 1–3 images
   selon la scène ; sans hébergeur externe, utilisable hors ligne).
2. **Inscription déléguée** : l'agent propose proactivement nom d'utilisateur/pseudo, mot de passe au choix
   (fourni par l'utilisateur ou généré par l'agent), envoi et soumission du code de vérification, upload
   direct de l'avatar (≤5 Mo, pas de SVG), gestion automatique des erreurs courantes (déjà pris / expiré / limite de fréquence).
3. **Connexion en un clic (double lien)** : dès l'inscription réussie, un lien de « semi-session » mène
   directement à la page d'abonnement ; après encaissement du paiement, on échange contre un nouvel état de
   connexion puis un lien de membership complet mène directement à l'accueil (via le pont officiel
   `me?token=` de la plateforme, qui pose automatiquement le cookie HttpOnly).
4. **Paiement de l'abonnement** : canal Alipay, commande déléguée à l'agent (mensuel ¥6.99 / trimestriel
   ¥19.99 / annuel ¥69.99, achat unique sans renouvellement automatique) + interrogation en boucle jusqu'à
   l'encaissement ; repli vers PayPal pour les utilisateurs à l'étranger ; QR code WeChat / Huawei IAP : on montre le chemin.
5. **Diagnostic des erreurs** : code de vérification non reçu, nom d'utilisateur/e-mail déjà pris, 403 non
   activé, compte verrouillé, etc. — tout vient du code source de la plateforme, sources citées.

## Structure des fichiers

```
powpow-register/
├── SKILL.md                            # Guide principal (conditions de déclenchement, flux en 8 étapes, ton, règles strictes)
├── README.md
├── .clawhubignore
├── assets/
│   └── screenshots/                    # Captures produit embarquées (powpow-01~06.jpg)
├── scripts/
│   └── powpow-register.mjs             # Script principal (zéro dépendance Node≥18, 11 sous-commandes)
└── references/
    ├── agent-flow.md                   # Contrat du script, séquence complète, mécanisme du double lien, conception sécurité
    ├── registration-flow.md            # Règles de champs, limites de fréquence, tableau de diagnostic (sources citées)
    ├── payment-and-activation.md       # Contrat Alipay vibepay, chaîne d'activation, diagnostic des canaux
    └── screenshots.md                  # Inventaire des captures embarquées + consultation rapide par scène
```

## Sécurité

- **Mot de passe** : passé au processus du script uniquement par variable d'environnement, jamais en
  argument de ligne de commande, jamais écrit sur disque, jamais dans le fichier d'état ; le mot de passe
  généré par l'agent n'est affiché qu'une fois, pour que l'utilisateur le sauvegarde.
- **Code de vérification** : utilisé uniquement pour l'interface officielle d'inscription, jeté après
  usage ; le fichier d'état (e-mail/nom d'utilisateur/token/numéro de commande) est stocké dans le
  répertoire temporaire système, effacé d'un coup par `cleanup` en fin de flux.
- **Paiement** : l'agent ne fait que créer la commande, ouvrir la caisse et consulter l'encaissement ; il
  ne touche jamais au compte Alipay de l'utilisateur ni à ses moyens de paiement, et ne paie jamais à sa
  place. Le paiement se fait toujours entre l'utilisateur et la caisse officielle Alipay.
- Toutes les requêtes ne partent que vers le domaine officiel `https://global.powpow.online` ; aucune clé n'est incluse.

## Licence

MIT-0 (licence unifiée ClawHub).

## Liens

- Site officiel : https://global.powpow.online
- Inscription : https://global.powpow.online/register
- Découvrir Bulle (vidéo) : https://www.bilibili.com/video/BV1Wu826UEVz/
