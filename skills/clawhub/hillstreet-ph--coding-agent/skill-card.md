## Description:

Delegate coding work to Codex, Claude Code, or OpenCode as background workers; not simple edits or read-only code lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to delegate substantial coding work to Codex, Claude Code, or OpenCode as background workers, including feature builds, PR reviews, large refactors, and issue-to-PR workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill launches Claude Code with permission checks bypassed, creating a significant permissions risk.

Mitigation: Review this behavior before installation; only run trusted tasks in an isolated environment with deliberately limited access.

Risk: The security scan is partial because two local path-like references could not be resolved, so it does not establish that the artifact is safe.

Mitigation: Review the unresolved references and inspect the complete artifact before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hillstreet-ph/skills/coding-agent)

## Skill Output:

**Output Type(s):** [Code, Files, Markdown, Guidance]

**Output Format:** [Project changes with a Markdown completion or failure report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Depends on the delegated coding task and target repository.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
