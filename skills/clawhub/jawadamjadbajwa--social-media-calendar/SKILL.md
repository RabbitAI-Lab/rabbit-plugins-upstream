---
name: social-media-calendar
description: Plan and manage a social media content calendar across platforms (YouTube, Instagram, LinkedIn, X, Facebook, TikTok, Threads and others) covering cadence, content pillar balance, campaign and launch timelines, events and blackout dates, production and approval schedule, time-zone aware posting times, rescheduling, and exports to CSV, ICS and Markdown. Use this skill whenever the user wants a content calendar, posting schedule, weekly or monthly plan, campaign timeline, a posting-frequency or best-time plan, to reschedule or audit an existing calendar, or says "make a calendar", "schedule plan", "content plan for this month", "when should I post", even if they only name one platform.
---

# Social media calendar

Turns a strategy and a team's real capacity into a dated plan that can be produced, approved and published on time, with checks that catch gaps, clashes and drift. Replies follow the user's language preference.

## Principles

- Capacity first. A calendar the team cannot produce fails by week two. Ask who creates, how many hours a week, and which formats are slow (video, design).
- Cadence is a hypothesis. Days, times and frequency in a new calendar are assumptions; label them as such and replace them with the user's own analytics (use the `analytics` skill if available). Do not quote "best times to post" statistics as facts.
- Balance by purpose: pillars from the content strategy (see `content-strategy`) set the mix; the tool checks the mix against the targets.
- Quality over volume: fewer well-made posts beat many thin ones. Recommend the lowest cadence that can be kept for 8 weeks.
- Dates that move (religious observances on lunar calendars, school terms, sales seasons) must come from a current source or from the user; the tool has no built-in holiday list.

## Workflow

1. **Intake.** Brand and goals, platforms, audience time zone, team and weekly hours, content already available, pillars (or ask for the strategy), key dates (launches, events, holidays, sales), blackout dates, approval steps, tools used for scheduling, start date and length. Ask only for what is missing; state assumptions.
2. **Capacity and cadence.** Propose a frequency per platform from capacity (see `references/planning-framework.md`), with a minimum viable version and a stretch version. Say plainly when the requested volume is unrealistic for the team.
3. **Pillars and formats.** Set the target mix (for example Educate 40, Proof 20, Story 20, Offer 10, Community 10) and the format mix per platform.
4. **Build the plan JSON.** Format at the top of `scripts/calendar_tools.py`. Run `python scripts/calendar_tools.py skeleton plan.json` to fill the slots, then add titles, formats and briefs (use `social-media-content` for the posts).
5. **Key dates and campaigns.** Add `events` and `blackout`; for launches or campaigns lay out the phases (teaser, launch, proof, last call, follow-up) with the templates in `references/templates.md`.
6. **Production schedule.** Work back from the post date: brief, draft, asset, review, approved, scheduled (offsets in the templates); batch similar work (record scripts together, design carousels together).
7. **Check.** `python scripts/calendar_tools.py check plan.json` flags cadence mismatches, pillar drift, gaps over 5 days, duplicate titles, blackout hits, bad dates, overdue statuses and missing fields. Fix FAILs; explain WARNs that are intentional.
8. **Export and hand over.** `python scripts/calendar_tools.py export plan.json --out calendar/` writes `calendar.csv` (spreadsheet or scheduler import), `calendar.ics` (any calendar app, UTC times) and `calendar.md` (readable). If the session offers a sheets or docs artifact type, put the calendar there. Scheduling or posting through a connected tool happens only if the user asks, and only after approval of each post.
9. **Review loop.** Weekly: status check, move slipped items (`shift`). Monthly: compare plan to results with `analytics`, then change cadence, pillars or times by evidence; note what changed.

## Commands

```bash
python scripts/calendar_tools.py skeleton PLAN.json [--out PLAN.json]
python scripts/calendar_tools.py check PLAN.json [--json report.json]
python scripts/calendar_tools.py export PLAN.json --out DIR
python scripts/calendar_tools.py shift PLAN.json --days N [--from YYYY-MM-DD] [--platform NAME]
```

Standard library only (Python 3.9+; time zones use the system database, on Windows `pip install tzdata` may be needed).

## Rules

- Never promise reach or growth from a schedule. Say what the plan controls (consistency, balance, preparation) and what it does not.
- Do not schedule or publish anything without the user's approval; do not reuse credentials from files.
- Flag sensitive dates (national mourning days, tragedies, elections, religious observances) for human review and avoid tone-deaf promotions; check current news before large campaigns.
- Respect platform and legal rules for contests, ads and disclosures (see `social-media-content`'s compliance notes).
- Keep a buffer of 3 to 5 approved posts so a sick day does not break the schedule.

## References

- `references/planning-framework.md`: capacity and cadence, pillar mix, time slots, campaign phases, batching, approvals, review cadence.
- `references/templates.md`: plan JSON examples, campaign timeline, production offsets, weekly and monthly review templates.
