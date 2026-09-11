## Description:

ClickSend API integration with managed authentication for sending SMS, MMS, and voice messages, managing contacts, lists, verified email addresses, and account configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with ClickSend through Maton: send or price SMS, MMS, and voice messages, manage contacts and lists, manage verified email addresses, and inspect delivery/account data. It is intended for workflows where the user explicitly confirms account authorization and every write or outbound communication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send SMS, MMS, and voice messages to real recipients and may incur costs.

Mitigation: Confirm the recipient, content, timing, and intended connection before sending; use read or price checks first when practical.

Risk: The skill can modify contacts, contact lists, verified sender identities, and account configuration.

Mitigation: Require explicit user approval for every POST, PUT, PATCH, or DELETE request, including exact resource identifiers and payload details.

Risk: Multiple Maton or ClickSend connections can cause writes to land in the wrong account.

Mitigation: List available connections and specify the intended connection when more than one account exists.

Risk: API keys, provider tokens, and raw API responses can expose credentials or personal data.

Mitigation: Prefer OAuth, use the narrowest ClickSend scopes available, avoid printing or logging secrets, and return only the response fields needed for the task.

## Reference(s):

- [ClawHub ClickSend Skill](https://clawhub.ai/byungkyu/skills/clicksend)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [ClickSend Developer Portal](https://developers.clicksend.com/)
- [ClickSend REST API v3 Documentation](https://developers.clicksend.com/docs)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include ClickSend response data; responses can contain personal data and should be minimized to the fields needed for the task.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
