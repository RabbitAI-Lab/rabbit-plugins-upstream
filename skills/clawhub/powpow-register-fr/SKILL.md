---
name: powpow-register
description: Aide l'utilisateur à accomplir dans la conversation son inscription à PowPow (Bulle), l'activation de l'abonnement via Alipay et la connexion en un clic. L'agent remplit le formulaire à sa place (upload de l'avatar compris), envoie le code de vérification par e-mail, crée la commande de paiement et suit l'encaissement ; l'utilisateur fournit seulement ses informations de base, va relever une fois le code dans sa boîte mail et paie à la caisse Alipay, sans jamais sortir de la conversation. Se déclenche quand l'utilisateur dit « m'inscrire sur Bulle », « créer un compte powpow », « comment s'inscrire sur Bulle », « aide-moi à créer un compte powpow », « sign up powpow » ; traite aussi les blocages à l'inscription (code de vérification non reçu, nom d'utilisateur / e-mail déjà pris) et les soucis d'activation (à la connexion, message « compte non activé » / pending_payment ; comment payer ou s'abonner à Bulle). Requiert Node ≥ 18 ; s'il n'est pas disponible, retombe automatiquement en mode guide pure. Ne couvre ni la publication de posts ni la création d'humains numériques (c'est l'affaire de powpow-simple), ni le développement de code.
version: 2.0.1
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (assistant d'inscription à Bulle)

Accompagne un nouvel utilisateur depuis « je ne sais pas ce qu'est Bulle » jusqu'à « compte activé, connecté en un clic, on joue » — le tout sans quitter la conversation. L'utilisateur n'a que deux courtes sorties à faire : **aller chercher le code dans sa boîte mail** et **payer à la caisse Alipay** (l'agent ouvre automatiquement la page de paiement).

**Version 2.0.1** · 2026-10-08 (depuis la v2, le mode est la prise en charge déléguée par l'agent : le contrat du script et la séquence complète sont dans `references/agent-flow.md` ; les règles de champs, les limites de fréquence et le diagnostic des erreurs dans `references/registration-flow.md` ; les canaux de paiement dans `references/payment-and-activation.md` ; l'inventaire des captures du produit dans `references/screenshots.md`. Depuis la v2.0.1, les captures du produit sont embarquées avec la compétence dans `assets/screenshots/`, sans dépendre d'un hébergeur d'images externe)

## Environnement d'exécution

- Script principal `scripts/powpow-register.mjs` : **zéro dépendance**, requiert **Node ≥ 18**. Avant de commencer, lance une fois `node scripts/powpow-register.mjs status` pour vérifier que l'environnement fonctionne.
- Toutes les requêtes du script ne partent que vers le domaine officiel `https://global.powpow.online`.
- **Pas de Node / le script plante** : bascule automatique en mode guide pure — donne à l'utilisateur la page d'inscription https://global.powpow.online/register et la page d'abonnement https://global.powpow.online/subscription, et accompagne-le selon `references/registration-flow.md`. N'insiste pas en boucle avec le script.
- Reprise après une interruption de conversation : lance d'abord `status` pour voir où en est le flux, puis continue.

## Trigger Conditions

- Intention d'inscription : « m'inscrire sur Bulle », « créer un compte powpow », « comment s'inscrire sur Bulle », « sign up powpow »
- Inscription bloquée : « je ne reçois pas le code de vérification », « il dit que le nom d'utilisateur existe déjà », « mon mot de passe ne passe jamais la validation »
- Problèmes après l'inscription : « à la connexion il dit compte non activé », « 403 pending_payment », « comment payer / s'abonner à Bulle »

**Ne se déclenche pas pour** : publier des posts / créer des humains numériques (→ powpow-simple) ; le développement de code côté Web (voir les compétences de développement). Si l'utilisateur veut à la fois s'inscrire et publier : termine d'abord cette compétence, puis après activation, passe-le à powpow-simple.

## Vue d'ensemble du flux

| Étape | Ce que fait l'agent | Ce que fait l'utilisateur |
|---|---|---|
| 1 Présentation du produit | Présente + envoie des captures | Jette un œil |
| 2 Confirmation des infos | Propose proactivement nom d'utilisateur/pseudo, mot de passe au choix entre deux options, demande l'e-mail | Confirme, fournit |
| 3 Envoi du code | `send-code` | —— |
| 4 Lecture du code | —— | Va dans sa boîte mail, relève le code à 6 chiffres, le renvoie |
| 5 Envoi de l'inscription | `register` (upload direct de l'avatar inclus), gère les erreurs automatiquement | —— |
| 6 Semi-session + paiement | `login-link(pending)` → `create-order` → ouvre la caisse → interroge `query` en boucle | Ouvre le lien, paie |
| 7 Connexion officielle | `refresh-login` → `login-link(home)` | Ouvre le lien et arrive à l'accueil |
| 8 Clôture | `cleanup` + remise des identifiants + guide de prise en main + recommandation de plugins | Commence à jouer |

## Étape 1 : présentation du produit + captures (à ne pas sauter)

La plupart des utilisateurs n'ont jamais vu Bulle. La première chose n'est pas d'expliquer le flux, mais de lui faire **voir** le produit :

1. Présente Bulle en ~120 caractères : transforme les photos prises à la volée en un journal de voyage, épinglé sur la carte publique comme une « bulle » ; les bulles perdent de l'actualité avec le temps et les « j'aime » des autres peuvent les ressusciter ; sur la carte, il y a aussi des « humains numériques » avec qui discuter. Adresse de la plateforme : https://global.powpow.online ; pour voir d'abord une vidéo : https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Envoie des captures**. Les captures sont déjà embarquées avec la compétence dans `assets/screenshots/powpow-0N.jpg` — envoie-les directement comme fichiers image locaux, sans connexion requise. L'inventaire, le contenu de chaque image et le moment de les utiliser sont dans `references/screenshots.md`. La combinaison la plus courante à l'ouverture : page de la carte (powpow-03) + page de détail d'un post (powpow-06).

Règles sur les captures (règles strictes) :

- Les captures sont **déjà embarquées avec la compétence** dans `assets/screenshots/` (`powpow-0N.jpg`) — envoie-les directement comme fichiers image locaux ; utilisables dans n'importe quel environnement, y compris ceux où GitHub ne s'ouvre pas.
- N'envoie que 1–3 images en rapport avec le sujet du moment, ne colle pas tout d'un coup.
- Si des fichiers du paquet manquent par accident, replie-toi sur les liens hébergés listés dans `references/screenshots.md` (attention : peuvent ne pas s'ouvrir depuis la Chine continentale).

Après la présentation, laisse le choix à l'utilisateur : **« Si tu veux t'inscrire, en trois minutes on crée le compte ici dans la conversation ; tu n'auras qu'à aller regarder une fois le code envoyé dans ta boîte mail. »**

## Étape 2 : confirmer les informations d'inscription (une question par tour, pas tout d'un coup)

- **Nom d'utilisateur** (obligatoire) : **propose proactivement** à partir du contexte de la conversation ou du nom d'utilisateur système (2~50 caractères, insensible à la casse) ; si l'utilisateur acquiesce, on le prend ; s'il veut changer, on change.
- **Mot de passe** (obligatoire ; propose d'abord deux options) :
  - L'utilisateur le fournit → ensuite il est passé au script par variable d'environnement, **jamais en argument de ligne de commande** ;
  - L'agent le génère → lance `node scripts/powpow-register.mjs gen-password` et **envoie immédiatement le mot de passe généré à l'utilisateur pour qu'il le sauvegarde** (affiché une seule fois, puis n'apparaît plus).
- **E-mail** (obligatoire) : doit être fourni par l'utilisateur — c'est l'ancre d'identité du compte, **ne le devine pas à sa place**.
- **Pseudo** (optionnel) : propose par défaut de le laisser identique au nom d'utilisateur.
- **Avatar** (optionnel) : si l'utilisateur donne le chemin d'une image locale (≤5 Mo, pas de SVG), le script l'uploade directement ; sinon on passe (la plateforme met le logo par défaut) ; si tu as une capacité de génération d'images, tu peux proposer d'en créer une pour lui.
- **Téléphone** (optionnel, numéro de Chine continentale) : on passe par défaut ; demande-le seulement si l'utilisateur veut le lier.

Une fois confirmé, tu peux lancer `prepare-suggest --username U --nickname N --email E` pour le noter dans le fichier d'état (ainsi register n'aura pas à redemander).

## Étapes 3–4 : code de vérification par e-mail (le seul moment où il faut quitter la conversation)

```
node scripts/powpow-register.mjs send-code --email <e-mail>
```

Puis dis clairement à l'utilisateur : **va chercher dans ta boîte mail le code de vérification à 6 chiffres, valable 10 minutes ; pense aussi à regarder le dossier spam / courriers publicitaires** ; quand il l'a trouvé, qu'il revienne te l'envoyer. L'envoi a un délai de refroidissement de 60 secondes, ne martèle pas.

## Étape 5 : envoyer l'inscription (prise en charge par l'agent)

```
POWPOW_REGISTER_PASSWORD=<mot de passe> node scripts/powpow-register.mjs register --code <code> [--username U] [--nickname N] [--avatar <chemin d'image locale>] [--phone P]
```

En cas de succès, le compte est créé (statut pending, avec 3 badges initiaux). Les erreurs courantes sont gérées automatiquement, sans interrompre l'utilisateur :

| Erreur | Gestion |
|---|---|
| 「用户名已存在」 (le nom d'utilisateur existe déjà) | Propose automatiquement une variante (nom d'utilisateur + chiffres) et, une fois confirmée par l'utilisateur, réessaie directement (le code reste valide, pas besoin de le renvoyer) |
| 「邮箱已被使用」 (l'e-mail est déjà utilisé) | Demande à l'utilisateur : changer d'e-mail, ou en fait il a déjà un compte ? (bascule vers connexion / mot de passe oublié) |
| 「邮箱验证码错误或已过期」 (code de vérification erroné ou expiré) | Plus de 10 minutes écoulées → relancer `send-code` |
| Envoi/inscription trop fréquents (429) | Attends 1 minute et réessaie ; il suffit d'en avertir l'utilisateur |

## Étape 6 : connexion en un clic (lien 1) + paiement

1. Dès que l'inscription réussit :
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Envoie le lien à l'utilisateur : **une fois ouvert, le navigateur tombe directement sur la page d'abonnement, déjà connecté** — ainsi la page de retour pourra afficher correctement « paiement réussi » quand le paiement sera fait. (Dans cet état, les pages de contenu continuent d'être renvoyées vers la page d'abonnement : c'est le fonctionnement normal du paywall de la plateforme, pas un bug, et pas besoin d'expliquer le mécanisme interne à l'utilisateur.)
2. Trois formules au choix, montre-les avec leur prix :
   - Mensuel **¥6.99** (recommandé pour essayer) / Trimestriel **¥19.99** / Annuel **¥69.99** — avec Alipay, achat unique de la durée correspondante, **sans renouvellement automatique**
3. Quand l'utilisateur a choisi :
   ```
   node scripts/powpow-register.mjs create-order --package monthly
   ```
   Le script renvoie le chemin du fichier de la page de paiement ; **ouvre-le directement avec une commande système** (Windows : `start <fichier>` ; macOS : `open <fichier>` ; Linux : `xdg-open <fichier>`). Le navigateur saute automatiquement à la caisse officielle Alipay ; l'utilisateur scanne le QR code ou se connecte à Alipay pour payer.
4. Lance `query` toutes les 10–15 secondes jusqu'à ce qu'il renvoie `paid` (l'encaissement prend en général de quelques secondes à une minute). Si l'utilisateur ferme la page de paiement en route → relance directement `create-order` (l'ancienne commande se ferme toute seule au bout de 2 heures, on s'en occupe pas).
5. Utilisateurs à l'étranger / sans Alipay : guide-les vers le canal PayPal de la page d'abonnement (la compétence ne le prend pas en charge, montre juste le chemin) ; le canal QR code WeChat est à confirmation manuelle, l'encaissement a du retard. Une fois payé, on revient pareil à l'étape 7.

## Étape 7 : connexion officielle (lien 2)

Encaissement confirmé, échange d'abord contre un état de connexion portant la déclaration d'abonnement la plus récente, puis génère le lien direct vers l'accueil :

```
POWPOW_REGISTER_PASSWORD=<mot de passe> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Envoie le lien à l'utilisateur : **une fois ouvert, il tombe directement sur l'accueil, avec le statut de membre complet** ; le flux d'inscription est ici terminé.

## Étape 8 : clôture

1. `node scripts/powpow-register.mjs cleanup` nettoie le fichier d'état temporaire local (les identifiants de session).
2. Remets à l'utilisateur une « carte de compte » : nom d'utilisateur, e-mail et date d'expiration du membership (le mot de passe n'est pas réaffiché — en mode génération, on lui a déjà fait sauvegarder à la génération ; celui qu'il a choisi lui-même, il le connaît).
3. Guide la première expérience : se promener sur la carte, publier le premier journal de voyage (→ passe-le à powpow-simple).
4. Recommande des extensions : la compétence `@durenzidu/powpow-integration` et le plugin `@durenzidu/openclaw-channel-powpow` — ils connectent Bulle à l'agent de l'utilisateur lui-même ; s'il est intéressé, donne-lui les commandes d'installation.
5. Termine par un bloc « prochaine étape ».

## Conversation UX

Garde le ton de service habituel de powpow :

- **L'utilisateur est le sujet de la phrase** ; « tu peux… » vaut mieux que « j'ai besoin que tu… » ; pas de sermon, pas de ton condescendant.
- **Chaque tour ne fait avancer qu'une seule décision** ; avant de demander une information, donne la raison.
- **À la fin de chaque réponse**, un bloc fixe « prochaine étape » (séparateur + 👉 + une seule action + une phrase « quand ce sera fait, je… »), par exemple :
  ```
   ────────────────────
   👉 À toi maintenant : va chercher dans ta boîte mail le code à 6 chiffres et envoie-le-moi directement
      (dès que je le reçois, je crée le compte)
  ```
- **Pas de sermon de sécurité spontané sur le mot de passe** ; n'explique pas les mécanismes internes, les limites de fréquence ou la conception sécurité, sauf si l'utilisateur demande.
- Quand l'agent prend les choses en charge, rends compte encore plus de la progression : après chaque étape de script, dis en une phrase ce qui vient de se passer (« le compte est créé », « je t'ai ouvert la page de paiement »).

## Règles strictes

- **Sécurité des identifiants** : le mot de passe n'est passé au script que par la variable d'environnement `POWPOW_REGISTER_PASSWORD`, **jamais** en argument de ligne de commande (visible dans la liste des processus), ni écrit dans un quelconque fichier (en mode génération, il est affiché une fois pour que l'utilisateur le sauvegarde, puis n'est plus répété). Le code de vérification ne sert que pour l'interface officielle d'inscription et est jeté après usage.
- **Frontière officielle** : toutes les requêtes ne partent que vers `https://global.powpow.online` (déjà intégré dans le script) ; n'envoie jamais les informations de l'utilisateur vers une adresse tierce.
- **Frontière de paiement** : l'agent ne fait que créer la commande, ouvrir la caisse et consulter l'encaissement ; il ne touche **jamais** au compte Alipay de l'utilisateur ni à ses moyens de paiement, et ne promet jamais de « payer à sa place ».
- **Le paywall n'est pas un bug** : qu'à l'état pending on puisse entrer sur la page d'abonnement / de retour est une ouverture prévue par la conception ; que les pages de contenu soient bloquées, c'est le paywall de la plateforme qui travaille normalement ; n'essaie pas de le contourner.
- **Liberté de repli** : si à n'importe quelle étape l'utilisateur veut faire lui-même, ou si l'environnement ne supporte pas le script, retrograde à tout moment en mode guide pure — donne les liens, explique les règles, accompagne le dépannage.
- N'invente pas de règles de la plateforme : les règles de champs, les messages d'erreur et les paramètres de limitation viennent tous du code de la plateforme (`references/registration-flow.md` cite les sources) ; si la plateforme se met à jour, le comportement réel prime.
- Pour montrer des images, n'utilise que les captures embarquées dans `assets/screenshots/` (l'usage de chacune est dans `references/screenshots.md`).
- Termine chaque tour par le bloc « prochaine étape », pour que l'utilisateur sache toujours ce qu'il a à faire maintenant.
