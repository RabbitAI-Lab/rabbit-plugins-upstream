# Rebase d'une branche PR sur upstream/main (fork-as-live-install)

Recette validée 2026-07-31 sur l'install git d'Hermes
(`~/.hermes/hermes-agent`, origin=`chpomob/hermes-agent` fork, upstream=`NousResearch/hermes-agent`).
Branche `feat/status-bar-hook-all-widths` : 4 commits locaux, **4393 commits derrière** upstream/main,
PR #63824 en état CONFLICTING, `hermes update` en échec.

## Diagnostic (avant de toucher quoi que ce soit)

```bash
git status                                  # branche courante + divergence affichée
git branch -vv                              # tracking: [upstream/main: en avance de N, en retard de M]
git log --oneline upstream/main..HEAD       # les commits locaux (la feature)
git log -1 --format="%h %ad %s" --date=short upstream/main   # fraîcheur d'upstream
git merge-base HEAD upstream/main           # point de divergence
# La feature a-t-elle déjà été mergée upstream ? (grep sur la branche upstream)
git grep -l "on_status_bar_render" upstream/main -- '*.py'
# État de la PR
gh pr view <branch> --repo NousResearch/hermes-agent --json mergeable,mergeStateStatus,state
# → mergeable=CONFLICTING confirme le drift ; MERGEABLE après rebase.
# L'update hermes fait quoi ? (mécanisme fork)
# hermes_cli/update_cmd.py: _sync_with_upstream_if_needed() — si origin/main est
# strictement derrière upstream/main, il pull upstream puis push le fork (fast-forward).
```

## Procédure

### 1. Backup (ne JAMAIS sauter)

```bash
git branch backup/adversarial-squashes main   # sauve les squashes locaux de main
git tag backup/feature-pre-rebase HEAD        # sauve l'état exact de la feature
```

### 2. Fetch + rebase

```bash
git fetch upstream main
git rebase upstream/main          # rejoue les commits locaux un par un sur upstream
```

Chaque commit peut confliter — résoudre dans l'ordre, `git rebase --continue` entre chaque.

### 3. Résolution de conflit : GARDER LES DEUX CÔTÉS

Cas validé (cli.py) : upstream avait ajouté `_status_bar_goal_segment`,
`battery_prefix`, `focus_label` dans la même fonction (`_build_status_bar_text`)
que la feature étendait (`_get_status_bar_plugin_values` + `plugin_values`).
Le mauvais réflexe serait de choisir un côté. Le bon :
- garder la méthode upstream ET la méthode de la feature (les deux coexistent) ;
- dans la branche narrow (`width < 52`), convertir la version upstream (concaténation
  `text = f"..."`) en liste `parts` pour pouvoir y injecter `parts.extend(plugin_values)`
  tout en conservant `battery_label`/`goal_segment`/`focus_label`/`yolo_active`.

Vérifier après coup : `git diff --name-only --diff-filter=U` vide, plus aucun marqueur
`<<<<<<<` / `=======` / `>>>>>>>` dans les fichiers.

### 4. `rebase --continue` non-interactif

```bash
GIT_EDITOR=true git rebase --continue
```

Sans `GIT_EDITOR=true`, un terminal d'agent (stdin non-TTY) échoue avec
`error: There was a problem with the editor 'editor'`. Le truc vaut pour tout
rebase/commit non-interactif. (`git rebase --abort` reste la sortie de secours.)

### 5. Vérification

```bash
python3 -m py_compile cli.py hermes_cli/hooks.py ...        # syntaxe des fichiers touchés
venv/bin/python -m pytest tests/cli/test_cli_status_bar.py tests/hermes_cli/test_hooks_cli.py tests/hermes_cli/test_plugins.py -q
scripts/run_tests.sh tests/cli/test_cli_status_bar.py ...   # runner canonique (CI-parity, hermetic)
```

Runner canonique = `scripts/run_tests.sh` (probe `.venv`, puis `venv`). Résultat validé :
139 passed, 0 failed. Les diagnostics Pyright préexistants sur cli.py (typage du fichier
entier) ne sont PAS des régressions — les ignorer, la syntaxe et pytest font foi.

### 6. Force-push → PR mergeable

```bash
git push --force-with-lease origin feat/status-bar-hook-all-widths
gh pr view <num> --repo NousResearch/hermes-agent --json mergeable,mergeStateStatus
# MERGEABLE ✓ (mergeStateStatus=BLOCKED = review requise, normal, pas une erreur)
```

`--force-with-lease`, jamais un `--force` nu : échoue si quelqu'un d'autre a poussé.

### 7. Realigner main + synchroniser le fork

```bash
git branch -f main upstream/main     # déplace main sans checkout
git checkout main
git merge-base --is-ancestor origin/main upstream/main && echo "FF OK"   # sécurité avant push
git push origin main                 # fast-forward le fork → origin/main == upstream/main
```

Vérifier ensuite que la synchro fork d'hermes update voit "up to date".

### 8. Confirmation finale

```bash
hermes update --check     # → "Already up to date."
```

## Règle de maintenance (prévention)

- **`main` local reste aligné sur upstream/main en permanence.** Jamais de squash
  adversarial sur `main` — les squashes du pipeline vont sur des branches de feature.
- Les features/loops vivent sur des branches (`feat/...`, `loop/...`) ; seul `main`
  track upstream. C'est ce qui garde `hermes update` fonctionnel.
- Après chaque cycle de loops sur l'install, si une PR est ouverte : rebaser tôt et
  souvent (le drift ne fait qu'empirer), pas seulement quand `hermes update` casse.
