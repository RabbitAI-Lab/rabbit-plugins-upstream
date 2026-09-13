# HealthOS Skill — usage guide

The `healthos` skill gives Quark (your OpenClaw agent) **read-only access to a
HealthOS user's synced Apple Health data** through `api.healthosx.com`. You ask
about your health in natural language; Quark runs the allow-listed helper script
and answers.

## Where to use it

Quark is reachable the same ways it always is:

- **Telegram** — DM the bot.
- **Feishu** — DM the bot.
- **TUI** — `openclaw tui` on the Mac.

The skill triggers automatically when your question is about your health data.

## What you can ask

```
"today's health summary"
"how did I sleep last night?"
"my resting heart rate over the last week"
"steps and active energy for September"
"what workouts did I do this month?"
"my HRV trend over the last 30 days"
"what does my blood oxygen / VO2 max / resting energy look like?"
"what types of health data do I have synced?"   → coverage
"what can HealthOS read from my Apple Health?"  → catalog
```

## What data is available

The skill reads everything your iPhone has synced to HealthOS, through two
surfaces:

1. **Projected / chartable** — `summary`, `metrics`, `sleep`, `workouts`
   (the daily summary and per-type series the app itself charts).
2. **The raw archive** — `catalog` (all 165 supported types), `coverage`
   (what *you* actually have), `samples` / `events` (any type, source-faithful).

Types include heart rate, resting HR, HRV, respiratory rate, steps, active &
resting energy, distance, flights climbed, running metrics, blood oxygen,
VO₂ max, body temperature, weight/height/BMI/body fat, all dietary nutrients,
sleep stages, mindful minutes, workouts, symptoms, and more — whatever the user
has actually recorded in Apple Health.

> Note: the phone syncs what it *reads*. If a type is empty (`coverage` shows
> no rows for it), the user simply hasn't recorded that data in Apple Health —
> it is not a bug.

## Setup (already done for your account)

- **Skill installed** in Quark's workspace.
- **Token configured** in `HEALTHOS_API_TOKEN` (read scopes:
  `health:summary:read`, `health:metrics:read`, `health:sleep:read`,
  `health:workouts:read`).

For a *new* user account:

1. Generate a token **in the app** — not on the website. Open the HealthOS app
   (iPhone or https://app.healthosx.com), go to **Settings → API access**, tap
   **Create token**, and select the four read scopes (`health:summary:read`,
   `health:metrics:read`, `health:sleep:read`, `health:workouts:read`). The
   token is shown exactly once — copy it then. (Under the hood this calls
   `POST /api/v1/tokens`, which requires a logged-in session; a `hos_` token
   can never create another.)
2. Set it in Quark: add `HEALTHOS_API_TOKEN` to `env.vars` in
   `/root/.openclaw/openclaw.json` (or the equivalent agent env).

## Using the helper script directly

```bash
python scripts/healthos_api.py summary --date 2026-09-11
python scripts/healthos_api.py metrics --type heart_rate --from 2026-09-01 --to 2026-09-11
python scripts/healthos_api.py sleep --from 2026-09-08 --to 2026-09-11
python scripts/healthos_api.py workouts --from 2026-09-01 --to 2026-09-11
python scripts/healthos_api.py catalog
python scripts/healthos_api.py coverage
python scripts/healthos_api.py samples --type basal_energy --from 2026-09-01 --to 2026-09-11
python scripts/healthos_api.py events --type sleep_analysis --from 2026-09-08 --to 2026-09-11
```

`HEALTHOS_API_TOKEN` is read from the environment; never put it in a prompt.

## For developers

- API docs: `https://api.healthosx.com/docs` (OpenAPI) and
  `https://api.healthosx.com/llms.txt`.
- Developer program (early access — request-only, not a token portal):
  `https://healthosx.com/developers`
- Scopes and endpoint reference: see `references/api.md`.

## Privacy & safety

The skill is **read-only** — there is no write surface. It reports numbers and
trends and never diagnoses. Labs, DNA, and other separately-scoped data require
an explicit opt-in and are not part of this skill.
