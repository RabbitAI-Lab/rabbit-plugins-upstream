## Description:

ClickSend provides managed ClickSend API access through Maton so agents can send SMS, MMS, and voice messages, manage contacts and lists, manage verified email addresses, and inspect account configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to operate a connected ClickSend account for message delivery, delivery tracking, contact management, list management, verified sender address management, and account checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send SMS, MMS, and voice messages to real recipients, which may create cost, privacy, and reputation impacts.

Mitigation: Confirm the exact recipient, message content, sending account or connection, timing, and expected cost before any send operation.

Risk: The skill can delete or modify contacts, contact lists, scheduled messages, and verified sender email addresses in a ClickSend account.

Mitigation: Default to read and list operations, verify resource identifiers first, and require explicit user approval before POST, PUT, PATCH, or DELETE requests.

Risk: Ambiguous Maton profiles or ClickSend connections can route a write to the wrong account.

Mitigation: Specify the intended Maton profile and ClickSend connection whenever multiple accounts or connections are present.

## Reference(s):

- [ClickSend skill on ClawHub](https://clawhub.ai/byungkyu/skills/clicksend)
- [Maton homepage](https://maton.ai)
- [ClickSend Developer Portal](https://developers.clicksend.com/)
- [ClickSend REST API v3 Documentation](https://developers.clicksend.com/docs)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run ClickSend API calls through the Maton CLI after the user confirms write operations.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
