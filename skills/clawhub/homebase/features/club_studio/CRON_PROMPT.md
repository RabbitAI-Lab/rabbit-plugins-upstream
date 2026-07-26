# Club Studio Watcher — Cron Prompt

Register this cron job via `openclaw cron add` (or `openclaw cron edit <id>`).
Do NOT edit `~/.openclaw/cron/jobs.json` directly — those changes are wiped
on daemon shutdown (see CLAUDE.md principle 10).

## Registration

Run from the homebase skill root (`~/.openclaw/workspace/skills/homebase`) in a
shell that has `OPENCLAW_GATEWAY_TOKEN` in env (openclaw normally sets this
up via login shell or keychain — if you get a `GatewaySecretRefUnavailableError`,
export it first or pass `--token`):

```bash
cd ~/.openclaw/workspace/skills/homebase && \
OWNER_PHONE=$(python3 -c "from core.config_loader import config; print(config.owner_phone)") && \
openclaw cron add \
  --name "Club Studio Watcher" \
  --cron "*/15 * * * *" \
  --thinking off \
  --channel whatsapp \
  --to "$OWNER_PHONE" \
  --message "$(sed -n '/^BEGIN PROMPT$/,/^END PROMPT$/p' features/club_studio/CRON_PROMPT.md | sed '1d;$d')"
```

`OWNER_PHONE` is read from `config.json` (`app.owner_phone`) — never hardcode
a phone number here. If `config.json` doesn't exist yet, copy it from
`config.example.json` and fill in your own values first.

Flags explained:
- `--cron "*/15 * * * *"` — every 15 min (matches `club_studio.poll_minutes`)
- `--message <text>` — agentTurn payload prompt. This job runs as an isolated
  session (no `--session main`), so the correct flag is `--message`, not
  `--system-event`. The daemon rejects `--system-event` on non-main sessions
  with `invalid cron.update params: isolated/current/session cron jobs
  require payload.kind="agentTurn" or "command"`.
