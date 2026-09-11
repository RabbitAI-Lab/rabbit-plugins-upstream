## Description:

ManyChat API integration with managed authentication for managing subscribers, tags, custom fields, flows, and Facebook Messenger messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage ManyChat pages, subscribers, tags, custom fields, flows, and outbound Messenger messages through Maton's authenticated gateway.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton mediates authentication and API access for the connected ManyChat account.

Mitigation: Verify that Maton is trusted for the account before installation or connection, and prefer OAuth over long-lived API keys.

Risk: Write actions and message sends can change subscriber data or contact external recipients.

Mitigation: Confirm the exact account, connection, target resource, payload, and intended effect before any POST, PUT, PATCH, DELETE, or message-send operation.

Risk: API keys or provider-issued tokens can leak through logs, files, shell history, or command arguments.

Mitigation: Keep credentials in OAuth or managed credential stores where possible; never print, log, persist, or pass keys on a command line, and rotate any exposed key.

Risk: CLI or SDK installation can introduce supply-chain concerns in controlled environments.

Mitigation: Pin, isolate, or otherwise control CLI and SDK installs when operating under strict supply-chain requirements.

## Reference(s):

- [ManyChat skill page on ClawHub](https://clawhub.ai/byungkyu/skills/manychat)
- [Maton homepage](https://maton.ai)
- [ManyChat API Documentation](https://api.manychat.com/swagger)
- [ManyChat API Key Generation Guide](https://help.manychat.com/hc/en-us/articles/14959510331420)
- [ManyChat Dev Program](https://help.manychat.com/hc/en-us/articles/14281269835548)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton CLI or SDK calls with OAuth preferred; raw HTTP examples are limited to environments where the CLI cannot be installed.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
