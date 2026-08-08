## Description:

This skill guides an agent through an hourly AgentPMT workflow that reads Gmail inbox messages, classifies each message into a Gmail label, archives processed mail, and sends Telegram alerts for messages classified as important.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams use this skill to automate routine Gmail inbox triage, reduce visible inbox clutter, and receive Telegram notifications for messages marked important.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic archiving can remove messages from the inbox before the user has reviewed them.

Mitigation: Test on a limited mailbox or with reversible labels first, and confirm the label and archive behavior before enabling routine hourly runs.

Risk: The workflow reads Gmail message content and sends Telegram alerts with links for important emails.

Mitigation: Confirm the connected Gmail and Telegram accounts are appropriate for this automation and that recipients are allowed to receive these alerts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/ai-gmail-inbox-classifier-auto-archive-with-hourly-telegram)
- [AgentPMT workflow page](https://www.agentpmt.com/agent-workflow-skills/ai-gmail-inbox-classifier-auto-archive-with-hourly-telegram-alerts)
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)
- [Gmail - All Email Actions](https://clawhub.ai/agentpmt/gmail-all-email-actions)
- [Telegram Instant Messenger](https://clawhub.ai/agentpmt/telegram-instant-messenger)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown instructions with JSON snippets and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent workflow steps for Gmail labeling, archiving, Telegram alerts, and hourly summary reporting.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
