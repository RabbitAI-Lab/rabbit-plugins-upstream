## Description:

Captures messaging misses, channel underperformance, audience drift, brand inconsistency, attribution gaps, and content decay to enable continuous marketing improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and agent operators use this skill to capture campaign issues, marketing learnings, and feature requests in local Markdown logs, then promote repeated patterns into durable marketing standards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional hooks can inspect local Bash output for marketing-related signals.

Mitigation: Keep hooks project-scoped and enable PostToolUse behavior only when local inspection of Bash output is acceptable.

Risk: Marketing logs can accidentally capture customer data, credentials, or sensitive revenue details.

Mitigation: Redact customer and revenue data, avoid secrets, and prefer aggregated metrics and campaign identifiers.

Risk: Promoting lessons into agent instruction files or generated skills can change future agent behavior.

Mitigation: Review proposed changes before applying them and require explicit user approval for promotion into agent-control files or generated skills.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jose-compu/skills/self-improving-marketing)
- [OpenClaw Integration](references/openclaw-integration.md)
- [Hooks Setup](references/hooks-setup.md)
- [Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional local Markdown log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local .learnings Markdown files when the user chooses to log marketing insights.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