- `--to "$OWNER_PHONE"` — the agent's *own reply text* goes to the OWNER DM,
  never a group. The agent posts to the configured WhatsApp groups itself
  via bash inside its turn, using the `targets` list `fetch_club_studio_emails`
  returns (sourced from `config.json`'s `whatsapp.groups[]`). This matches
  the school pattern. `NO_REPLY` from the agent suppresses delivery so owner
  isn't spammed on quiet polls.
- No `--session`, `--model`, or `--tools` — the job uses openclaw defaults:
  isolated session, the default local model configured in `openclaw.json`
  (currently `ollama/gemma4:26b`), and all tools available (the agent needs
  bash exec to call `python3 tools.py fetch_club_studio_emails`,
  `openclaw message send --target <jid>`, `add_calendar_event`, and
  `delete_calendar_event`).

To update just the prompt on the live job (does NOT recreate it):

```bash
cd ~/.openclaw/workspace/skills/homebase && \
openclaw cron edit <job_id> \
  --message "$(sed -n '/^BEGIN PROMPT$/,/^END PROMPT$/p' features/club_studio/CRON_PROMPT.md | sed '1d;$d')"
```

Find `<job_id>` with:
`sqlite3 ~/.openclaw/state/openclaw.sqlite "SELECT job_id FROM cron_jobs WHERE name='Club Studio Watcher';"`

## Prompt (agent-facing)

```
BEGIN PROMPT
[cron:club_studio_watcher Club Studio Watcher] Fetch a Club Studio Fitness email, announce it to your configured WhatsApp groups, and keep the family calendar in sync. Your own reply text always goes to the OWNER DM configured on this cron job (the --to flag at registration), never to any group.

REPLY DISCIPLINE — overrides everything below. Your final response text MUST be exactly one of these three shapes and nothing else:
  1. The literal token `NO_REPLY` — empty inbox, noise, past class, or any uncertainty. Silences delivery.
  2. A polished announcement per Step 4 — starts with `🏋️`, `⏳`, or `❌`.
  3. A diagnostic per Step 6 — starts with `⚠️ Club Studio watcher:`.

If a tool is missing, fails, times out, or the situation is unclear: reply `NO_REPLY`. Never narrate what you tried. Never mention tool names, tool availability, retries, or your own thinking (phrases like "I can't use...", "isn't available", "let me try...", "I need to...", "stop retrying" are BUGS — they will be delivered verbatim to the owner's WhatsApp). If you catch yourself typing first-person meta-commentary, replace the entire reply with `NO_REPLY`.

Step 1. Call `fetch_club_studio_emails` to get one raw email plus `targets` — a list of `{jid, name}` WhatsApp groups read from config.json. The fetch is hard-capped to one email per poll so backlogs drain over 15-min ticks; do not expect a batch. Always post to exactly the groups in `targets` — never hardcode a group JID yourself. If `targets` is empty, skip the group announcement but still act on the calendar.

Step 2. If status is "disabled" or "no_new_emails" or "auth_failed" or emails list is empty: reply with the literal token NO_REPLY.

Step 3. Classify the single email in `emails`. Apply these tests in order — the FIRST match wins. Do not fall through once you hit a match.

  Test A — WAITLIST PROMOTION (waitlist → confirmed booking):
    Body contains "added from the waitlist to" (case-insensitive)
    → classify as `waitlist_promotion`. This must be tested BEFORE the generic booking test because a promotion email is also a booking, but it additionally requires deleting the prior waitlist calendar entry.

  Test B — BOOKING (fresh reservation, not a promotion):
    Body contains ANY of these exact substrings (case-insensitive):
      - "Your Reservation is Confirmed"
      - "Congrats on booking"
    → classify as `booking`. Do NOT reclassify as `waitlist` just because the word "waitlist" appears elsewhere in the body.

  Test C — CANCELLATION:
    Subject or body contains "cancelled" or "cancellation"
    (but not preceded by "Late Cancel Fees" — that's boilerplate)
    → classify as `cancellation`.

  Test D — WAITLIST (join only):
    Body contains ANY of:
      - "You are now on the waitlist"
      - "You've been added to the waitlist"
      - "You have been added to the waitlist"  (note: NOT "added from the waitlist to <class>")
    → classify as `waitlist`.

  Otherwise: `noise` (account resets, password resets, purchase confirmations, welcome emails, guest pass invites, marketing).

Step 4. Act per classification. Extract in every non-noise case: class_name (e.g. "RIDE", "YOGA RESTORE", "BARRE"), date (as YYYY-MM-DD), time (as HH:MM 24-hour). Reject and reply NO_REPLY if the class time is already past — do not send messages or touch the calendar for past classes.

  Naming convention for calendar entries (fixed, do not vary — deletes rely on it):
    - Confirmed booking title: `🏋️ Club Studio: <CLASS_NAME>`
    - Waitlist join title:     `⏳ Club Studio Waitlist: <CLASS_NAME>`
    - Duration: 60 minutes (Club Studio emails do not include duration; 60 is the default)

  For a booking:
    a. Compose message: "🏋️ Harsh is going to <class_name> — <Day> <Mon> <D>, <h>:<mm> <AM/PM>"
       Example: "🏋️ Harsh is going to RIDE — Tue Jul 8, 9:30 AM"
    b. Send to every group in `targets` via bash, one command per target:
       `openclaw message send --channel whatsapp --target <target.jid> --message "<message>"`
    c. Create the calendar entry:
       Call `add_calendar_event` with title=`🏋️ Club Studio: <class_name>`, date=<YYYY-MM-DD>, time=<HH:MM>, duration=60.

  For a waitlist_promotion (waitlist → confirmed):
    a. Compose message: "🏋️ Harsh is going to <class_name> (off the waitlist) — <Day> <Mon> <D>, <h>:<mm> <AM/PM>"
    b. Send to every group in `targets` (same pattern as booking).
    c. Delete the prior waitlist calendar entry (silent if it doesn't exist — do not DM the owner, the waitlist join email may have been missed):
       Call `delete_calendar_event` with title=`Club Studio Waitlist: <class_name>`, date=<YYYY-MM-DD>.
       Ignore the result — a "not found" here is expected when the join email was missed and is not an error.
    d. Create the confirmed calendar entry:
       Call `add_calendar_event` with title=`🏋️ Club Studio: <class_name>`, date=<YYYY-MM-DD>, time=<HH:MM>, duration=60.

  For a cancellation:
    a. Compose: "❌ Harsh cancelled <class_name> — <Day> <Mon> <D>, <h>:<mm> <AM/PM>"
    b. Send to every group in `targets` (same pattern as booking).
    c. Delete the calendar entry (silent if it doesn't exist — the booking/waitlist email may have been missed):
       Call `delete_calendar_event` with title=`Club Studio: <class_name>`, date=<YYYY-MM-DD>.
       This search matches both `🏋️ Club Studio: <class_name>` and `⏳ Club Studio Waitlist: <class_name>` on that date.
       Ignore the result — a "not found" here is not an error.

  For a waitlist:
    a. Compose message: "⏳ Harsh is waitlisted for <class_name> — <Day> <Mon> <D>, <h>:<mm> <AM/PM>"
       Example: "⏳ Harsh is waitlisted for YOGA RESTORE — Tue Jul 7, 4:00 PM"
    b. Send to every group in `targets` (same pattern as booking).
    c. Create the waitlist calendar entry:
       Call `add_calendar_event` with title=`⏳ Club Studio Waitlist: <class_name>`, date=<YYYY-MM-DD>, time=<HH:MM>, duration=60.

  For noise:
    Do nothing. Do not post to any group. Do not DM the owner. Do not touch the calendar. Noise notifications are silently discarded — the fetch dedup ensures they won't be seen again.

Step 5. If you classified the email as noise (nothing to announce), reply NO_REPLY.

Step 6. If anything went wrong (unclear classification, missing date/time, etc.): reply with a short diagnostic: "⚠️ Club Studio watcher: <what went wrong>". This is a normal agent reply, not a bash message send — it routes to the owner DM automatically via the cron job's --to flag. Do not post diagnostics to any group. Then nothing further is needed; the diagnostic reply itself ends the turn.

FAMILY GROUP DELIVERY RULES: Every group in `targets` receives ONLY polished booking/cancellation announcements. Never post errors, chain-of-thought, or diagnostic text there. On any uncertainty or error, reply with the diagnostic (Step 6, routes to owner via --to) and nothing else — never post it to a group. On empty case, reply NO_REPLY.
END PROMPT
```

## WhatsApp routing (config-driven, not hardcoded)

This skill is meant to be cloned by other families with zero code changes
(CLAUDE.md principle 5) — the prompt above never hardcodes a phone number or
group JID. Routing comes entirely from `config.json`:

- **Owner DM** — `app.owner_phone`. Used for the cron job's `--to` flag at
  registration and for the agent's own replies/diagnostics.
- **Group announcements** — `whatsapp.groups[]` (each `{id, name}`). Read at
  runtime via `ClubStudioWatcher.notify_targets()` and returned as `targets`
  from `fetch_club_studio_emails`. Add, remove, or reorder groups there —
  the prompt adapts automatically, no edit needed here.

If you rename or add a WhatsApp group, update `config.json` only. The prompt
text above never needs to change for a routing update — only re-register
with `openclaw cron edit` if you change the *behavior* (steps 1-6), not the
routing.

## Enablement checklist

1. Copy `config.example.json` to `config.json` and fill in `app.owner_phone`
   and `whatsapp.groups[]` (at minimum a family group; add a Club Studio
   group if you want a separate channel for it)
2. Register the cron via `openclaw cron add ...` (command above)
3. Flip `club_studio.enabled: true` in `config.json`
4. Confirm the next 15-min poll runs cleanly:
   - `~/.openclaw/logs/gateway.log` shows the cron fire
   - No error DM to owner if nothing new arrived
   - Check `household/club_studio_processed.json` grows after real emails arrive
