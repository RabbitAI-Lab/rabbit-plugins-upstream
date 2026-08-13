## Description:

Automatically organizes a Gmail inbox every hour by reading inbox messages, classifying each email into one of eleven labels, applying the selected label, archiving processed messages, and sending Telegram alerts for messages tagged Important.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

External users, busy professionals, and teams use this skill to automate recurring Gmail triage, keep inboxes clear, and receive Telegram notifications for important emails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The hosted workflow has recurring access to read full Gmail messages and process every inbox email.

Mitigation: Confirm Gmail permissions before installation and test the workflow on a low-risk mailbox or limited account before enabling it on a primary mailbox.

Risk: The workflow archives processed Gmail messages, which can remove messages from the inbox even when classification is wrong.

Mitigation: Verify that labels and archive behavior are reversible, and monitor early runs before relying on unattended hourly execution.

Risk: Important-email subjects or links may be sent through Telegram.

Mitigation: Confirm Telegram destination settings and avoid using the workflow where email subjects or message links would expose sensitive information to an unintended chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/ai-gmail-inbox-classifier-auto-archive-with-hourly-telegram)
- [AgentPMT workflow page](https://www.agentpmt.com/agent-workflow-skills/ai-gmail-inbox-classifier-auto-archive-with-hourly-telegram-alerts)
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)
- [Gmail - All Email Actions](https://clawhub.ai/agentpmt/gmail-all-email-actions)
- [Telegram Instant Messenger](https://clawhub.ai/agentpmt/telegram-instant-messenger)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, configuration]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides AgentPMT-hosted workflow calls that read, label, archive, and summarize Gmail messages and send Telegram alerts for important messages.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
