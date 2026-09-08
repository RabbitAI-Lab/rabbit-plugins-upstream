## Description:

Benxiang is a persistent object representation layer for AI work that helps agents recover project state, commit semantic transactions, enforce deterministic gates, and trace why stored values exist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dongsheng123132](https://clawhub.ai/user/dongsheng123132)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to guide persistent project-state workflows, especially when new sessions lose context, multi-agent work drifts, or decisions, tasks, facts, risks, and provenance need accountable replay.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The referenced workflow persists project decisions, tasks, facts, risks, and provenance in local .origin packages, which can expose sensitive project state if used carelessly.

Mitigation: Avoid committing secrets or sensitive private data unless intended, and review package contents before sharing or publishing.

Risk: The skill references external repository commands that execute code outside the bundled artifact.

Mitigation: Review the referenced repository or run it in an isolated workspace before installation or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dongsheng123132/skills/benxiang-protocol)
- [Publisher profile](https://clawhub.ai/user/dongsheng123132)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local .origin package operations and MCP integration; no bundled executable code was found in the skill artifact.]

## Skill Version(s):

1.1.1 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
