## Description:

ManyChat API integration with managed authentication for managing subscribers, tags, custom fields, flows, and Facebook Messenger messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to ManyChat through Maton, inspect subscriber, page, tag, custom-field, and flow data, and perform approved messaging or automation actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make real changes in a connected ManyChat account, including subscriber updates, tag changes, deletion, message sends, and automation triggers.

Mitigation: Confirm the exact account, connection, recipient, payload, and intended effect before any write operation.

Risk: Connection setup grants Maton mediated access to a ManyChat account.

Mitigation: Create or refresh a ManyChat connection only after explicit user approval and select the least privilege scopes available for the task.

Risk: Using an API key instead of OAuth increases exposure of long-lived credentials.

Mitigation: Prefer OAuth login through the Maton CLI, avoid printing or persisting keys, and rotate any key that was exposed.

## Reference(s):

- [ManyChat ClawHub Skill](https://clawhub.ai/byungkyu/skills/manychat)
- [Maton Homepage](https://maton.ai)
- [ManyChat API Documentation](https://api.manychat.com/swagger)
- [ManyChat API Key Generation Guide](https://help.manychat.com/hc/en-us/articles/14959510331420)
- [ManyChat Dev Program](https://help.manychat.com/hc/en-us/articles/14281269835548)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an approved ManyChat connection.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
