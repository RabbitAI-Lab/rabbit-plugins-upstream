# Captures d'écran du produit — powpow-register

À utiliser à la demande pendant l'exécution. Quand l'utilisateur n'a aucune idée de ce qu'est Bubble, ou a besoin de « voir » à quoi ressemble le produit fini, envoyez directement les liens correspondants.

## Règles des liens

- Lien principal (raw) :
  `https://raw.githubusercontent.com/durenzidu/durenzidu/main/screenshots/powpow-0N.jpg`
- Miroir (à utiliser si raw est inaccessible, `N` = 1 à 6) :
  `https://cdn.jsdelivr.net/gh/durenzidu/durenzidu@main/screenshots/powpow-0N.jpg`
- Les images sont dans un dépôt public et peuvent être envoyées directement ; **ne** téléchargez **pas** les images dans le répertoire du skill et n'envoyez pas de chemins locaux comme images.
- N'envoyez qu'1 à 3 images pertinentes pour le sujet du moment à chaque fois.

## La liste

### powpow-01.jpg — Page de détail d'un humain numérique

![Page de détail d'un humain numérique](https://raw.githubusercontent.com/durenzidu/durenzidu/main/screenshots/powpow-01.jpg)

La carte d'une personne réelle / figure historique transformée en humain numérique : statut en ligne, lieu, biographie, « Démarrer la conversation » etc.
**Utilisation** : pour présenter « une fois inscrit, tu peux discuter avec les humains numériques de la carte ».

### powpow-02.jpg — Page d'édition d'un post

![Page d'édition d'un post](https://raw.githubusercontent.com/durenzidu/durenzidu/main/screenshots/powpow-02.jpg)

L'interface d'édition pour écrire des posts / journaux de voyage, avec un groupe de boutons flottants en bas à droite.
**Utilisation** : quand l'utilisateur demande « que puis-je faire après l'inscription » / « où écrire quelque chose ».

### powpow-03.jpg — Page carte (bulles + humains numériques)

![Page carte](https://raw.githubusercontent.com/durenzidu/durenzidu/main/screenshots/powpow-03.jpg)

La carte publique dans son ensemble : les posts géolocalisés se regroupent en « bulles » sur la carte, les humains numériques sont épinglés à des lieux réels avec leurs avatars.
**Utilisation** : **l'image de référence pour l'introduction du produit** — « tes articles de journal de voyage deviennent une bulle sur la carte ».

### powpow-04.jpg — Page de profil (actifs numériques)

![Page de profil](https://raw.githubusercontent.com/durenzidu/durenzidu/main/screenshots/powpow-04.jpg)

La page personnelle de l'utilisateur : amis/abonnements/abonnés, et « Actifs numériques » — solde de badges, mes bulles, mes humains numériques.
**Utilisation** : pour montrer où se trouvent les badges quand on dit « l'inscription offre 3 badges » ; quand l'utilisateur demande « quels actifs ai-je ? ».

### powpow-05.jpg — Page de progression d'une histoire

![Page de progression d'une histoire](https://raw.githubusercontent.com/durenzidu/durenzidu/main/screenshots/powpow-05.jpg)

Le gameplay narratif de la plateforme (exemple « 永乐·1421 ») : progression des chapitres, gagner des badges, jeu de rôle.
**Utilisation** : quand l'utilisateur demande « à quoi d'autre puis-je jouer à part publier » / « comment gagner des badges ».

### powpow-06.jpg — Page de détail d'un post (exemple abouti)

![Page de détail d'un post](https://raw.githubusercontent.com/durenzidu/durenzidu/main/screenshots/powpow-06.jpg)

Un journal de voyage publié : auteur, tags de lieu, texte, images ; en bas : aimer/commenter/partager/enregistrer.
**Utilisation** : **la deuxième image d'ouverture** — « c'est exactement ce que les autres voient quand ils ouvrent ta bulle sur la carte ».

## Aide-mémoire par scénario

| Ce que dit l'utilisateur / étape en cours | Quelle image envoyer |
|---|---|
| Introduction « qu'est-ce que Bubble » | powpow-03 + powpow-06 |
| « Que puis-je faire après l'inscription ? » | powpow-02 + powpow-01 |
| « C'est quoi les badges / qu'ai-je ? » | powpow-04 |
| « À quoi d'autre puis-je jouer à part publier ? » | powpow-05 |
| Dépannage d'erreurs d'inscription/abonnement | En général aucune image ; n'en envoyer que s'il faut indiquer un emplacement sur une page |

## Notes de maintenance

La bibliothèque actuelle ne contient pas de captures de la **page d'inscription** ni de la **page d'abonnement**. Si elles sont ajoutées plus tard sous `screenshots/` du dépôt `durenzidu/durenzidu` (par ex. `powpow-07.jpg` pour l'inscription, `powpow-08.jpg` pour l'abonnement), ajoutez ici une section au même format ; le texte de guidage de SKILL.md pourra s'y référer.