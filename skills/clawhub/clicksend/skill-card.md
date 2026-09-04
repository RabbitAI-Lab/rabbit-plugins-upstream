## Description:

ClickSend API integration with managed authentication for sending SMS, MMS, and voice messages and managing contacts, lists, verified email addresses, and account configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent interact with a connected ClickSend account through Maton for messaging, delivery tracking, contact and list management, verified sender management, and account checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messaging operations can contact real recipients and may incur costs.

Mitigation: Confirm the recipient, message content, sender identity, and send timing before approving any SMS, MMS, or voice send.

Risk: Account, contact, list, and verified sender changes can affect live ClickSend resources.

Mitigation: Use read or list calls first, verify the target account and resource identifiers, and require explicit approval before write operations.

Risk: Long-lived Maton API keys can be exposed through logs, command history, or child processes.

Mitigation: Prefer OAuth through the Maton CLI and avoid printing, persisting, or passing credentials on command lines.

Risk: Multiple Maton profiles or ClickSend connections can route a write to the wrong account.

Mitigation: Specify the intended profile or connection when more than one account or connection is available.

## Reference(s):

- [ClickSend skill page](https://clawhub.ai/byungkyu/skills/clicksend)
- [Maton homepage](https://maton.ai)
- [ClickSend Developer Portal](https://developers.clicksend.com/)
- [ClickSend REST API v3 Documentation](https://developers.clicksend.com/docs)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized ClickSend connection]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
