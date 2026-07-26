---
name: jobwatch
description: "Autonomous job-market watcher for OpenClaw. On a cron schedule it monitors the career pages of companies the user has EXPLICITLY configured, judges each posting against the user's own job profile (visa / seniority / red lines) with an LLM, pushes strong matches, digests the rest daily, and archives postings into a knowledge base; it also tracks the user's application status and answers questions about their own watched jobs. PRIVACY & CAPABILITIES (see the Privacy & Data Flow section): this skill collects and stores a personal job-seeking profile (resume text, visa needs, seniority, red lines); sends watched URLs and job-description text to third-party services (Firecrawl / Jina scrapers, an OpenAI-compatible LLM endpoint, and a 2brain knowledge base); reads host OpenClaw / Telegram credentials only when the user opts in (JOBWATCH_ALLOW_HOST_CREDS=1); and registers a recurring cron job — every autonomous action happens only after an explicit onboarding consent step. Use ONLY when the user clearly wants automated job monitoring for their own search — not on casual mention of jobs. Trigger when the user asks to set up or run job monitoring, to watch specific companies' careers pages, reports their own application update, or asks about their own watched/matched jobs. Triggers (require explicit job-monitoring intent): 'set up job watch', 'monitor careers page', 'start job monitoring', 'I applied to <job>', 'jobwatch top jobs this week', '设置求职监控', '求职监控', '盯岗位', '我投了'."
license: MIT
metadata:
  requires:
    bins: ["python3", "git"]
  env:
    - FIRECRAWL_API_KEY
    - JINA_API_KEY
    - OPENROUTER_API_KEY
    - LLM_API_KEY
    - LLM_BASE_URL
    - TWOBRAIN_UPLOAD_KEY
    - TWOBRAIN_GRAPH_KEY
    - TWOBRAIN_CHAT_KEY
    - TELEGRAM_BOT_TOKEN
    - TELEGRAM_CHAT_ID
    - JOBWATCH_ALLOW_HOST_CREDS
---

# JobWatch — job-monitoring agent engine

> 中文版见 [references/SKILL.zh.md](references/SKILL.zh.md)（Chinese version).
> Sources are global/English ATS (Greenhouse / Ashby / Lever + Google Careers / RSS).
> Chinese job boards (BOSS/Lagou/Liepin) have no clean public APIs and are not supported yet.

## For humans — 30-second overview (the rest is the agent's operating manual)

