---
name: skroll
description: Drive Skroll (skrollai.com) decks via the official CLI. Use when the user asks for Skroll specifically — create/edit/generate/version/export Skroll decks, brands, or PDF/PPTX through `npx @skrollai/cli`. Do not use for generic local slide advice unrelated to Skroll.
---

# Skroll

Skroll is a browser-canvas presentation tool. This skill drives it through the official CLI, which uses the same OAuth login as the MCP server.

## Setup

Needs Node.js 22+.

**If you cannot open a browser** (headless agent, CI, container), do not run `login` — it
waits five minutes for a browser callback and then times out. Ask the user for an API key
from https://skrollai.com/app/settings/integrations and export it:

```bash
export SKROLL_API_KEY=sk_…      # or SKROLL_TOKEN=<OAuth access token>
```

**If a browser is available**, log in once (PKCE, no API key needed), then confirm:

```bash
npx @skrollai/cli login
npx @skrollai/cli whoami
```

A first-time user is signed up and given an organization automatically during `login`;
there is nothing to set up in the web app first.

Default origin is `https://skrollai.com`. Override with `--origin` or `SKROLL_ORIGIN` for local
or self-hosted instances — log in once per origin, since a stored credential is only ever sent
to the host that issued it. `--token` / `SKROLL_TOKEN` works against any origin.

## Commands

The CLI maps 1:1 to the Skroll MCP tools (plus `download_export`, which writes a file). Run `npx @skrollai/cli help` for flags.

| Task | Command |
| --- | --- |
| List decks | `npx @skrollai/cli list_decks` (add `--scope org` for the whole organization; default is your own) |
| Create a blank deck | `npx @skrollai/cli create_deck --title "Q3 review"` (add `--format webpage` for a scrolling page instead of 16:9 slides, `--brand-id <id>` to style it) |
| Generate from a brief | `npx @skrollai/cli generate_deck --id <deckId> --mode create --brief "Series A pitch for Acme"` |
| Inspect a deck | `npx @skrollai/cli get_deck --id <deckId>` |
| Patch title or visibility | `npx @skrollai/cli update_deck --id <deckId> --title "New title"` |
| Replace canvas source | `npx @skrollai/cli set_deck_content --id <deckId> --source @deck.tsx` |
| Natural-language edit | `npx @skrollai/cli edit_deck --id <deckId> --instruction "Make slide 2 a comparison"` |
| Delete a deck | `npx @skrollai/cli delete_deck --id <deckId>` |
| Versions | `list_deck_versions`, `get_deck_version`, `revert_deck_version` |
| Export PDF / PPTX | `create_export --id <deckId> --format pdf` then `get_export --id <exportId>` |
| Download the file | `download_export --id <exportId> --out ./deck.pdf` |
| Brands | `list_brands`, `get_brand`, `create_brand_from_url --url https://…`, `delete_brand` |
| Sign out | `npx @skrollai/cli logout` |

Commands print the raw API payload. Prefix a flag value with `@` to read it from a file.

`generate_deck`, `edit_deck` and `create_brand_from_url` run synchronously and can take one to three minutes. `create_export` is asynchronous: poll `get_export` until status is `completed`, then `download_export`.

## Errors worth handling

Every failure is JSON: `{"error":{"code":…,"message":…}}`. Three are worth reacting to
rather than retrying:

- **402 `payment_required`** — the organization has used its free allowance (10 skrolls,
  100 edits). Retrying will never succeed. Tell the user, and point them at
  https://skrollai.com/app/settings/billing.
- **429 `rate_limited`** — back off for the `retryAfterSeconds` in the response.
  `generate_deck`, `edit_deck`, `create_brand_from_url` and `create_export` share a budget
  of 10 per minute; everything else is 120 per minute.
- **401 `unauthorized`** — the session expired or was revoked. Run `login` again, or check
  `SKROLL_API_KEY`.

## Sharing

Public viewer URLs look like `https://skrollai.com/d/f4zqohxo7d`. After `update_deck --visibility public`, share the `publicUrl` field from the JSON. `get_deck` and `list_decks` return the same field when the skroll is public. Never invent a share link from the deck id, title, or API path.

## Docs

- Product: https://skrollai.com
- CLI: https://skrollai.com/developers/cli
- MCP (same tools, OAuth in the client): https://skrollai.com/developers/mcp
- REST: https://skrollai.com/developers
