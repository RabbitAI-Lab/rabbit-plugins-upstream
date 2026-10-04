# powpow-register

L'assistant d'inscription Bubble de PowPow (édition OpenClaw) : fait passer un nouvel utilisateur de « je ne sais pas ce qu'est Bubble » à « compte activé et prêt à l'emploi » — présentation du produit (avec captures d'écran de l'interface), accompagnement pas à pas de l'inscription, résolution des erreurs et explication de l'activation de l'abonnement.

Skill purement indicatif, sans script ni dépendance ; toutes les actions d'inscription sont effectuées par l'utilisateur dans le navigateur/l'application.

## Installation

```
openclaw skills install @durenzidu/powpow-register
```

## Fonctionnalités

1. **Présentation du produit** : introduction d'environ 120 caractères + liens de captures hébergées dans un dépôt GitHub public (6 images : page carte, page de détail d'un post, etc. ; envoyez-en 1 à 3 selon le contexte).
2. **Accompagnement à l'inscription** : règles des champs (nom d'utilisateur / mot de passe / code de vérification e-mail / téléphone / avatar), connexion tierce (Google / Watcha / Huawei), paramètres de limitation de débit — le tout issu du code source de la plateforme, avec sources citées.
3. **Résolution des erreurs** : 13 problèmes courants, dont code de vérification non reçu, nom d'utilisateur / e-mail déjà utilisé, 403 non activé, compte verrouillé.
4. **Activation de l'abonnement** : trois canaux — PayPal (web) / QR code WeChat (confirmation manuelle) / IAP Huawei (HarmonyOS) — avec explications et dépannage ; la chaîne de paiement existante est réutilisée telle quelle, le skill se contente de montrer le chemin.

## Structure des fichiers

```
powpow-register/
├── SKILL.md                            # Guide principal (déclencheurs, parcours, règles de ton)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # Règles des champs, limitations, tableau des erreurs (avec sources)
    ├── payment-and-activation.md       # Activation de l'abonnement, canaux de paiement, conclusion de réutilisation
    └── screenshots.md                  # Liste des captures hébergées + aide-mémoire par scénario
```

## Sécurité

- Ne contient aucun secret ; aucun script, ne touche jamais aux identifiants de l'utilisateur.
- **Ne demandez jamais** le mot de passe, le code de vérification ou les justificatifs de paiement de l'utilisateur ; l'inscription et le paiement se font entièrement sur les pages de la plateforme.

## Licence

MIT-0 (licence unifiée ClawHub).

## Liens

- Site officiel : https://global.powpow.online
- Inscription : https://global.powpow.online/register
- Découvrir Bubble (vidéo) : https://www.bilibili.com/video/BV1Wu826UEVz/