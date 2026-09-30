<sub>🌐 <a href="README.md">简体中文</a> · <a href="README.zh-Hant.md">繁體中文</a> · <a href="README.en.md">English</a> · <b>Français</b> · <a href="README.es.md">Español</a> · <a href="README.ar.md">العربية</a> · <a href="README.ja.md">日本語</a> · <a href="README.ru.md">Русский</a></sub>

<div align="center">

<img src="logo.png" alt="Hui Ning IP" width="150">

# Madrid Trademark · Système de Madrid

> *« Une question. Une réponse directement exploitable au dossier. »*
> *"Ask once. Get a filing-ready Madrid practice answer."*

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-3.4.5-blue.svg)](https://github.com/huiningip/madrid-trademark)
[![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)](#installation)
[![Madrid Members](https://img.shields.io/badge/Madrid%20Members-117%20%C2%B7%20133%20countries-green)](https://www.wipo.int/en/web/madrid-system/members/)
![Office-Neutral](https://img.shields.io/badge/Perspective-Office--Neutral-orange)

<br>

**Une compétence d'agent dédiée à la pratique du système de Madrid, destinée aux conseils en marques, avocats en propriété intellectuelle et juristes d'entreprise du monde entier.**

<br>

Pas une vulgarisation sur « qu'est-ce que le système de Madrid », mais **des livrables qui vont directement au dossier** : décomptes de taxes exacts, calcul des deux catégories de délais, listes de contrôle et notes de réponse prêtes à remplir, textes de traités vérifiables mot à mot.

La phase internationale de l'OMPI est identique depuis n'importe quelle partie contractante. Cette compétence est rédigée dans une **perspective neutre (office-neutral)** — le volet CNIPA/Chine n'est qu'un chapitre optionnel. Que vous partiez de l'USPTO, de l'EUIPO, du JPO ou du CNIPA, l'usage est le même.

Chaque montant de taxe, chaque délai et chaque déclaration porte une **date d'arrêté des données et un point de vérification officiel**. Ce qui est introuvable est renvoyé par un « néant » — sans invention.

```
git clone https://github.com/huiningip/madrid-trademark ~/.workbuddy/skills/madrid-trademark
```

Compatible avec tout agent — s'installe dans n'importe quel agent prenant en charge les skills.

> 📣 **Les données volatiles ne sont jamais figées.** Taxes, taxes individuelles, déclarations des parties contractantes, nombre de membres et textes juridiques sont chacun assortis d'une « date d'arrêté + périodicité de révision + point de vérification officiel ». À échéance, la compétence impose une vérification en ligne et refuse de se fier aux valeurs mises en cache par les moteurs de recherche.

[Ce que cela fait](#ce-que-cela-fait) · [Installation](#installation) · [Mécanismes clés](#mécanismes-clés) · [Structure du dépôt](#structure-du-dépôt) · [Limites](#limites)

</div>

---

<p align="center"><sub>

```
Demande/enregistrement de base ──▶ Transmission par l'office d'origine ──▶ Examen formel OMPI ──▶ Date d'enregistrement international
                                                                                            │
                                          ┌───────────────────────────────────────────────────┴──────────────────────────┐
                                          ▼                                                                              ▼
              Délai de refus par office désigné : 12 / 18 / 25 mois                          Attaque centrale : dépendance de 5 ans
                                          │                                                                              │
                          Aucun refus ⇒ protection accordée                    Base anéantie ⇒ transformation sous 3 mois,
                                                                               déposée directement auprès de chaque office désigné
```

</sub></p>

<p align="center"><sub>▲ Un seul fil conducteur : dépôt → transmission → suivi des délais de refus → repli par transformation. Chaque point de contrôle 🔴 est verrouillé par la compétence.</sub></p>

---

## Installation

```bash
# Option 1 : CLI skills
npx skills add huiningip/madrid-trademark

# Option 2 : git clone (repli si la synchronisation de la CLI déraille)
git clone https://github.com/huiningip/madrid-trademark ~/.workbuddy/skills/madrid-trademark
```

> **Vérifiez après installation** : ce n'est pas une compétence réduite au seul `SKILL.md`. `references/` (13 fichiers Markdown + 2 PDF officiels), `scripts/` (7 scripts Python + 2 fichiers JSON de données) et `templates/` (2 modèles) sont des entités référencées dans le corps du texte par des chemins relatifs `@` ; en manquer une suffit à rompre la chaîne.
>
> Après installation, inspectez le répertoire : si seul `SKILL.md` est présent et que les sous-répertoires manquent, votre outil de synchronisation n'a récupéré qu'un fichier — réinstallez avec `git clone` ci-dessus.
>
> Auto-test des scripts (Python 3.10+ ; les scripts hors ligne n'utilisent que la bibliothèque standard) :
>
> ```bash
> py -B scripts/selftest.py     # 9 groupes de cas — tout au vert = déploiement complet
> ```

Puis adressez-vous directement à l'agent, dans n'importe quel agent compatible skills :

```
« Taxe individuelle pour le Japon — calcule-moi un dépôt sur 3 classes »
« Refus pour la Chine : 15 ou 30 jours, et à compter de quand ? »
« L'enregistrement de base de mon client (2021) vient d'être annulé — une transformation est-elle encore possible ? »
« Renouvellement : enregistré le 2016-07-01 pour 10 ans. Est-ce encore dans les délais ? »
« Calcule les délais de refus pour US/JP/ID/IL — lesquels exigent une surveillance à 18 mois ? »
```

Pas de formulaire. Pas d'assistant pas-à-pas. Pas d'inscription. Une question, et vous obtenez de quoi alimenter le dossier.

---

## Ce que cela fait

| Capacité | Livrable | Contrainte clé |
|----------|----------|----------------|
| Demande internationale | Étapes de procédure + `templates/madrid_application_checklist.md` | Verrouille le délai de transmission (2 mois) et les spécifications de reproduction |
| Calcul des taxes | Décompte par partie (taxe de base / supplémentaire / complémentaire / individuelle) | **Double contrôle** : instantané hors ligne vs mesure officielle en direct |
| Calcul du délai de refus | Compte à rebours 12 / 18 / 25 mois | Vérifier d'abord les déclarations de la partie — **jamais présumer 18 mois** |
| Calcul du délai de réponse | Compte à rebours par partie (dont Chine 15 / 30 jours) | Reconnaît 6 points de départ ; **refuse** de compter depuis la date de réception si la base officielle diffère |
| Réponse au refus provisoire | Qualification de la procédure + axes de stratégie + `templates/madrid_refusal_response_memo.md` | Distinguer d'abord le refus d'office de l'opposition d'un tiers |
| Gestion du renouvellement | Fenêtre de renouvellement + surtaxe de délai de grâce | Surtaxe de grâce = **50 % de la taxe de base (327 CHF)** |
| Modification / cession / limitation / renonciation | Voie de dépôt + règles de numéro (numéro d'origine + lettre majuscule) | Division et fusion passent par l'office d'origine |
| Réponse à l'attaque centrale | Test de dépendance de 5 ans + compte à rebours de 3 mois | La transformation est déposée **directement auprès de chaque office désigné**, pas auprès de l'OMPI |
| Vérification des produits/services (MGS) | Processus de contrôle du libellé normalisé | Le libellé doit correspondre exactement à la MGS de l'OMPI |
| Examen des déclarations | Liste par partie des 17 catégories + test de la clause de sauvegarde | Les déclarations peuvent être **inopposables** entre États doublement parties |
| Volet Chine (CNIPA) | Voie de dépôt via l'office d'origine + points d'examen accéléré | Chapitre optionnel — inutile hors pratique chinoise |
| Vérification des traités | Textes intégraux et littéraux de l'Arrangement / du Protocole / du Règlement / des Instructions | Toujours citer le texte, jamais le résumé |

---

## Couverture en détail

### Taxes : deux voies, non substituables

`scripts/madrid_fee.py` est le calcul par **instantané hors ligne** — sans réseau ni navigateur, avec les taxes individuelles de 76 parties contractantes intégrées ; il applique les **modifications tarifaires annoncées** selon `--date`.

`scripts/madrid_feecalc_live.py` est la **mesure officielle en direct** — il pilote le calculateur de taxes de l'OMPI via un vrai navigateur, renvoie les montants faisant autorité par partie, et sert d'instrument d'arbitrage en cas de contestation.

> Le calculateur officiel est une application JSF : la liste des parties comme les résultats sont rendus par JavaScript, ce qui le rend **impossible à récupérer en HTTP simple**. Chaque case cochée déclenche un repaint AJAX et un clic isolé peut être avalé ; le script prévoit donc jusqu'à 4 tours de reprise (« cocher → relire l'ensemble coché → cocher ce qui n'a pas pris »). Si la ligne finale indique « N / M cochées » en deçà de M, le résultat est inutilisable par construction.

```bash
# Hors ligne : première estimation pour un devis
py madrid_fee.py --countries ID,IL --classes 2 --date 2026/11/01

# En direct : la mesure décisive en cas de contestation
py madrid_feecalc_live.py --origin US --classes 1 --countries JP,ID,IL
```

**`--date` est le paramètre décisif.** La page OMPI des taxes individuelles n'affiche que le montant *actuel*, alors que le calculateur applique les tarifs en vigueur à la *date de dépôt envisagée*. En franchissant une date d'entrée en vigueur (couramment le 1er novembre ou le 1er janvier), il faut chiffrer séparément selon la date de dépôt envisagée — une même demande peut avoir deux prix de part et d'autre. Exemple mesuré et consigné : **entrée en vigueur le 2026-11-01, Indonésie 91 → 125, Israël 471 → 503**.

### Délais : deux catégories, et c'est là que la pratique se trompe

Le **délai de refus** est le délai de *l'office* pour notifier, compté en mois : socle de **12 mois**, **18 mois** lorsque la partie a fait la déclaration au titre de l'article 5(2)(b), et jusqu'à environ **25 mois** lorsqu'une déclaration au titre de l'article 5(2)(c) s'y ajoute et qu'une opposition survient. Pour une désignation postérieure, il court à compter de la **date d'inscription**.

Le **délai de réponse** est le délai du *titulaire* pour répondre à un refus provisoire, compté en jours ou en mois, notifié pays par pays au titre de la règle 17(7) :

- Chine (CN) : **15 jours** pour un refus d'office / **30 jours** pour un refus consécutif à une opposition, à compter de la réception de la transmission de l'OMPI
- France (FR) : 1 mois / 2 mois · Royaume-Uni (GB) : 2 mois · Allemagne (DE) : 4 mois · Japon (JP) : 3 mois
- États-Unis (US) : 6 mois (d'office) / 40 jours (opposition, à compter de l'ordonnance du TTAB) · Thaïlande (TH) : 90 jours

> **Avertissement sur la couverture.** Ce tableau de l'OMPI ne recense que **38 membres** (sur 117), et le point de départ varie selon **6 modalités** (réception par le titulaire / transmission OMPI / envoi par l'office / réception par l'OMPI / 14e jour après l'envoi / ordonnance du TTAB). **Non listé ≠ absence de délai de réponse.** Lorsque la base officielle n'est pas « date de réception », `madrid_deadline.py` **refuse** de décompter depuis la date de réception — ce calcul surestimerait le temps restant — et exige la date de départ officielle.

**Ne confondez pas 15/30 jours et 12/18/25 mois.** Les premiers sont le délai de réponse du titulaire, les seconds le délai de notification de l'office.

### Attaque centrale : 3 mois, et le bon destinataire

Un enregistrement international dépend de la demande/du enregistrement de base pendant ses **5 premières années** ; l'annulation de la base entraîne sa chute. Le remède est l'article 9quinquies : déposer une demande de transformation **directement auprès de chaque office désigné** dans les **3 mois** de l'annulation. La demande nationale qui en résulte conserve la **date d'enregistrement international et la date de priorité d'origine**.

> L'erreur récurrente : déposer la transformation auprès de l'OMPI. La transformation se dépose auprès des **offices désignés**, pas auprès du Bureau international.

### Déclarations : vérifier d'abord, décider ensuite

Les parties contractantes peuvent formuler 17 catégories de déclarations et notifications, qui pèsent sur l'effet, les taxes et les délais. Pour choisir les parties désignées, vérifier dans l'ordre : perçoit-elle une taxe individuelle → quel palier de délai de refus → une exigence particulière (déclaration d'intention d'usage, par exemple) → division/fusion applicables → l'inscription d'une licence a-t-elle un effet international.

> **Rappel de la clause de sauvegarde.** Lorsque la partie désignée **et** la partie d'origine sont **toutes deux parties à l'Arrangement et au Protocole**, les déclarations de cet État au titre de l'article 8(7) et de l'article 5(2)(b)/(c) sont **inopposables dans leurs relations mutuelles** (article 9sexies(1)(b) du Protocole ; barème des taxes, rubriques 2.4 / 5.3 / 6.4). Un déposant chinois désignant la France, l'Allemagne, l'Italie, l'Espagne ou la Suisse doit vérifier ce point au cas par cas.

### Textes des traités : vérifiables mot à mot, réextractibles en une commande

L'Arrangement (18 articles), le Protocole (16 articles + 10 sous-règles), le Règlement d'exécution (41 règles + barème des taxes) et les Instructions administratives (7 parties, 19 sections + section 11bis) sont tous fournis en **textes intégraux et littéraux en chinois** (traduction officielle WIPO Lex) appariés aux **textes officiels en anglais**. Lorsque l'OMPI met un texte à jour, réextrayez-le avec `wipo_lex_fetch.py` :

```bash
# Inspecter d'abord la structure, et vérifier les premier/dernier articles ainsi que leur nombre
py -B wipo_lex_fetch.py --url https://www.wipo.int/wipolex/en/text/384637 --inspect
```

---

## Mécanismes clés

### Le verrou de fraîcheur des données volatiles

La règle la plus dure de la compétence. Tout ce qui peut changer — taxes, taxes individuelles, déclarations, nombre de membres, cours de change, versions des traités — doit figurer au §3.0 avec une « date d'arrêté + périodicité de révision + point de vérification officiel » :

| Donnée | Date d'arrêté | Révision | Point de vérification |
|--------|---------------|----------|------------------------|
| Nombre de membres | 2026-09-23 | Mensuelle | Page des membres de l'OMPI |
| Taxes de l'OMPI | Barème, version 2023-02-01 | Trimestrielle | Barème des taxes de l'OMPI |
| Taxe individuelle par partie | 2026-08-23 | Mensuelle | Page des taxes individuelles |
| Déclarations des parties | 2026-03-15 | Mensuelle | Page des déclarations |
| Tableau des délais de réponse | 2026-08-28 | Mensuelle | Page des délais de réponse |
| Cours du CHF | **non intégré** | Avant chaque paiement | Cours en temps réel / Fee Calculator |

Passé la périodicité, ou à la demande expresse de l'utilisateur, la compétence **doit vérifier en ligne avant de répondre**. Ce qui est introuvable reçoit la réponse « néant ».

### Source unique pour chaque donnée

Une même donnée n'est jamais stockée à deux endroits, ce qui écarte la coexistence de deux versions :

- Taxes → `references/madrid-fees.md` (miroir lisible par machine : `scripts/madrid_fee_data.json`)
- FAQ et contre-exemples → `references/madrid-faq.md`
- Déclarations → `references/madrid-declarations.md` (17 catégories numérotées)

La cohérence de chaque paire « version humaine ↔ version machine » est contrôlée partie par partie par des cas dédiés de `selftest.py` — modifiez le document sans synchroniser la donnée et l'auto-test passe au rouge.

### Deux catégories de délais, strictement séparées

Une seule commande couvre les deux, avec une logique étanche :

- Le mode par défaut calcule le **délai de refus** (12 / 18 / 25 mois) — il présume 12 mois et exige la vérification des déclarations ; **18 mois requiert un `--declared-18` explicite** ; revendiquer la prorogation pour opposition sur la base de 12 mois est rejeté d'emblée (l'article 5(2)(c) suppose une déclaration à 18 mois).
- `--respond` calcule le **délai de réponse** — données de la règle 17(7) intégrées pour les 38 membres, avec résolution des 6 modalités de point de départ.

### Discipline de format de sortie

La documentation interne de la compétence peut s'appuyer sur des tableaux Markdown ; en revanche, **le texte livré à l'utilisateur après appel ne doit contenir aucun tableau Markdown** — il use de lignes « poste : montant (base juridique) », de puces `·` par partie, ou d'un alignement par indentation. Aucun montant ni délai ne perd son unité ou sa base ; toute donnée volatile est signalée comme à revérifier.

### Bibliothèque de contre-exemples

`references/madrid-faq.md` recense 16 contre-exemples fréquents, y compris les corrections d'erreurs historiques de cette compétence. Parmi les plus fréquents et les plus lourds : présumer un délai de refus de 18 mois ; confondre taxe complémentaire et taxe individuelle ; calculer la surtaxe de grâce comme « 50 % du total dû » ; payer le dernier jour du délai de grâce ; modifier la liste de produits lors du renouvellement ; déposer la transformation auprès de l'OMPI après une attaque centrale.

> Principe de fond : dans la pratique de Madrid, **le respect des délais et la conformité formelle priment sur la force de l'argumentation**. Un délai manqué équivaut, en règle générale, à un droit irrécupérable.

---

## Par rapport à une IA généraliste

Demandez à un modèle généraliste « combien coûtent les taxes de Madrid » et vous obtiendrez un chiffre **sans date d'arrêté, sans source traçable, possiblement périmé**. La différence tient à trois points :

| | IA généraliste | madrid-trademark |
|---|---|---|
| Montants des taxes | Instantané issu des données d'entraînement, sans date d'arrêté | Date d'arrêté + point de vérification officiel + remesure en direct |
| Délai de refus | Répond souvent « 18 mois » | Socle de 12 mois, dicté par les déclarations ; 25 mois sous conditions strictes |
| Donnée manquante | Tendance à inventer une réponse plausible | Répond « néant » |
| Calcul des délais | Mental, source d'erreurs | `madrid_deadline.py` résout les 6 modalités de départ |
| Citations juridiques | Reformulées, invérifiables | Textes intégraux de l'Arrangement / Protocole / Règlement / Instructions, vérifiables par grep |
| Livrable | Un paragraphe de prose | Liste de contrôle + note de réponse + décompte par partie |

L'IA généraliste est une **meilleure conversation** ; cette compétence vise à **faire disparaître l'incertitude du « introuvable / inexact »**.

---

## Données et provenance

- **Zéro invention.** Ce qui est introuvable reçoit la réponse « néant » — jamais estimé, jamais comblé par un texte de remplissage.
- **Aucune télémétrie.** La compétence est un ensemble de fichiers purement local : elle n'émet rien et ne contient aucune clé.
- **Citations vérifiables.** Tous les textes de traités proviennent des pages officielles WIPO Lex, et le script d'extraction `wipo_lex_fetch.py` est fourni pour permettre une réextraction et une contre-vérification. Les annexes « points clés et errata » sont des synthèses de la compétence, non des textes officiels : **citez toujours le corps du texte**.
- **Reproductible.** Chaque script de calcul de dates accepte `--today` pour reproduction, ce qui rend les résultats traçables.
- **Avertissement.** La sortie des scripts est une estimation et une alerte ; la notification officielle de l'OMPI / du CNIPA et la facture officielle prévalent.

---

## Limites

Ce que la compétence ne fait pas, dit franchement :

- **Elle ne couvre pas l'interprétation article par article du droit substantiel des marques des parties désignées, ni les stratégies contentieuses.** Le droit national (dispositions précises du Lanham Act américain, règlement sur la marque de l'UE, pratique nationale de recours) relève du droit local ou d'un conseil local.
- **Elle ne traite pas les demandes nationales ou régionales.** Les dépôts directs auprès de l'USPTO, de l'EUIPO ou du JPO, hors voie Madrid, sont hors du flux principal et n'apparaissent qu'à titre de comparaison.
- **Elle ne porte pas d'appréciation subjective de similitude ni de pronostic de succès.** Elle fournit un cadre de réponse au refus et des modèles ; elle ne prédit ni la registrabilité, ni le risque de conflit, ni l'issue d'une affaire.
- **Elle n'extrait pas les cours de change en direct.** Le cours du CHF est volatil et doit être vérifié avant chaque paiement.
- **Elle ne remplace pas le jugement professionnel.** C'est une aide à la pratique, non un avis juridique.
- **Sans le dossier, elle ne peut pas produire de plan ciblé.** Commencez par fournir la notification de refus, le numéro d'enregistrement et les parties désignées.

**Pour obtenir la meilleure réponse :** précisez le type d'opération (dépôt / renouvellement / réponse à un refus / modification ou cession / transformation / taxes / délais) + les faits clés (parties désignées, nombre de classes, statut de la base, date ou numéro d'enregistrement, existence et origine d'un refus) + le livrable attendu (estimation de taxes / compte à rebours / modèle de réponse / étapes / liste de risques).

---

## Structure du dépôt

```
madrid-trademark/
├── SKILL.md                          # Document principal (lu par l'agent ; structure en six parties : rôle / tâche / contexte / processus / règles / format de sortie)
├── README.md                         # Chinois simplifié (par défaut)
├── README.zh-Hant.md                 # Chinois traditionnel
├── README.en.md                      # English
├── README.fr.md                      # Français (ce fichier)
├── README.es.md                      # Español
├── README.ar.md                      # العربية
├── README.ja.md                      # 日本語
├── README.ru.md                      # Русский
├── LICENSE                           # Licence MIT
├── logo.png                          # Marque de l'entreprise (en-tête du README)
├── references/                       # 15 éléments : 13 Markdown + 2 PDF officiels
│   ├── madrid-agreement.md / -en.md           # Arrangement de Madrid (18 articles, texte intégral zh/en)
│   ├── madrid-protocol.md / -en.md            # Protocole de Madrid (16 articles + 10 sous-règles, zh/en)
│   ├── madrid-regulations.md / -en.md         # Règlement d'exécution (41 règles + notes officielles, zh/en)
│   ├── madrid-admin-instructions.md / -en.md  # Instructions administratives (7 parties, 19 sections + 11bis, zh/en)
│   ├── madrid-fees.md                         # Source unique des taxes (taxes individuelles de 76 parties)
│   ├── madrid-declarations.md                 # Source unique des déclarations (17 catégories + délais de réponse des 38 membres)
│   ├── madrid-faq.md                          # FAQ + 16 contre-exemples + index des articles
│   ├── madrid-goods-services-classification.md    # Synthèse du guide de classification (5e éd., 2026)
│   ├── madrid-fast-track-examination-cnipa.md     # Examen accéléré du CNIPA : points pratiques
│   ├── madrid-efiling-applicant-guide.pdf         # Guide du déposant e-Filing de l'OMPI (officiel, 43 p.)
│   └── madrid-goods-services-classification-guide.pdf  # Guide officiel de classification (5e éd.)
├── scripts/                          # 9 éléments : 7 Python + 2 JSON
│   ├── madrid_fee.py                 # Calculateur de taxes (instantané hors ligne, --date applique les entrées en vigueur)
│   ├── madrid_fee_data.json          # Miroir machine des taxes (aligné partie par partie avec madrid-fees.md)
│   ├── madrid_deadline.py            # Calculateur de délais (refus 12/18/25 mois + réponse, 38 membres)
│   ├── madrid_response_times.json    # Données des délais de réponse (table règle 17(7) complète + 6 départs)
│   ├── madrid_renewal.py             # Fenêtre de renouvellement et surtaxe de grâce
│   ├── madrid_feecalc_live.py        # Mesure des taxes en direct (navigateur pilotant le calculateur officiel ; outil d'arbitrage)
│   ├── wipo_lex_fetch.py             # Extraction littérale des traités WIPO Lex (vers Markdown)
│   ├── madrid_dateutil.py            # Utilitaires de dates partagés (mois civil, fin de mois, année bissextile)
│   └── selftest.py                   # 9 groupes d'auto-tests (dont deux contrôles de cohérence)
└── templates/                        # À copier avant usage ; ne pas modifier les originaux sur place
    ├── madrid_application_checklist.md      # Liste d'auto-contrôle avant dépôt du MM2
    └── madrid_refusal_response_memo.md      # Note de réponse au refus provisoire
```

> **Règle de structure.** Strictement 2 niveaux (niveau 1 = `SKILL.md` / `references/` / `scripts/` / `templates/` ; niveau 2 = fichiers de chaque répertoire), sans imbrication plus profonde.
> **Encodage.** Les fichiers Markdown sont en CRLF pur, sans BOM ; les `.py` et `.json` de `scripts/` sont en LF, UTF-8 sans BOM.
> **Discipline de maintenance.** Toute modification d'un montant de taxe doit être répercutée dans `references/madrid-fees.md` et `scripts/madrid_fee_data.json`, et `py scripts/selftest.py` doit passer tous les cas avant commit.

---

## Origine

La difficulté d'un dossier Madrid est très concrète : **la même chose est écrite une fois dans l'Arrangement, une fois dans le Règlement d'exécution, une fois dans le barème des taxes, et une fois encore dans les déclarations de chaque partie contractante** — et toute révision de l'un de ces textes peut invalider une position encore correcte la semaine précédente. Une modification tarifaire, une déclaration de plus, un nouveau membre : en pratique, il faut tout revérifier.

D'où l'extraction des quatre couches de textes juridiques (Arrangement / Protocole / Règlement / Instructions administratives), avec le barème, la page des déclarations et les guides officiels, en textes intégraux ; l'horodatage de toutes les données volatiles ; et l'écriture en scripts reproductibles de tout ce qui se calcule — délais, taxes. L'objectif : faire de la « vérification » un appel, et non un après-midi.

---

## License

Publié sous **licence MIT** ([LICENSE](LICENSE)). Vous êtes libre d'**utiliser, modifier et distribuer** ce projet, **y compris à des fins commerciales** — usage interne, livraison dans un dossier client, œuvres dérivées et rediffusion, sans autorisation préalable, sans frais et sans notification. L'attribution n'est pas obligatoire, mais appréciée.

Copyright **Hui Ning IP (辉宁知识产权)**.

**Périmètre.** La licence MIT couvre le code (`scripts/`) et la documentation propres à cette compétence (`SKILL.md`, les README, les synthèses de `references/`, `templates/`). Les textes officiels WIPO Lex reproduits littéralement dans `references/` et les deux PDF officiels OMPI/CNIPA restent la propriété de leurs organismes émetteurs : ils sont joints pour faciliter la vérification et **ne sont pas couverts par cette licence** — respectez les conditions de leurs sources.

Toute conclusion produite avec cette compétence doit être confrontée au droit national de la partie désignée et aux faits de l'espèce avant d'être invoquée ; en tant qu'aide à la pratique, elle ne constitue pas un avis juridique.

---

## Contact

Maintenu par **Hui Ning IP (辉宁知识产权)** — équipe chinoise de conseils en brevets et en marques, couvrant la procédure en brevets, la procédure en marques et les services internationaux de propriété intellectuelle.

- Les Issues sont bienvenues pour signaler une donnée périmée, une erreur de citation ou un problème de script. **Pour signaler un écart sur une donnée volatile, joignez l'URL de la page officielle et une capture d'écran** ; la date d'arrêté sera mise à jour après vérification.
- Si vous connaissez une position pratique locale dans une partie contractante, partagez-la : cette compétence est neutre par conception, et ces différences de juridiction sont précisément ce dont elle a le plus besoin.
