## Description:

Personalized daily news briefings/digests and real-time breaking-news alerts from newsflash.sh — a deduped news event graph where every event carries a corroboration count and confidence score. Use when the user asks about news, headlines, markets, crypto, what's happening, wants a daily digest or recurring briefing, or wants to be alerted when something breaks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zatmonkey](https://clawhub.ai/user/zatmonkey)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to produce personalized daily news briefings, answer ad-hoc news questions, and deliver breaking-news alerts using deduplicated events with corroboration and confidence signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The hosted news service receives selected interests and categories for briefings or alerts.

Mitigation: Install only when this data sharing is acceptable, and avoid putting sensitive personal or confidential topics into interests.

Risk: Recurring briefings and live alerts can run repeatedly or continue in the background.

Mitigation: Review briefing time, quiet hours, minimum-source thresholds, and alert settings before enabling recurring or streaming behavior.

Risk: The skill depends on external commands and network calls through npx, curl, and newsflash.sh.

Mitigation: Treat npx/newsflash.sh as external dependencies and review commands before execution in controlled environments.

Risk: Single-source news events may be unconfirmed or misleading if presented as established facts.

Mitigation: Keep single-source events out of the main briefing, label them as one-outlet reports, or place them in a watchlist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zatmonkey/skills/newsflash)
- [Publisher profile](https://clawhub.ai/user/zatmonkey)
- [Newsflash homepage](https://newsflash.sh)
- [Newsflash events API](https://newsflash.sh/api/events?limit=1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown briefings and alerts with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update a workspace newsflash.json preferences file and may emit source links, outlet counts, and alert text.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
