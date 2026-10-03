---
name: powpow-register
description: Aide les utilisateurs à créer un compte PowPow (Bubble) et à finaliser l'activation de leur abonnement. Se déclenche quand l'utilisateur dit « s'inscrire à Bubble », « créer un compte powpow », « comment s'inscrire sur Bubble », « aide-moi à créer un compte powpow », « sign up powpow » ; gère aussi les problèmes pendant l'inscription (code de vérification non reçu, nom d'utilisateur/e-mail déjà utilisé, format de mot de passe invalide) et après l'inscription (connexion qui indique « compte non activé » / pending_payment, comment s'abonner/payer). Skill purement indicatif : présentation du produit (avec captures d'écran) → accompagnement pas à pas de l'inscription → résolution des erreurs → activation de l'abonnement. Ne couvre pas la publication de posts / la création d'humains numériques (c'est le rôle de powpow-simple), ni le développement de code.
version: 1.0.1
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Assistance à l'inscription Bubble)

Fait passer un nouvel utilisateur de « je ne sais pas ce qu'est Bubble » à « compte activé et prêt à l'emploi ».

**Version 1.0.0** · 2026-09-23 (détails du parcours d'inscription et résolution des erreurs voir `references/registration-flow.md` ; activation de l'abonnement et canaux de paiement voir `references/payment-and-activation.md` ; liste des captures d'écran du produit voir `references/screenshots.md`)

## Environnement d'exécution

Ce skill est **purement indicatif** : aucun script, aucune dépendance Node ou autre. Toutes les actions (remplir les formulaires, recevoir le code de vérification, payer) sont effectuées par l'utilisateur dans le navigateur/l'application ; vous vous chargez de la présentation, des indications et du dépannage.

## Conditions de déclenchement

- Intention d'inscription : « s'inscrire à Bubble », « créer un compte powpow », « comment s'inscrire sur Bubble », « sign up powpow »
- Inscription bloquée : « je ne reçois pas le code de vérification », « le nom d'utilisateur est déjà pris », « le mot de passe est toujours refusé »
- Problèmes après l'inscription : « la connexion indique compte non activé », « 403 pending_payment », « comment payer / s'abonner à Bubble »

**Ne se déclenche pas** : publier des posts / créer des humains numériques (→ powpow-simple) ; développement de code web (voir les skills de développement).
Si l'utilisateur veut à la fois s'inscrire et publier : terminez d'abord ce skill, puis passez le relais à powpow-simple après l'activation.

## Présentation du produit + tour des captures (Étape 1 — à ne pas sauter)

La plupart des utilisateurs n'ont jamais vu Bubble. La toute première chose n'est pas d'expliquer le parcours, mais de leur faire **voir** le produit :

1. Présentez Bubble en ~120 caractères : transformez une photo prise sur le vif en article de journal de voyage, épinglé sur une carte publique comme une « bulle » ; les bulles se fanent avec le temps, mais les likes des autres peuvent les faire revivre ; la carte compte aussi des « humains numériques » avec qui discuter. Adresse de la plateforme : https://global.powpow.online ; pour voir une vidéo d'abord : https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Envoyez les liens des captures** (en image Markdown ou en lien brut, les deux conviennent). La liste, le contenu et le moment d'utilisation de chaque image : `references/screenshots.md`. Meilleure combinaison d'ouverture : page carte (powpow-03) + page de détail d'un post (powpow-06).

Règles des captures (règles strictes) :

- Les captures sont hébergées sous `screenshots/` dans le dépôt public `durenzidu/durenzidu` (`powpow-0N.jpg`) ; **ne** téléchargez **pas** les images dans le répertoire du skill et n'envoyez pas de chemins locaux comme images.
- Si `raw.githubusercontent.com` ne répond pas, utilisez le miroir jsdelivr (voir `references/screenshots.md`).
- N'envoyez qu'1 à 3 images pertinentes pour le sujet du moment à chaque fois, ne les déversez pas toutes d'un coup.
- Si on ne sait pas de quelle image il s'agit, ne devinez pas — choisissez selon les descriptions de `references/screenshots.md`.

Après la présentation, rendez la main à l'utilisateur pour la suite : **« Si vous êtes prêt(e) à vous inscrire, nous créons votre compte en trois minutes. »**

## Parcours d'inscription (Étape 2)

L'inscription se fait entièrement dans la page web : **https://global.powpow.online/register**. Faites ouvrir la page à l'utilisateur, puis guidez-le pas à pas (règles complètes des champs, paramètres de limitation de débit et tableau des erreurs dans `references/registration-flow.md` — consultez-le en cas de problème) :

1. **(Facultatif) Avatar** : image ≤5 Mo, SVG non pris en charge.
2. **Nom d'utilisateur** : 2 à 50 caractères ; insensible à la casse (Tom et tom sont le même compte).
3. **Mot de passe** : au moins 8 caractères, doit contenir majuscules, minuscules et chiffres ; saisissez-le une seconde fois pour confirmer.
4. **Surnom** : facultatif, le nom d'utilisateur est utilisé par défaut.
5. **E-mail (obligatoire)** : cliquez sur « Envoyer le code de vérification » → cherchez dans votre messagerie le **code à 6 chiffres** (valable 10 minutes, pensez aussi au dossier spam/promotions) ; le bouton a un compte à rebours de 60 secondes.
6. **Téléphone** : facultatif, format des numéros de Chine continentale ; un numéro ne peut être lié qu'à un seul compte.
7. Validez.

En bas de page se trouvent aussi trois boutons de connexion tiers : **Google / Watcha / compte Huawei** — si l'utilisateur préfère un compte tiers, il lui suffit de cliquer sur le bouton, sans passer par l'inscription par e-mail.

**Ce qui se passe après la validation** : le compte est créé immédiatement (statut pending, 3 badges initiaux) et la page redirige automatiquement vers la page d'abonnement `/subscription`. **Ce n'est qu'après avoir finalisé l'abonnement que le compte est activé**, avec le fil d'actualités, la carte et le dialogue avec les humains numériques — c'est la section suivante.

Pendant l'accompagnement, n'inventez aucune information pour l'utilisateur ; terminez chaque réponse par un bloc « prochaine étape » explicite.

## Activation de l'abonnement (Étape 3)

L'inscription ne crée qu'un compte pending ; **c'est le paiement de l'abonnement qui l'active**. Ce skill ne touche à aucun paiement — il suffit d'orienter l'utilisateur vers la page d'abonnement : **https://global.powpow.online/subscription**

Selon l'environnement de l'utilisateur, la page affiche l'un des trois canaux :

| Canal | Environnement | Explication |
|---|---|---|
| Abonnement PayPal | Web | Renouvellement automatique ; activé automatiquement par Webhook après paiement ; annulable à tout moment |
| Abonnement par QR code WeChat | Web | Virement par scan de QR code, **activé après confirmation manuelle** ; le crédit peut prendre du temps |
| Achat intégré Huawei | Dans l'app HarmonyOS | PayPal / WeChat Pay indisponibles sur HarmonyOS ; recours à l'IAP natif Huawei |

Après le paiement, le compte passe à active et revient automatiquement à l'accueil (ou à la page que l'utilisateur voulait voir avant l'inscription).
Les détails des canaux, la chaîne d'activation et la conclusion « les moyens de paiement existants sont directement réutilisables » figurent dans `references/payment-and-activation.md`.

**Message à l'utilisateur** : « Après l'inscription, la page vous mènera à la page d'abonnement ; sur le web vous pouvez payer par PayPal ou QR code WeChat, et dans l'app HarmonyOS vous payez avec Huawei Pay. Dès que vous avez payé, votre compte est activé. »

## Expérience de conversation (UX)

Conservez le ton orienté service propre à powpow :

- **L'utilisateur est le sujet de la phrase** — « vous pouvez… » vaut mieux que « j'ai besoin que vous… » ; pas de leçon, pas de condescendance.
- **Une seule décision par échange** ; donnez la raison avant de demander des informations.
- **Chaque réponse se termine** par un bloc « prochaine étape » fixe (séparateur + 👉 + une seule action + une phrase « une fois que vous aurez fait ceci, je… »), par exemple :
  ```
  ────────────────────
  👉 Ce qu'il faut faire maintenant : ouvrez la page d'inscription et remplissez le nom d'utilisateur et le mot de passe
     (dites-le-moi quand c'est fait, on passera au code de vérification)
  ```
- **Pas de sermon sécuritaire sur le mot de passe** ; n'expliquez pas les mécanismes internes, la limitation de débit ou la conception de sécurité, sauf si l'utilisateur le demande.

## Règles strictes

- L'inscription se fait dans la page web ; ce skill ne fait que présenter, orienter et dépanner — **ne demandez jamais** le mot de passe ou le code de vérification de l'utilisateur, et ne tentez jamais de soumettre des formulaires à sa place.
- N'inventez pas les règles de la plateforme : règles des champs, messages d'erreur et paramètres de limitation proviennent tous du code de la plateforme (`references/registration-flow.md` cite les sources) ; en cas de mise à jour de la plateforme, le comportement réel fait foi.
- Pour les images, n'utilisez que les liens hébergés de `references/screenshots.md` et respectez les règles des captures.
- Terminez chaque échange par un bloc « prochaine étape » pour que l'utilisateur sache toujours quoi faire.