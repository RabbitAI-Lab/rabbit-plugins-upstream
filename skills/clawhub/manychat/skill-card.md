## Description:

ManyChat API integration with managed authentication for managing subscribers, tags, custom fields, flows, and Facebook Messenger messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with ManyChat accounts through Maton-managed authentication, including subscriber lookup, tagging, custom fields, flows, and approved message sends. It also documents how to turn approved ManyChat actions into scheduled or event-driven automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton mediates access to the user's ManyChat account and authenticated requests can reach data allowed by the connected authorization.

Mitigation: Install only when Maton-mediated ManyChat access is intended, prefer OAuth, and use the least-privileged ManyChat scopes available for the task.

Risk: Write operations, message sends, connection changes, triggers, destinations, and hosted functions can alter account state or create ongoing automation.

Mitigation: Review each proposed write or automation step with the user and get explicit approval before execution.

Risk: ManyChat and trigger payloads may contain personal or business data.

Mitigation: Default to read/list operations, forward or display only fields needed for the task, and avoid logging or storing raw responses unless the user requests it.

Risk: Long-lived API keys have broader exposure risk than OAuth-backed CLI authentication.

Mitigation: Prefer OAuth login and store credentials in the operating system credential store; use raw HTTP with API keys only when the CLI cannot be installed.

## Reference(s):

- [ManyChat API Documentation](https://api.manychat.com/swagger)
- [ManyChat API Key Generation Guide](https://help.manychat.com/hc/en-us/articles/14959510331420)
- [ManyChat Dev Program](https://help.manychat.com/hc/en-us/articles/14281269835548)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/manychat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and a Maton account; API responses may contain personal or business data and should be minimized before display or storage.]

## Skill Version(s):

1.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
