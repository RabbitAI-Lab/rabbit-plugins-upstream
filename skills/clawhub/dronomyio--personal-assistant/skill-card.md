## Description:

Helps users set up a personal market-and-research assistant with watchlist briefs, reading summaries, site monitoring, and an optional private dashboard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dronomyio](https://clawhub.ai/user/dronomyio)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals use this skill to configure personal market briefs, organize reading, monitor their sites, and review results in a private dashboard or daily digest.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Opt-in background jobs and local storage may continue running and retaining personal data.

Mitigation: Review cron entries, systemd units, environment variables, output directories, and the Memori database location before enabling them.

Risk: The YouTube transcript fetcher uses a workaround for platform bot checks.

Mitigation: Review the fetcher before use, or remove or replace it if this scraping workflow is not acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dronomyio/skills/personal-assistant)
- [Architecture](references/architecture.md)
- [Dashboard pattern](references/dashboard-pattern.md)
- [Scheduling patterns](references/scheduling-patterns.md)
- [Temporal setup](references/temporal-setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON]

**Output Format:** [Markdown instructions and briefs, with configuration examples and JSON status files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional scheduled updates and alerts on significant changes]

## Skill Version(s):

1.1.2 (source: ClawHub release metadata and skill changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
