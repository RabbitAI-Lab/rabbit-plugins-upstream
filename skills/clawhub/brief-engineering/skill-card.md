## Description:

Technical daily brief for engineers covering service health, deploys, alerts, DLQ/latency, workflows, migrations, and customer signals for engineering and on-call briefs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vmishra-atlassian](https://clawhub.ai/user/vmishra-atlassian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, on-call responders, engineering managers, and PMs use this skill to produce a daily engineering brief that prioritizes service health, deployments, alerts, incidents, work queues, and next steps under the invoking user's access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads work, calendar, service ownership, deployments, alerts, and allowlisted operational Slack results using delegated access.

Mitigation: Confirm the discovered service scope before use, keep scope memory per user, and stop any source that requires missing consent.

Risk: A copied or stale scope file can cause briefs to include services the user does not own.

Mitigation: Use the confirmed `memory/engineering-brief/scope.json` as the only service-name source, reconfirm expired scope, and delete copied scope memory before a teammate's first run.

Risk: The optional local operational relay publishes derived Splunk and SignalFx findings to a creator-private Confluence page.

Mitigation: Enable the relay only with user approval, keep raw logs and tokens local, require a fresh validity window, and ignore stale or malformed relay content.

Risk: Missing or broken connectors can make operational coverage look healthier than it is.

Mitigation: Run connector preflight, bound every call, and report exact coverage states such as checked, not registered, failed, stale, or runtime unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vmishra-atlassian/skills/brief-engineering)
- [README](README.md)
- [Signal catalogue](references/signal-catalog.md)
- [Operational connector authentication](references/connector-auth.md)
- [Local operational relay](references/local-operational-relay.md)
- [Team signal pack contract](references/signal-packs.md)
- [Persona presentation policy](references/personas.md)
- [Rolling this out to a team](references/team-adoption.md)
- [Sharing this with a teammate](references/install-for-teammates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown brief with ordered sections, evidence links, coverage rows, and inline shell command or configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs under the invoking user's delegated access; first run stores confirmed per-user service scope and may use optional team signal-pack or private relay configuration.]

## Skill Version(s):

1.0.5 (source: server evidence, SKILL.md frontmatter, README.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
