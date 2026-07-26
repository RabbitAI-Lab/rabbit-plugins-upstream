# Kleap recipes

Longer worked examples for the `kleap` skill. Load this only when the core
`SKILL.md` workflow isn't enough for the task at hand.

## Recipe 1 — full business site: create, connect a domain, then edit

```bash
# 1. Create — builds and deploys in one call, blocks until live.
npx -y @eliottd/kleap@latest create \
  "a one-page site for a bakery called Warm Loaf, warm earthy palette, \
   sections: hero, our story, menu with prices, contact form, hours"
# ✓ created app 4821 — https://warm-bakery-fold.kleap.io

# 2. User already owns bakery-warmloaf.com and wants it connected.
npx -y @eliottd/kleap@latest domains connect bakery-warmloaf.com 4821
# ✓ bakery-warmloaf.com pending DNS — point A @ to <ip>, propagation 5-60min

# One line: relay the printed A-record IP and the propagation window to the
# user. TLS auto-issues once DNS propagates; use --json for the full
# dns_config object.

# 3. A week later: tweak the copy.
npx -y @eliottd/kleap@latest edit 4821 "change the headline to 'Baked at dawn, gone by noon'"
# ✓ edited app 4821 — https://warm-bakery-fold.kleap.io
```

Report the connected custom domain to the user once DNS is set, but keep
using the `kleap.io` URL (or the numeric id) for further `edit`/`status`
calls until they confirm the custom domain resolves — it's the one
guaranteed to already work.

## Recipe 2 — non-blocking flow (agent has other work to do)

```bash
npx -y @eliottd/kleap@latest create "a landing page for my podcast" --no-wait --json
# { "app_id": 5310, "task_id": "t_9f2...", ... }

# ... do other work ...

npx -y @eliottd/kleap@latest status 5310
# ✓ Podcast Landing (5310) — live: https://crisp-mic-drift.kleap.io
# (or "— not published" while the build is still running; poll again)
```

Don't tight-loop `status` faster than every ~10-15s — builds take 1-15
minutes; polling harder doesn't make it finish sooner.

## Recipe 3 — parsing `--json` output in a script

```bash
url=$(npx -y @eliottd/kleap@latest create "a landing page for my podcast" --json \
  | node -e 'let d="";process.stdin.on("data",c=>d+=c).on("end",()=>{
      const p = JSON.parse(d);
      console.log(p.url || p.production_url || "");
    })')
if [ -z "$url" ]; then
  echo "create failed or is still building — check status" >&2
else
  echo "Live: $url"
fi
```

Prefer checking the process exit code (`$?` / `child_process` non-zero) over
trying to detect failure purely from JSON shape. On failure with `--json`,
stdout is `{"error":{"code":...,"message":...}}` — see `troubleshooting.md`
for the codes.

## Recipe 4 — forms and a contact form

There is no separate "create a form" command. Ask for it in plain language as
part of `create` or `edit` — e.g. `"...with a contact form that emails the
owner"` — and Kleap wires up hosting, storage and the submit endpoint as part
of the normal build. Don't invent a `kleap forms` subcommand; it doesn't
exist in this CLI version.

## Recipe 5 — finding an existing site instead of asking the user for an id

```bash
npx -y @eliottd/kleap@latest list --q bakery
# 4821  Warm Loaf Bakery  https://warm-bakery-fold.kleap.io
```

Use the returned id/url for subsequent `edit`/`status`/`publish` calls rather
than asking the user to look it up themselves.
