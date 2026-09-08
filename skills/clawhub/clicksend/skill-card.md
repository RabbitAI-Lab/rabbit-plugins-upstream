## Description:

ClickSend is a Maton-backed API integration that helps agents send SMS, MMS, and voice messages, manage contacts and lists, manage verified sender email addresses, and inspect delivery and account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to connect a ClickSend account, send or price messages, manage contact lists and sender addresses, and track delivery. The skill is suited for agent-assisted ClickSend operations where reads are preferred first and write actions require explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messaging operations can deliver SMS, MMS, or voice messages to real recipients and may incur costs.

Mitigation: Confirm the target account, recipient, content, timing, and pricing intent before approving any send action.

Risk: Write operations can modify ClickSend contacts, lists, verified sender email addresses, and account configuration.

Mitigation: Default to read or list calls first, verify exact resource identifiers and payloads, and require explicit user approval before POST, PUT, PATCH, or DELETE requests.

Risk: Connection creation or ambiguous defaults can authorize or operate on the wrong ClickSend account.

Mitigation: Ask for approval before creating a connection and specify the intended connection or profile when multiple accounts are available.

Risk: Fallback raw HTTP use requires handling a long-lived Maton API key.

Mitigation: Prefer OAuth through the Maton CLI; if a key is unavoidable, do not print, log, persist, or pass it on a command line, and send it only to api.maton.ai.

## Reference(s):

- [ClawHub ClickSend Skill](https://clawhub.ai/byungkyu/skills/clicksend)
- [Maton Homepage](https://maton.ai)
- [Maton API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
- [ClickSend Developer Portal](https://developers.clicksend.com/)
- [ClickSend REST API v3 Documentation](https://developers.clicksend.com/docs)
- [ClickSend PHP SDK](https://github.com/ClickSend/clicksend-php)
- [ClickSend Help Center](https://help.clicksend.com/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an active ClickSend connection; write actions require explicit user approval.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
