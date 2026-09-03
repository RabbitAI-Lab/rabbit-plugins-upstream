## Description:

Technical daily brief for engineers: service health, deploys, alerts, DLQ/latency, workflows, migrations, customer signals. Use for engineering/on-call briefs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vmishra-atlassian](https://clawhub.ai/user/vmishra-atlassian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, on-call responders, engineering managers, and PMs use this skill to assemble a daily service-health and work-priority brief from delegated workspace sources. It is intended for morning engineering briefs, on-call handoffs, and service-health review where each user's confirmed scope controls what appears.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill combines service-health signals with Jira work, PRs, calendar events, notifications, Slack search results, and operational sources under the invoking user's delegated access.

Mitigation: Install only where that combined brief is intended, confirm the per-user service scope, and schedule recurring runs only when that recurring read access is acceptable.

Risk: Incorrect or copied per-user scope can cause a brief to report services the current user does not own.

Mitigation: Require first-run scope confirmation and do not copy memory/engineering-brief between users; delete stale scope.json and rerun discovery if the service list is wrong.

Risk: Connector gaps or consent failures can make a source unavailable during a brief.

Mitigation: Preserve the coverage report and label unavailable sources as not checked instead of treating missing data as healthy.

Risk: Tool schemas and runtime requirements may differ, which can produce broad or misleading results if inputs are silently ignored.

Mitigation: Verify tool schemas before relying on results, use exact parameter names, bound queries, and sanity-check counts against the expected service scope.

Risk: Slack and similar communications can expose irrelevant or private context if broad search results are retained.

Mitigation: Use the delegated Rovo route, keep only results from allowlisted operational channels, exclude DMs, and avoid retaining raw message bodies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vmishra-atlassian/skills/brief-engineering)
- [README](README.md)
- [Signal catalogue](references/signal-catalog.md)
- [Team signal pack contract](references/signal-packs.md)
- [Persona presentation policy](references/personas.md)
- [Rolling this out to a team](references/team-adoption.md)
- [Sharing this with a teammate](references/install-for-teammates.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief with ordered action buckets, evidence links, coverage notes, and inline command or configuration snippets where useful.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses delegated workspace access and reports unavailable sources as not checked rather than healthy.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
