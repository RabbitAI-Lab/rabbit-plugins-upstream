# Scheduled Jobs — Fired, Skipped, Doubled, Or Silently Empty

**Before this pass**, read `## System Baseline` in `~/Clawic/data/analysis/memory.md` (or the file its `## Boxes` line names) for the recorded job inventory and each job's expected interval, `## Due` for cadences this skill owns, and the shared `~/Clawic/data/servers/servers.md` for the hosts those jobs run on — a job scheduled on a machine no inventory knows about is itself the finding. A job missing from a setup that used to have it is a finding; so is a job nobody remembers creating.

**Contents:** [Inventory First](#inventory-first) · [Schedule Expression Bugs](#schedule-expression-bugs) · [The DST Window](#the-dst-window) · [Thundering Herd](#thundering-herd) · [Overlap](#overlap) · [Silent Failure](#silent-failure) · [The Non-Interactive Environment](#the-non-interactive-environment) · [Output Growth](#output-growth) · [Retries](#retries) · [Cost Per Schedule](#cost-per-schedule) · [Unattended Authority](#unattended-authority) · [Sweep](#sweep) · [Write It Down](#write-it-down)

## Inventory First

For every automation — cron entries, systemd timers, launch agents, platform schedulers, webhook triggers, watch loops — record six fields in `## System Baseline` in `memory.md`: name, schedule, timezone, what it runs, where its output goes, and how you would know it failed. The sixth is the one that is usually empty, and it is the one that matters.

Jobs live in more places than anyone remembers: the user crontab, the system crontab and its drop-in directories, systemd timers, per-user launch agents, the agent platform's own scheduler, and CI schedules in repositories. A job inventory that covers one of those is why "it stopped running" investigations go in circles.

## Schedule Expression Bugs

| Expression | What people mean | What it does |
|---|---|---|
| `0 0 1 * 1` | First of the month, if it is a Monday | Runs on the 1st **and** every Monday — when both day-of-month and day-of-week are restricted, classic cron takes the **union**, not the intersection |
| `* * * * *` after an edit meant to be hourly | Hourly | Every minute; combined with a job that spawns an agent run, this is a runaway bill |
| `*/7 * * * *` | Every 7 minutes | Every 7 minutes *within each hour*, so the gap across the hour boundary is 4 minutes (56 → 0) |
| `0 0 * * 7` | Sunday | Sunday in implementations that accept 7; an error in those that only accept 0-6 |
| `@reboot` | On boot | Only if the scheduler runs at boot and the user session exists; on a laptop, effectively "sometimes" |
| `30 2 * * *` | Nightly at 02:30 | Skipped or doubled twice a year — see below |
| Second-precision fields | Standard | Only some schedulers accept 6 fields; the same string means different things in different runners |

Validation is cheap: parse the expression, print the next five fire times in the job's declared timezone, and show them to the user. Nobody reads a cron string correctly; everybody reads five dates correctly.

## The DST Window

A job scheduled between 01:00 and 03:00 local time, in a zone that shifts at 02:00, **does not run at all** on the spring-forward date and **runs twice** on the fall-back date. Every backup, report, and cleanup that anyone has ever scheduled at 02:00 hits this twice a year.

Fixes, in order of preference: express the schedule in UTC; or move it outside the window (00:30 and 03:30 are both safe in every zone that shifts at 02:00); or make the job idempotent so the double run is harmless. Idempotency alone does not fix the *skipped* run.

Check every job's schedule against the window as part of the sweep. It is a two-line check that prevents a whole class of "the backup from March 30th is missing".

## Thundering Herd

Jobs written by hand cluster at minute 0 and at midnight. When five agent runs start at 00:00 they compete for CPU, rate limit each other against the same provider, and lock the same files.

Stagger deterministically so the assignment is stable across re-installs: `minute = hash(job_name) mod 60`, or simply spread by hand across the hour and write the spread into the job inventory in `## System Baseline`. Finding threshold: three or more jobs sharing a start minute, or any two that touch the same files or the same provider.

## Overlap

A job that takes longer than its interval will eventually run concurrently with itself: two writers on the same file, doubled API calls, and a queue that never drains.

Rule with a number: if p95 runtime exceeds **half** the interval, either raise the interval or add a lock. A lock is a file whose existence blocks a second start, with the pid and start time inside so a stale lock can be identified, and a max age after which it is broken and reported. A lock with no max age converts a single crash into a permanently dead job — that is its own finding, and it is common.

## Silent Failure

The default failure mode of a scheduled job is silence: nothing runs, nobody is told. Alerting on failure is not enough, because a job that never starts produces no failure to alert on.

- **Dead-man's switch**: the job reports success on each run to something that alerts when the report is *absent*. Threshold: alert when the last success is older than `2 × interval + p95 runtime`; tighter than that produces noise from ordinary jitter.
- **Assert on the artifact, not on the exit code.** A job can exit 0 having done nothing: empty input, wrong working directory, a silent auth failure, a filter that matched zero rows. The check is "does today's file/row/timestamp exist and is it newer than the last interval", which is also what makes the audit able to verify it without running the job.
- **Detection during the audit**: for each job, compare the last success timestamp to the interval. Anything above `2 × interval` is a WARNING; a job with no recorded last-success at all is a WARNING whose action is instrumentation, not investigation.

## The Non-Interactive Environment

The top cause of "it works when I run it by hand". A scheduled process gets a different world:

| Difference | Symptom | Fix |
|---|---|---|
| Minimal `PATH` | "command not found" for something clearly installed | Absolute paths, or set `PATH` in the job definition |
| No shell profile sourced | Missing environment variables, missing version-manager shims | Export explicitly in the job; never rely on the interactive profile |
| Working directory is not the project | Relative paths resolve elsewhere; files appear in `$HOME` | `cd` as the first action, absolute paths everywhere else |
| No TTY | Anything that prompts blocks forever | Non-interactive flags; treat a prompt as a bug |
| Different user | Permission denied on files the user owns; a different credential store | Run as the owning user, or make the credential reachable to the job's user (`secrets.md`) |
| No unlocked keychain on a locked machine | Auth failures only overnight | Move the credential to a store that survives lock, or reschedule |
| Locale and timezone differ | Dates parsed or formatted differently, off-by-one days | Set both explicitly in the job |

The diagnostic that settles it in one shot: run the job through the scheduler's own environment (an `env -i` invocation with only the variables the scheduler sets) rather than from your shell.

## Output Growth

Job output is append-forever by default. Two findings: no redirection at all (output is lost, so failures are invisible), and redirection with no rotation (the disk fills). Both are WARNING; the action is a rotation rule with a size and a count, plus keeping stderr where a human will see it. Include job output directories in the retention pass (`workspace.md`).

## Retries

A retry without backoff turns one provider blip into a self-inflicted rate limit. Standard shape:

```
sleep = min(cap, base × 2^attempt) × (0.5 + random()/2)
```

with `base` 1s, `cap` 60s for interactive work and 300s for background jobs, and a hard attempt limit — 5 is a sane default. Jitter is the half that matters when several jobs retry against the same provider at once. Retrying a 4xx other than 408/429 is a bug: the request was wrong and will stay wrong.

## Cost Per Schedule

Frequency multiplies everything downstream. `runs_per_day = 1440 / interval_minutes`, so a 5-minute job is 288 runs a day, 8,640 a month. If each run costs tokens, that multiplier is the whole cost story: an agent run costing $0.02 on a 5-minute schedule is ~$173/month for a job that is idle most of the time.

Two cheap fixes before touching the interval: make the job exit early when there is nothing to do (a cheap local check before any model call), and switch from polling to an event or webhook where the source offers one. Write the estimate into the job inventory in `## System Baseline` so the next audit can compare (`cost.md`).

## Unattended Authority

Anything that runs without a human present must sit at rung 2 or below of the scope ladder in `permissions.md`. A scheduled job with broad grants is the highest-value target in the whole setup: it runs on a timer, its output is rarely read, and its input often comes from somewhere someone else can write.

## Sweep

| Check | Passing looks like |
|---|---|
| Every job inventoried with all six fields | Including "how would I know it failed" |
| Next five fire times shown per job | They match the intent |
| No job in the 01:00-03:00 local DST window | Or scheduled in UTC |
| No start-minute cluster | Max two jobs per minute, none sharing a target |
| p95 runtime below half the interval, or a lock with a max age | No self-overlap possible |
| Last success within `2 × interval` for every job | Plus a dead-man's switch on anything that matters |
| Output redirected and rotated | Size and count set |
| Retries bounded, with jitter | Attempt limit and cap present |
| Cost per schedule estimated | Runs/day × per-run cost recorded |
| Unattended jobs at rung ≤2 | Narrow grants, named hosts |

## Write It Down

Same turn as the pass:

- The job inventory with its six fields, plus runs/day and estimated monthly cost → `## System Baseline` in `memory.md` (splits to `baseline.md` past the threshold).
- Broken schedules, missing dead-man's switches, overlap risk, unrotated output → `## Open Findings`, one per job.
- Cadences this audit owns or the user accepts → `## Due` rows in `memory.md`, each with its last run and next due date.
- A job's recovery procedure that worked → `~/Clawic/data/analysis/artifacts/job-<name>-runbook.md`, plus its `## Boxes` line.
- Any host the jobs run on → the shared `~/Clawic/data/servers/servers.md` (`memory-template.md` has the format and the identity rule).
