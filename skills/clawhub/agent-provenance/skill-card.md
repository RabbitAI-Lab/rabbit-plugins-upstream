## Description:

Tracks authorship and review history for agent instruction and memory files with provenance headers, git conventions, and scheduled or on-demand review guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[richgoodson](https://clawhub.ai/user/richgoodson)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and agent operators use this skill to track who changed instruction and memory files, review stale material, and produce audit-friendly change reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to agent instruction and memory files can affect future agent behavior or expose private context in reports.

Mitigation: Review proposed edits and reports, preserve user-owned rules, and avoid secrets in provenance headers and commit messages.

Risk: An optional weekly check continues running until disabled or removed.

Mitigation: Enable it only after explicit user consent and use the documented OpenClaw automation commands to disable or remove it.

## Reference(s):

- [Agent Provenance on ClawHub](https://clawhub.ai/richgoodson/skills/agent-provenance)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown reports and guidance with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [On-demand change reports; optional weekly reports only with user approval.]

## Skill Version(s):

2.2.1 (source: skill metadata and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
