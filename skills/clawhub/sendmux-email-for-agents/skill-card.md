## Description:

Give OpenClaw agents a Sendmux inbox to receive, triage, route, reply to, and send email with owner approval and scoped credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external teams use this skill to route agent-email tasks across Sendmux mailbox setup, mailbox triage, replies, outbound sending, attachments, MCP setup, CLI use, and token-efficient workflows. It is intended for agents that need an inbox, mailbox identity, outbound email, triage loop, reply workflow, or human approval path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI package could introduce package-source or trust risk.

Mitigation: Confirm that @sendmux/cli is the intended official package before installation.

Risk: Mailbox credentials or OAuth tokens could be exposed or over-scoped during setup and runtime.

Mitigation: Use scoped Sendmux credentials, do not paste secrets into chat, and let the CLI persist agent profiles where applicable.

Risk: Agents could send email or mutate mailbox state without adequate human control.

Mitigation: Keep human approval in place for sending, label/read-state changes, deletes, key revocation, suspend, and resume actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sendmux.ai/skills/sendmux-email-for-agents)
- [Sendmux Skills Repository](https://github.com/Sendmux/skills)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with routed skill names, credential scope notes, runtime surface choices, core calls, approval checkpoints, and efficiency patterns.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Designed to keep detailed implementation in task-specific Sendmux skills after the route is clear.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
