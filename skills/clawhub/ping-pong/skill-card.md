## Description:

Agent Ping-Pong guides a human-mediated workflow for passing structured handoff blocks between OpenClaw and Codex or Claude Code so code can be built, reviewed, and merged through GitHub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[highnoonoffice](https://clawhub.ai/user/highnoonoffice)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical operators use this skill to coordinate a human-in-the-loop coding workflow where one agent writes implementation work and another specs, reviews, and approves changes. It is intended for GitHub pull-request workflows that separate sandbox building from production porting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may route raw handoff blocks to a hardcoded Telegram chat, which can expose project details outside the local clipboard workflow.

Mitigation: Use the skill only if that routing is intentional, or remove or disable the Telegram gates before installation.

Risk: Handoff blocks and clipboard contents can expose secrets or sensitive project details if users paste credentials into them.

Mitigation: Keep credentials in agent configuration only, never include secrets in handoff blocks, and review blocks before sending them through external channels.

Risk: Broad GitHub tokens can expand the impact of an agent error beyond the intended sandbox or production repositories.

Mitigation: Use fine-grained, repo-scoped GitHub tokens with only the documented Contents, Pull Requests, and Metadata permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/highnoonoffice/skills/ping-pong)
- [Project homepage](https://github.com/highnoonoffice/agent-ping-pong)
- [OpenClaw](https://openclaw.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured [AGENT_HANDOFF] blocks and inline commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires human relay, review, and explicit merge approval.]

## Skill Version(s):

2.8.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
