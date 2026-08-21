# Publish checklist — Vedetta skill

## Before upload

1. Publisher is **korra.finance** (SKILL.md frontmatter). Set the same on the ClawHub form.
2. Disclaimer lives in SKILL.md body (agents must keep it). Paste a short version on ClawHub listing:
   "Descriptive research only. Not financial advice, investment recommendations, or buy/sell instructions."
3. Do **not** add `skill-card.md` — ClawHub generates that card; publishing it fails or is ignored.
4. Confirm no secrets in the folder:
   ```bash
   grep -RniE '0x[a-fA-F0-9]{64}|PRIVATE_KEY|mnemonic' . || true
   ```
5. Optional self-scan:
   ```bash
   hermes skills publish . --to clawhub
   ```

## Zip (already built next to this folder)

```
C:\Users\Mommy\Desktop\donut_output\vedetta-skill.zip
```

Rebuild:
```bash
cd /mnt/c/Users/Mommy/Desktop/donut_output/vedetta-skill
# python zip under parent; do not include skill-card.md
```

## ClawHub

- Submit: https://clawhub.ai/submit
- CLI (if available): `clawhub publish ./vedetta-skill --slug vedetta --name "Vedetta — x402 Market Intelligence" --version 2.12.0-v8`
- Buyer scripts in package: `scripts/pay.mjs` (Base EVM) · `scripts/pay-sol.mjs` (Sol SVM; Tier B)

## Hermes GitHub path

```bash
hermes skills publish ./vedetta-skill --to github --repo YOUR_USER/skills
```

## Smoke after someone installs

```bash
curl -s https://vedetta.dethboy.com/health
hermes skills list | grep -i vedetta
```
