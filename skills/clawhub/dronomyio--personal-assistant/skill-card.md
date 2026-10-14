## Description:

Helps build a private personal briefing system for watchlist movers, news and video ideas, reading notes, and website health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dronomyio](https://clawhub.ai/user/dronomyio)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals use this skill to configure scheduled market and news briefs, organize reading notes, check their own websites, and view results in a private dashboard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduled jobs may run or notify more often than intended.

Mitigation: Review cron jobs and notification thresholds before enabling them.

Risk: Personal briefs, reading notes, or transcripts may expose private or licensed content if published.

Mitigation: Keep outputs in private paths and do not publicly sync transcripts or full-text extracts.

Risk: Site checks or video transcript fetching may conflict with site ownership or third-party content terms.

Mitigation: Check only your own sites; disable the transcript fetcher if its Android-client workaround or content terms are unacceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dronomyio/skills/personal-assistant)
- [Architecture](references/architecture.md)
- [Scheduling patterns](references/scheduling-patterns.md)
- [Dashboard pattern](references/dashboard-pattern.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance, local JSON reports, and reading notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scheduled jobs write dated local files and current-result pointers; the dashboard and spoken audio require separate setup.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
