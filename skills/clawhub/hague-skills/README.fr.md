🌐 [中文](README.md) · [繁體中文](README.zh-Hant.md) · [English](README.en.md) · **Français** · [Español](README.es.md) · [العربية](README.ar.md) · [日本語](README.ja.md) · [Русский](README.ru.md)

<p align="center"><img src="logo.png" alt="Hui Ning IP" width="150"></p>

# Hague Design System · Compétence pratique pour l'enregistrement international des dessins et modèles

> *« Une seule question, une réponse directement exploitable en matière de dessins et modèles. »*
> *"Ask once. Get a filing-ready Hague design practice answer."*

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.10.8-blue.svg)](references/changelog.md)
![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)
[![Hague Members](https://img.shields.io/badge/Hague%20Members-83-green)](https://www.wipo.int/en/web/hague-system)
![No-Fabrication](https://img.shields.io/badge/Principle-No--Fabrication-orange)

**Une compétence complète dédiée au système de La Haye, pour les conseils en dessins et modèles, les juristes PI et les directions juridiques du monde entier — centrée sur la phase internationale de l'OMPI, utilisable depuis la perspective de toute partie contractante, avec un chapitre optionnel OMPIC/Chine.**

Pas une encyclopédie : des chemins de vérification pour chaque étape de dépôt et d'examen, des sources juridiques vérifiables clause par clause (Acte de Genève / Règlement d'exécution / Instructions administratives / Guide), des spécifications chiffrées pour les reproductions, l'unité de dessin et la priorité, ainsi que des paramètres de taxes et de délais à revérifier (avec un script intégré de calcul des taxes).

Conçue selon le format universel Agent Skills (`/SKILL.md`) ; fonctionne avec tout agent prenant en charge les skills.

[Fonctionnalités](#fonctionnalités) · [Installation](#installation) · [Mécanismes clés](#mécanismes-clés) · [Structure du dépôt](#structure-du-dépôt) · [Limites](#limites)

---

## Installation

### Option 1 : script de synchronisation (recommandé)

```bash
# Windows
py -3 scripts/sync_to_local.py

# macOS / Linux
python3 scripts/sync_to_local.py

# Options courantes
py -3 scripts/sync_to_local.py --dry-run                # prévisualisation, sans écriture
py -3 scripts/sync_to_local.py --target D:/path/to/skills   # répertoire de skills personnalisé
```

Le script synchronise, en sens unique, ce dépôt comme une compétence unique vers votre répertoire local de skills (par défaut `~/.workbuddy/skills`, installée sous `hague-design-system/`) : les fichiers nouveaux ou modifiés sont écrasés, les fichiers obsolètes supprimés, et **les métadonnées locales telles que `_user_meta.json` sont préservées** ; les fichiers propres au dépôt (README, LICENSE, logo, etc.) ne sont jamais installés dans le répertoire de skills.

### Option 2 : copie manuelle

Copiez le dossier entier du dépôt dans votre répertoire de skills (par ex. `~/.workbuddy/skills/`) et renommez-le en `hague-design-system`, puis redémarrez ou rechargez l'application.

> ⚠️ Compétence multi-fichiers : la base de connaissances sous `references/` (Acte et Règlement d'exécution, Instructions administratives, Guide du système de La Haye, chapitre Chine optionnel, etc.) est référencée depuis `SKILL.md` par des chemins relatifs `@` — **un seul fichier manquant rompt la chaîne**. Copiez les répertoires entiers ; ne prenez pas `SKILL.md` seul.

## Fonctionnalités

| Domaine | Description |
|------|------|
| Demande internationale | Qualité pour déposer ; dépôt DM/1 et eHague ; exigences relatives aux reproductions ; unité de dessin ; priorité ; voies de dépôt et étapes de procédure |
| Enregistrement et publication | Examen formel et corrections ; enregistrement international et date d'enregistrement ; publication et report ; retraits |
| Examen et recours | Réponse aux refus des Offices désignés ; déclarations d'octroi de protection et leurs effets ; nullité ; voies après refus |
| Renouvellement et modifications | Durée et renouvellement (y compris délai de grâce) ; changement de titulaire, de données du titulaire, de mandataire, limitation, renonciation |
| Taxes | Les sept types d'opérations (demande / renouvellement / changement de titulaire / changement de données du titulaire / changement de nom et d'adresse du créateur / limitation / renonciation) ; calculateur de taxes de La Haye ; structure des taxes en CHF ; script intégré de calcul |
| Recherche | Recherche d'antériorités et de statut juridique dans DesignDB |
| Optionnel · Chapitre Chine | Déclarations de la Chine ; examen et recours devant l'OMPIC ; transmission et opérations du système ; demandes divisionnaires ; notes en CNY (les praticiens hors Chine peuvent l'ignorer entièrement) |

## Mécanismes clés

1. **Cœur universel** : la phase internationale de l'OMPI (commune à toutes les parties contractantes) constitue le corps principal ; le chapitre OMPIC/Chine est optionnel et peut être ignoré par les praticiens hors Chine ;
2. **Source juridique et données à point unique** : les données volatiles (taxes, déclarations) convergent vers une source d'autorité unique ; historique des versions et index des fichiers centralisés (`changelog.md`, `11-file-index.md`) pour éviter toute divergence ;
3. **Divulgation progressive** : les textes longs (dont le Guide du système de La Haye de 286 Ko) résident dans `references/`, chargés à la demande avec un index par numéro de ligne, sans saturer le contexte ;
4. **« Aucune donnée » faute de source** : toute information incertaine est signalée comme telle — aucune disposition, aucun délai, aucun montant inventé ; les réponses livrées n'utilisent jamais de tableaux Markdown (listes et définitions en ligne à la place).

## Structure du dépôt

```text
HAGUE-SKILLS/                        # Racine du dépôt = racine de la compétence (dépôt mono-compétence)
├── SKILL.md                         # Plan de contrôle : rôle / tâche / contexte / processus / règles / sortie
├── references/                      # 12 fichiers de connaissances (dont chapitre Chine optionnel, changelog, index)
├── scripts/                         # Scripts de la compétence (calculateur, assistant) + sync_to_local.py
├── README.md                        # 简体中文 (par défaut)
├── README.zh-Hant.md                # 繁體中文
├── README.en.md                     # English
├── README.fr.md                     # Français (ce fichier)
├── README.es.md                     # Español
├── README.ar.md                     # العربية (RTL)
├── README.ja.md                     # 日本語
├── README.ru.md                     # Русский
├── LICENSE                          # Licence MIT
└── logo.png                         # Marque (en-tête du README)
```

- La racine du dépôt est la racine de la compétence ; une fois installée, elle est strictement sur **2 niveaux** (`SKILL.md` / `references/` / `scripts/`), conformément à la structure officielle WorkBuddy ;
- Les fichiers propres au dépôt (`README*.md`, `LICENSE`, `logo.png`, `scripts/sync_to_local.py`) ne sont jamais installés dans le répertoire de skills ;
- Fichiers de skills : **CRLF, UTF-8 sans BOM**.

## Données et actualité

- Les sources juridiques suivent les **versions officielles en vigueur de l'OMPI / de l'OMPIC** ; la date de référence des données et le cycle de revérification recommandé sont indiqués dans la compétence (liste §3.0) ;
- Pour les données volatiles (taxes, taxes de désignation individuelle, déclarations, taux de change), revérifiez les dernières publications officielles ou le calculateur de taxes avant tout usage au dossier ;
- La sortie est une référence pratique — **elle ne constitue pas un conseil juridique**.

## Limites

- Ne remplace ni l'appréciation officielle ni l'appréciation au cas par cas : délais, taxes et conclusions procédurales relèvent des notifications de l'Office désigné et des publications officielles ;
- Aucune invention : les données introuvables sont renvoyées comme « aucune » ;
- La couverture juridique se limite à la procédure et aux règles communes du système de La Haye ; le droit substantiel et la pratique d'examen de chaque partie contractante désignée suivent les positions officielles de cette partie.

## License

[MIT](LICENSE) © 2026 Hui Ning IP（辉宁知识产权）.

- Le contenu de la compétence elle-même (organisation et annotations dans `SKILL.md` et `references/`) est sous MIT ;
- Les textes officiels de l'OMPI reproduits ou cités dans `references/` (Acte de Genève, Règlement d'exécution, Instructions administratives, Guide, etc.) restent la propriété de l'OMPI et ne sont pas couverts par cette licence.

## Contact

- Questions et suggestions : ouvrez une Issue dans ce dépôt ;
- Conçu et maintenu par Hui Ning IP (une équipe chinoise de conseils en brevets).
