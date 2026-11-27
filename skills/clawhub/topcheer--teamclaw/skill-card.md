## Description:

Orchestrate a virtual AI software team to build features, fix bugs, or complete any software task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[topcheer](https://clawhub.ai/user/topcheer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use TeamClaw to delegate software work to a virtual team of roles, track progress and results, and respond to worker clarifications through a running TeamClaw controller.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad build or create requests can initiate multi-role task orchestration and messages through the controller.

Mitigation: Review the request and intended recipients before submitting it, then monitor controller status and worker results.

Risk: The security scan was partial and does not establish that all behavior is safe.

Mitigation: Review the skill and unresolved local references before enabling it, and use a trusted TeamClaw controller.

## Reference(s):

- [TeamClaw API Quick Reference](artifact/references/api-quick-ref.md)
- [TeamClaw documentation](https://github.com/topcheer/teamclaw/blob/main/README.md)
- [TeamClaw releases](https://github.com/topcheer/teamclaw/releases)
- [TeamClaw project homepage](https://github.com/topcheer/teamclaw)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown summaries and operational guidance, with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task and worker status summaries, deliverable reviews, and clarification prompts.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
