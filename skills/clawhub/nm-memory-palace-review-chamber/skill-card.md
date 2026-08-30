## Description:

Captures and retrieves PR-review findings in memory palaces for architectural decisions, recurring patterns, standards, and lessons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill after pull request review to preserve durable review knowledge, classify findings, and retrieve past decisions or patterns during future work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent review memory may include security issues, private implementation details, or contributor identities.

Mitigation: Confirm persistent capture is appropriate for the repository and configure retention, export, and search scope to match team privacy expectations.

Risk: Stored review decisions or patterns may become stale and mislead later reviews.

Mitigation: Review entries periodically, prune outdated knowledge, and surface contradictions when new captured entries conflict with existing memory.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-memory-palace-review-chamber)
- [ClawHub Publisher Profile](https://clawhub.ai/user/athola)
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/memory-palace)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell command examples and structured review-memory entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference configured memory-palace rooms, PR identifiers, tags, and search filters.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
