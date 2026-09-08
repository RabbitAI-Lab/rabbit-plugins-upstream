# Publishing text-to-infographic

This folder is the **direct upload root** for GitHub and ClawHub.

## 1. Local validation

```bash
python3 scripts/validate_infographic_plan.py examples/*.json --pretty
python3 scripts/build_infographic_adapters.py examples/infographic-roadmap-demo.json --out ./adapter-output/roadmap --pretty
```

## 2. GitHub publish

Recommended:
- create a public repository named `text-to-infographic`
- upload the contents of this folder as the repository root
- keep `SKILL.md` at the repository root

## 3. ClawHub publish

Dry run first:

```bash
clawhub login
clawhub whoami
clawhub skill publish . \
  --slug text-to-infographic \
  --name "Text to Infographic" \
  --version 0.1.0 \
  --categories creative,knowledge,productivity \
  --topics "infographic,whiteboard,svg,lark,feishu" \
  --changelog "Initial standalone infographic-first release" \
  --dry-run
```

Actual publish:

```bash
clawhub skill publish . \
  --slug text-to-infographic \
  --name "Text to Infographic" \
  --version 0.1.0 \
  --categories creative,knowledge,productivity \
  --topics "infographic,whiteboard,svg,lark,feishu" \
  --changelog "Initial standalone infographic-first release"
```

If publishing under an org owner, add:

```bash
--owner <owner>
```
