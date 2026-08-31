## Description:

BigFocus tracks product prices, public-figure updates, industry news, and custom metrics, then reports changes on user-defined schedules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kobenfang](https://clawhub.ai/user/kobenfang)

### License/Terms of Use:

MIT-0

## Use Case:

External users use BigFocus to maintain personal watchlists for prices, people, industries, and metrics, with scheduled checks and change-only notifications. It is intended for user-confirmed tracking items rather than broad collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent watchlists and raw history may reveal private interests if users track sensitive topics.

Mitigation: Use the skill only for intended tracking items, avoid sensitive personal targets, and review stored tracker and history files before enabling scheduled scans.

Risk: Scheduled URL fetching can reach unintended public domains when arbitrary URLs are tracked.

Mitigation: Restrict tracked URLs to validated public product or API domains before enabling the hourly cron job.

Risk: Web-search based updates for people, industries, or custom metrics may surface incomplete or unverified information.

Mitigation: Treat notifications as alerts and review source results before making decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kobenfang/skills/bigfocus)
- [cron-templates.json](references/cron-templates.json)
- [cron-install-shell.sh](references/cron-install-shell.sh)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON responses with optional shell commands for cron setup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains local tracker and raw-history files; scheduled scans report only detected changes.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
