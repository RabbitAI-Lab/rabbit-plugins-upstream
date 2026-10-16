## Description:

Builds a personal market and research briefing system with watchlist updates, transcript collection, reading notes, site checks, and an optional private dashboard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dronomyio](https://clawhub.ai/user/dronomyio)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and their agents use this skill to assemble private market briefs, research notes, transcript-based ideas, and site-health updates from their own watchlists, sites, and reading inboxes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An always-on watchdog installs persistent background services.

Mitigation: Review the service units, run the worker under your normal user account, and define disable and removal steps before enabling them.

Risk: The watchdog can execute configured local scripts without tight boundaries.

Mitigation: Point executable environment variables only to trusted, reviewed scripts.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dronomyio/skills/personal-assistant)
- [Architecture](references/architecture.md)
- [Scheduling patterns](references/scheduling-patterns.md)
- [Dashboard pattern](references/dashboard-pattern.md)
- [Temporal watchdog setup](references/temporal-setup.md)
- [Temporal CLI releases](https://github.com/temporalio/cli/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown briefs and notes, timestamped JSON reports and status files, and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local outputs use latest.json pointers; notifications are reserved for significant events.]

## Skill Version(s):

1.1.1 (source: server release metadata and skill changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
