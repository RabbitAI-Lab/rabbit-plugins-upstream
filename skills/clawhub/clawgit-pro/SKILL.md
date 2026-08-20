---
name: ClawGit Pro
slug: clawgit-pro
version: 1.0.0
description: "Interagér med GitHub via `gh` CLI — issues, PRs, CI-runs og avancerede API-queries. PLUS unik feature: repo-sundhedsrapport, auto-changelog-generator og issue-triage."
metadata: {"clawdbot":{"emoji":"🐙","requires":{"bins":["gh"]}}}
---

# ClawGit Pro

GitHub-skill baseret på `gh` CLI — **forbedret med 3 unikke features** som originalen ikke har:

## 🆕 Unikke features (findes ikke i originalen)

### Feature 1: Repo-sundhedsrapport
Få et hurtigt overblik over et repos tilstand — stars, åbne issues, PR-alder, CI-status
og aktivitet, alt i én rapport:

```bash
bash scripts/repo_health.sh owner/repo
```

### Feature 2: Auto-changelog-generator
Generér automatisk en CHANGELOG.md fra commits/PR'er mellem to tags eller siden en dato:

```bash
bash scripts/changelog.sh owner/repo v1.0.0 v1.1.0
bash scripts/changelog.sh owner/repo --since 2026-01-01
```

### Feature 3: Issue-triage
Kategorisér åbne issues efter alder, labels og forfatter — find hurtigt hvad der
trænger til opmærksomhed:

```bash
bash scripts/triage.sh owner/repo
```

---

## Standard-operationer (arvet fra originalen)

### Pull Requests
```bash
gh pr checks 55 --repo owner/repo
gh run list --repo owner/repo --limit 10
gh run view <run-id> --repo owner/repo
gh run view <run-id> --repo owner/repo --log-failed
```

### API for avancerede queries
```bash
gh api repos/owner/repo/pulls/55 --jq '.title, .state, .user.login'
```

### JSON-output
```bash
gh issue list --repo owner/repo --json number,title --jq '.[] | "\(.number): \(.title)"'
```

## Feedback
- Hjælpsom? → `clawhub star clawgit-pro`
