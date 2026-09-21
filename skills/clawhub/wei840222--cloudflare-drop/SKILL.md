---
name: cloudflare-drop
description: Deploy small, non-sensitive static sites to temporary Cloudflare Workers previews. Use when an intended user explicitly accepts Cloudflare terms and needs a short-lived workers.dev URL with a privately delivered Claim URL.
---

# Cloudflare Drop

## Deploy

1. Show the intended user the Cloudflare Terms and Privacy Policy, then obtain explicit acceptance.
2. Choose a new private path for the Claim URL; the script creates it as `0600` and refuses to overwrite it.
3. Run:

```bash
node <installed-skill-dir>/scripts/deploy.mjs <static-directory> \
  --accept-terms \
  --claim-url-file <new-private-file>
```

4. Return the Live URL. Read the Claim URL from its private file and deliver it only to the intended user.

## Boundaries

- Deploy only regular files with a root `index.html`; never deploy private files, symlinks, or large media bundles.
- Do not expose Claim URLs in group chat, browser output, analytics, or logs.
- Stop before provisioning when consent, input validation, or Claim-file creation fails.

## Reference

Read `references/cloudflare-api.md` before diagnosing an API failure, retrying a fresh deployment, or deciding whether a site exceeds this skill's limits.