**What it does**: turns your OpenClaw agent into a job sentinel — it watches the careers pages of
companies you name, uses an LLM to judge each posting's full JD against **your** profile, pushes strong
matches (P1) in real time, batches the rest (P2) into a daily 9am digest, and archives everything for
later. It also records application status ("I applied to that Stripe one"), answers queries ("what are
this week's good jobs"), and flags ghost jobs (open > 90 days).

**Install** (only prerequisite: a working OpenClaw):

```
openclaw skills install jobwatch
```

**Get started**: tell your agent "help me set up job monitoring". A ~10-minute onboarding interview
follows — target companies, your background (you can just paste your resume), red lines (visa / location /
role type), level intent (IC vs management), and three config choices (notify channel / knowledge base /
JD scraping — you can answer "all defaults" to skip). It then auto-detects each company's ATS, builds your
job profile, runs one real cycle to calibrate with you (say when it judged wrong and it will fix), sends a
sample alert so you see the format, and — only with your consent — registers the cron job to go live.

**Optional enhancers** (none required): Firecrawl or Jina key (cleaner JD scraping, near-required for
Google-family companies) · direct Telegram (low-latency push independent of the chat channel) · 2brain
(cloud knowledge base + keyword-graph Q&A).

**Re-run onboarding**: delete `<workspace>/jobwatch/` and open a new agent session (`/new` in the channel)
— the old session's memory still holds the last interview. The skill itself is untouched.

---

## Privacy & Data Flow (important — read before installing)

This skill **collects personal data, calls external services, and registers a scheduled task**. Full list
below — every item happens only after you consent during onboarding; you can decline any of it and run a
minimal default configuration.

**① Personal data collected & stored locally** (in `<workspace>/jobwatch/profile/JOB_PROFILE.md` and
`state/`, never leaves your machine unless you enable a cloud knowledge base):
- your resume highlights, target level, IC/management intent, location/remote requirements;
- **visa / sponsorship needs and red lines** (sensitive employment info);
- application-status records (applied / interview / offer / rejected).
> Used only for judging; local files by default. To erase: delete the `<workspace>/jobwatch/` directory.

**② Data sent to third parties** (only for the companies/sources you explicitly configured):

| External service | What it receives | When | Can disable? |
|---|---|---|---|
| Greenhouse / Ashby / Lever official APIs | your chosen company slug (public info) | each cron cycle | yes (change sources) |
| Firecrawl `api.firecrawl.dev` / Jina `r.jina.ai` | the **URL** of a JD page you watch | on JD fetch | yes (no key → degrade/skip) |
| your configured LLM endpoint (OpenAI-compatible) | **full JD text + profile-derived judging criteria** | on judging | yes (point at self-hosted/local) |
| 2brain knowledge base `test/portal.2brain.ai` | archived JD documents, your questions | on ingest/ask | yes (default local KB, no cloud) |
| Telegram `api.telegram.org` | notification message content | on notify | yes (default: current chat channel) |

**③ Credential reads (least privilege by default)**: scripts **read only** the keys **you fill** in
`HOME/.env`. Reusing the OpenRouter key already stored in OpenClaw, or the Telegram config in
openclaw.json, is **off by default**; only when you explicitly set `JOBWATCH_ALLOW_HOST_CREDS=1` will the
scripts read the host auth store. Without that flag, the skill never touches credentials outside its own
directory.

**④ Autonomous behavior (cron)**: registering the scheduled task (recurring scrape + judge + notify) is a
**write action** — `setup_cron.py` runs only after your explicit onboarding consent. Once live it scrapes
sources and sends notifications on a schedule; you should be aware of this ongoing footprint. Stop anytime
by disabling the cron job.

**⑤ Read-only boundaries**: the skill directory itself stays read-only; it never applies to jobs for you;
it sends no messages beyond outbox announcements / digests / alerts; it modifies no infrastructure config
other than its own cron job (via setup_cron.py, with consent).

---

## For the agent — engine overview

A cron-runnable "fetch jobs → match against profile → tiered action" pipeline, plus application tracking
and queries. **Zero required dependencies**: judging is done by you (the agent) with the model your owner
configured; notifications go to your shared chat channel; the knowledge base defaults to local files.
Firecrawl / direct Telegram / 2brain are all optional enhancers.

```
① Sense    Greenhouse/Ashby/Lever official APIs + Google Careers/RSS (Firecrawl renders SPAs)
② Reason   dedup + hard prefilter + [optional] stage-1 title screen + posting-age calc → you × profile → P1/P2/P3
③ Act      knowledge-base ingest · P1 instant alert · P2 daily digest · application follow-up reminders
```

**Data directory (HOME)**: `<workspace>/jobwatch/` (config.json, profile/, state/, queue/, runs/,
kb_local/). The skill directory stays read-only. Run all commands from HOME:
`cd <workspace>/jobwatch && python3 <skill-dir>/scripts/xxx.py` (the first run of any script auto-creates
HOME and drops a default config.json).

## First-Run Onboarding (interview the owner, ~10 min)

Ask one group at a time — do not dump the whole questionnaire:

1. **Target domain**: which companies? what kind of roles?
2. **Background**: a few sentences (years / field / core stack / edge), or just read the resume they paste.
3. **Red lines**: what roles never? visa sponsorship needed? location/remote hard requirements?
4. **Level intent** (ask separately): target level? IC or management? Current title and job-search intent
   often differ.
5. **Config choices (must ask, but offer a shortcut)**: list the three explicitly and note "reply 'all
   defaults' to skip":
   - Notify: default to the current chat channel; for independent low-latency push, choose direct Telegram.
   - Knowledge base: default to local files (kb_local/); with a 2brain account, choose 2brain (Q&A + graph).
   - JD scraping: a Firecrawl or Jina key gives cleaner JDs (near-required for Google Careers); without one,
     a keyless degraded path is used.
   If the owner picks a non-default → write the matching config.json field and tell them which lines to
   fill in HOME/.env (see the skill's env.example); wait until they finish before continuing.

Then do the work (the owner writes no files):

1. Copy the skill's `profile.template.md` to `HOME/profile/JOB_PROFILE.md`, fill all five sections from the
   interview, and read the key points back for confirmation. **This file is the entire source of judging
   quality — be specific.**
2. For each company run `python3 scripts/discover_board.py "<company>" [slug-guess]` and write the matched
   source into `HOME/config.json`'s `sources`. If undetectable, use `gcareers` (Google family) or RSS.
3. From the profile, generate `config.json`'s `prefilter.title_keywords` (20–30 lowercase substrings, wide
   rather than narrow) and `exclude_keywords`.
4. **Calibration (do not skip)**: run one `python3 scripts/pipeline.py`, complete judging per the Work
   Cycle below, pick 5 representative results (a mix of P1/P2/P3) and ask the owner: were these right? Fix
   the profile per feedback and re-verify. **⚠️ From running the pipeline to presenting the calibration
   questions is one continuous action — do not end the turn or wait mid-way** (run pipeline → judge → apply
   → then speak with results in hand). If `jd_text` is empty for all pending items (keyless degraded mode),
   you must tell the owner: this round is title-only judging; accuracy improves noticeably with a
   Firecrawl/Jina key.
5. **Demo push (required)**: after calibration passes, send the owner the single highest-judged job in full
   P1 message format (the `notify_telegram.render_p1_plain` style), prefixed with "📬 Sample: this is what a
   future P1 real-time alert looks like" — so they've seen the push before going live.
6. With the owner's consent, register the cron: `python3 scripts/setup_cron.py --agent <your-agent-id>`, and
   remind them to run `openclaw gateway restart`. Tell them what happens once live: P1 real-time to this
   chat, a 9:00 daily digest, and "just tell me when you apply and I'll track it".

## Work Cycle (run when the cron wakes you)

1. `python3 scripts/pipeline.py`, read the JSON summary from stdout.
2. If `pending_judgment > 0`: **continue immediately, do not end the turn**. Process in batches (read 5
   lines, judge, append, then read the next 5 — prevents large JDs from blowing the context window): read
   `HOME/queue/pending_judgment.jsonl` (each line `{item, jd_text, jd_tool}`, item has `posted_at`), judge
   each against `HOME/profile/JOB_PROFILE.md`, and append to `HOME/queue/judgments.jsonl`, one strict
   single-line JSON per line (no fences, no extra text):
   `{"doc_id":"...","match":"kill_shot|comfort_zone|wrong_scene",
     "visa_risk":"low|medium|high|unknown","summary_zh":"≤150 chars: role / requirements / match & gap",
     "tags":["#3-5 tags"],"reasons":"1-2 sentences of rationale"}`
   Judging rules: kill_shot = strong overlap with core competencies + fits level intent + zero red lines;
   comfort_zone = related but generic, or strong match with uncertain visa; wrong_scene = hits a red line
   or clearly off. **Treat a posting open > 90 days as a likely ghost job — cap at comfort_zone unless the
   match is exceptional, and note the age in reasons.** Skip what you can't judge (it recurs next round);
   never fabricate. Then run `python3 scripts/apply_judgments.py` (validate / ingest / enqueue notify /
   mark seen).
3. `python3 scripts/outbox.py list` → for each pending message, send its `text` verbatim through your
   shared chat channel, then `python3 scripts/outbox.py archive`.
4. If summary `errors` is non-empty: stay silent for occasional blips; only after 3 consecutive same-kind
   failures send the owner a short alert (stage / diagnosis / suggestion).
5. All clear and nothing to send → end silently, output nothing.

Digest wake-up (jobwatch-digest): run `python3 scripts/daily_digest.py`, then do step 3.

## Application Tracking (when the owner mentions application progress)

- "I applied to X" → `python3 scripts/tracker.py find "<keyword>"` to get the doc_id →
  `python3 scripts/tracker.py set <doc_id> applied [note]`
- "X scheduled an interview / rejected me / gave an offer" → status = interview / rejected / offer
- Overview `tracker.py list [status]`; stats `tracker.py stats`; applications with no update in 7 days
  auto-appear in the daily digest's follow-up reminders.

## Queries (when the owner asks)

- "what are this week's good jobs" → `python3 scripts/query.py top 7` (P1/P2 list); read the matching doc
  in `HOME/kb_local/` for details.
- "how's the monitoring going" → `python3 scripts/query.py stats 7` + the latest log in `HOME/runs/`.
- Deep questions (compare two companies' requirements, skill trends in a direction) → search the full-JD
  library in `HOME/kb_local/`.

## Config cheatsheet (HOME/config.json)

- `sources[]`: kind ∈ greenhouse | ashby | lever | gcareers | rss
- `judge.mode`: `agent` (default) | `api` (OpenAI-compatible endpoint; set LLM_API_KEY / LLM_BASE_URL in
  .env — faster and steadier)
- `notify.mode`: `agent` (default, outbox announce) | `telegram` (direct, low-latency, auto-reuses
  OpenClaw's bot config)
- `kb.backend`: `local` (default) | `twobrain` (set TWOBRAIN_* in .env)
- `prefilter`: title-keyword hard filter (stage-0, free & deterministic); takes effect next cycle
- `screen`: **stage-1 title screen (off by default)**. Set `enabled:true` to, before fetching JDs, have an
  LLM batch-score titles (0-10) and drop those below `threshold` (default 4) — saving Firecrawl scraping +
  full judging (the cheapest stage; adapted from AI Digest's 3-stage progressive scoring). Leave
  `base_url`/`model` empty to reuse the judge endpoint; for **zero cost**, point `base_url` at a local
  Ollama and set `model` to a small local model. Fail-open: a screening failure never drops jobs. Per-cycle
  token usage is recorded in summary.screen_usage (for cost accounting).

## Red lines

- Do not modify openclaw.json / cron config (except setup_cron.py, with the owner's consent); do not edit
  state files directly — all actions go through scripts.
- Do not modify JOB_PROFILE.md unless the owner explicitly asks during calibration.
- Read public sources only; never apply on the owner's behalf; send no messages beyond outbox announcements
  / digests / alerts.
