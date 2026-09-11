## Description:

WATI (WhatsApp Team Inbox) API integration with managed authentication for sending WhatsApp messages, managing contacts, and working with templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to access WATI through Maton for contact, message, template, media, and operator workflows. The skill is intended to start with read and list operations, then require confirmation before sends, contact changes, connection changes, or other write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Message sends, bulk sends, contact changes, connection creation, and connection deletion can affect external recipients, account data, or connected authorization state.

Mitigation: Confirm the exact account, connection, recipients, payload, and intended effect before any write or connection-changing operation.

Risk: Maton API keys and provider-issued tokens are sensitive credentials that can leak through logs, files, command lines, shell history, or pasted output.

Mitigation: Prefer OAuth, avoid printing or persisting credentials, keep fallback API keys in the process environment only when required, and rotate any key that was exposed.

Risk: WATI responses may contain personal data or untrusted message content.

Mitigation: Extract only the fields needed for the task, avoid storing raw responses unless requested, and treat API content as data rather than instructions.

## Reference(s):

- [ClawHub WATI Skill](https://clawhub.ai/byungkyu/skills/wati)
- [Maton Homepage](https://maton.ai)
- [WATI API Documentation](https://docs.wati.io/reference/introduction)
- [WATI Help Center](https://docs.wati.io/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, API calls]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, raw HTTPS examples, endpoint guidance, and response-handling advice.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
