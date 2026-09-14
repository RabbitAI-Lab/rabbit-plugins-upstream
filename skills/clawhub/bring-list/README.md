# 🛒 bring-list — The Best Bring! Skill for OpenClaw

**Lightweight. Most features. Clean code. Privacy-first.**

The only Bring! skill that runs everywhere — just `curl` and `jq`, no Node.js, no Python, no pip, no npm. Works on any Linux, any container, any VPS out of the box.

## Why bring-list?

There are 6+ Bring! skills on ClawHub. Here's why this one wins:

### 🏆 Most features
Other skills only do add + remove. **bring-list** does everything:
- ✅ Add items (with quantity/description like "low fat, 1L")
- ✅ Add multiple items in one go ("Milk, Bread, Cheese|Gouda, Butter|Irish")
- ✅ Check off items when you've bought them
- ✅ Uncheck items (move back to shopping list)
- ✅ Remove items completely
- ✅ Remove or check off multiple items at once
- ✅ View all your lists and items
- ✅ JSON output for automation

### 🪶 Lightweight
| | **bring-list** | Others |
|---|---|---|
| Needs | `curl` + `jq` | Node.js + npm, or Python + pip |
| Install time | Instant | Minutes of downloading packages |
| Works in containers | Always | Often breaks |

### 🧠 Built for AI agents
- **Step-by-step Agent Setup Guide** — your agent knows exactly how to help you set up
- **Private terminal setup** — passwords are entered only in your own terminal, never in chat and never stored on disk
- **Default list support** — say "put milk on the list" without naming the list every time
- **Partial name matching** — "einkauf" finds "Einkaufsliste"
- **Smart argument parsing** — the agent figures out what's an item and what's a list name

### 🔒 Clean & secure
- Passwords are never stored; the protected token cache is owner-only
- No malware, remote code, or third-party telemetry
- No external services — talks directly to Bring! API
- Fully auditable: one bash script, ~850 lines, no magic

## Installation

```bash
clawhub install bring-list
```

## Quick Setup

Tell your agent: *"Set up the Bring shopping list skill"* — it will walk you through it.

Or manually:
```bash
scripts/bring.sh setup
```

You need a [Bring!](https://getbring.com) account (free). If you signed up via Google/Apple, set a direct password first in the Bring! app (Settings → Account → Change Password).

## Just Talk Naturally

- *"Put milk and eggs on the shopping list"*
- *"What's on our list?"*
- *"Check off the butter, we got it"*
- *"Add bread, cheese, and yogurt to the list"*
- *"Remove the tomatoes"*

Your agent handles the rest.

## Configuration

`~/.config/bring/credentials.json`:
```json
{
  "email": "your@email.com",
  "default_list": "Einkaufsliste",
  "country": "DE"
}
```

- `default_list` — Skip typing the list name every time
- `country` — Item catalog language (default: `DE`). Use `AT`, `CH`, `US`, `FR`, etc.

## Good to Know

- **Shared lists sync instantly** — your partner sees changes in real time
- **Lists must be created/deleted in the Bring! app** — API limitation, not ours
- **Special characters fully supported** — umlauts, quotes, emoji, all fine
- **Token auto-refreshes** — rerun setup only if the refresh token expires

## Privacy

No third-party services, no telemetry, no cloud — the skill talks **only** to Bring!'s own API (`api.getbring.com`).

Run `scripts/bring.sh setup` in your own terminal. It reads the password with `read -s`, uses it for that login, and never writes it to disk or accepts it in chat. The email/profile lives in `~/.config/bring/credentials.json`; the owner-only access/refresh token lives in `~/.cache/bring/token.json` and remains a secret.

If you used an older version that stored a password in `credentials.json`, rerun setup to replace it with the password-free profile.

## License

MIT
