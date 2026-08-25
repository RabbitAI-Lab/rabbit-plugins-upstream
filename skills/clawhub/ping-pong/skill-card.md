## Description:

Your OpenClaw is the brain. Codex or Claude Code are the hands. The clipboard is the protocol.

This skill is ready for commercial/non-commercial use.

## Publisher:

[highnoonoffice](https://clawhub.ai/user/highnoonoffice)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and builders use this skill to coordinate OpenClaw with Codex or Claude Code for GitHub-based coding work, routing specs, PR reports, reviews, and merge approvals through structured handoff blocks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Handoff content may be sent to a hard-coded Telegram chat outside the local clipboard workflow.

Mitigation: Remove or disable the Telegram instructions unless that external relay is explicitly intended and approved.

Risk: The workflow requires scoped GitHub write tokens for the participating agents.

Mitigation: Use fine-grained tokens limited to the intended sandbox and production repositories, and review permissions before installation.

Risk: Structured handoff blocks can carry sensitive information through the clipboard or external relay.

Mitigation: Keep raw secrets out of handoff blocks and store credentials only in agent configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/highnoonoffice/skills/ping-pong)
- [Project homepage](https://github.com/highnoonoffice/agent-ping-pong)
- [OpenClaw](https://openclaw.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured handoff blocks and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires human relay and approval gates; credentials remain in agent configuration.]

## Skill Version(s):

2.8.2 (source: server release evidence; artifact frontmatter: 2.8.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
