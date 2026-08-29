## Description:

Implements structured usage logging and audit trails for cost and session tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add structured JSONL usage logs, session tracking, audit trails, cost tracking, and debugging analytics to agent skills or plugins.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Usage logs and metadata may capture secrets, sensitive user content, or more operational detail than intended.

Mitigation: Keep logged metadata minimal, exclude secrets and sensitive content, and review the log schema before deployment.

Risk: Local JSONL logs and session files can accumulate or remain available longer than intended.

Mitigation: Choose an explicit storage path and define retention, access, and deletion rules for log and session files.

## Reference(s):

- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)
- [Log Formats](modules/log-formats.md)
- [Session Patterns](modules/session-patterns.md)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown with Python, JSON, YAML, and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides implementation patterns for local logging; it does not execute logging itself.]

## Skill Version(s):

1.9.19 (source: server release evidence; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
