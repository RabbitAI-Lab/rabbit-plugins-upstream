## Description:

Technical daily brief for engineers: service health, deploys, alerts, DLQ/latency, workflows, migrations, customer signals. Use for engineering/on-call briefs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vmishra-atlassian](https://clawhub.ai/user/vmishra-atlassian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, on-call engineers, engineering managers, and PMs use this skill to generate a daily operational brief for owned services, including deploy state, alerts, reliability signals, migrations, customer signals, and the next actions to take.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads sensitive workplace context such as tickets, pull requests, calendar events, direct notifications, allowlisted Slack evidence, Confluence content, and operational telemetry using the invoking user's delegated access.

Mitigation: Install only for users who accept that access model, keep runs per-user, avoid shared service accounts, and do not copy another user's memory folder.

Risk: Tokens or credentials could be exposed if users paste secrets into prompts, memory, dashboards, logs, or published skill files.

Mitigation: Do not put tokens in prompts or memory; use delegated connectors, approved remote tools, or local secret storage for the optional operational relay.

Risk: Missing, failed, or stale connectors can make a brief appear more complete than it is.

Mitigation: Use the connector preflight and coverage rows, distinguish not registered, failed, runtime unavailable, and stale states, and avoid inferring health from missing data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vmishra-atlassian/skills/brief-engineering)
- [README](README.md)
- [Operational connector authentication](references/connector-auth.md)
- [Sharing this with a teammate](references/install-for-teammates.md)
- [Local operational relay](references/local-operational-relay.md)
- [Persona presentation policy](references/personas.md)
- [Signal catalogue](references/signal-catalog.md)
- [Team signal pack contract](references/signal-packs.md)
- [Rolling this out to a team](references/team-adoption.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown brief with evidence links, coverage rows, prioritized findings, action plans, and inline shell commands or JSON examples when setup is required]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-user output depends on confirmed service scope, delegated workplace access, connector availability, and optional team signal packs.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
