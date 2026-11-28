# Templates

## Plan JSON (minimal)

```json
{
  "brand": "Brand name",
  "timezone": "Asia/Karachi",
  "start": "2026-12-07",
  "weeks": 4,
  "platforms": {
    "instagram": {"per_week": 3, "days": ["Mon", "Wed", "Sat"], "times": ["19:00"]},
    "linkedin": {"per_week": 2, "days": ["Tue", "Thu"], "times": ["10:00"]}
  },
  "pillars": {"Educate": 40, "Proof": 25, "Story": 20, "Offer": 15},
  "blackout": [],
  "events": [{"date": "2026-12-15", "name": "Product launch", "note": ""}],
  "items": []
}
```

Run `skeleton`, then fill `title`, `format`, `brief`, `cta`, `owner`, `status` for each item. Tip: start the plan on a Monday so weeks align with calendar weeks; the tool counts weeks from the start date.

## Item fields

`date` (YYYY-MM-DD), `time` (HH:MM, plan time zone), `platform`, `pillar`, `format` (carousel, reel, short, text, thread, video, story, live, poll), `title`, `brief` (one or two lines: point, proof, action), `cta`, `status`, `owner`, `notes` (asset links, approvals, caveats).

## Campaign timeline example (2-week launch)

| Day | Phase | Pieces |
|---|---|---|
| -7 | Tease | story hint, short video of the problem |
| -3 | Educate | carousel on the problem, LinkedIn story |
| -1 | Tease | countdown story (only a real date) |
| 0 | Announce | launch post on every channel, email, pinned post |
| +1 to +3 | Proof | demo clip, first results or testimonial (real, permitted), FAQ replies |
| +5 | Educate | how-to carousel and thread |
| +7 | Last call | deadline reminder (only if the deadline is real) |
| +9 | Follow-up | thank-you, results recap, lessons learned |

## Production schedule (per item)

| Step | Owner | Due | Done |
|---|---|---|---|
| Brief | | post date -10 | |
| Draft | | -7 | |
| Assets | | -4 | |
| Review | | -2 | |
| Scheduled | | -1 | |

## Weekly check (15 minutes)

1. Posted vs planned this week? Reason for each miss.
2. Buffer of approved posts: how many?
3. Items to shift (`shift` command) and why.
4. Any news or sensitivity that needs a pause?
5. One thing to try next week.

## Monthly review

| Question | Answer |
|---|---|
| Which pillar or format earned the most saves, shares, replies, clicks, leads? | |
| Which underperformed and why (topic, hook, time, format)? | |
| Did the cadence hold? What was the real production time? | |
| Which time slot test finished and what did it show (with sample sizes)? | |
| Decisions: repeat / stop / test next month | |

## Handing off to a scheduler

Export CSV (`calendar.csv`) and map the columns to the tool's import format; paste the final text from the content pack (`social-media-content`) and attach media. Check each scheduled post once in the tool's preview. Use ICS (`calendar.ics`) for team reminders in a calendar app: events are placed at the post time, in UTC, so each app shows them in the viewer's local time.
