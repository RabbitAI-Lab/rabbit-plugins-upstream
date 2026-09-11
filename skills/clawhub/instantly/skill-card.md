## Description:

Instantly API integration with managed OAuth for managing campaigns, leads, sending accounts, email workflows, and analytics through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an Instantly account through Maton, inspect outreach data, manage campaigns and leads, and perform approved write operations such as updates, sends, and deletes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify outreach data, including creating, updating, sending, or deleting resources.

Mitigation: Confirm the target account, resource IDs, payload, and intended effect before any write operation.

Risk: Long-lived API keys can be exposed if OAuth is not used.

Mitigation: Prefer OAuth, install Maton and SDK packages only from the official publisher, and use isolated environments for raw HTTP fallback.

## Reference(s):

- [ClawHub Instantly Skill](https://clawhub.ai/byungkyu/skills/instantly)
- [Maton Homepage](https://maton.ai)
- [Instantly API V2 Documentation](https://developer.instantly.ai/api-reference)
- [Instantly API Introduction](https://developer.instantly.ai/)
- [Instantly Help Center](https://help.instantly.ai/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton CLI or SDK calls; defaults to read/list guidance and requires explicit user approval for connection creation and write operations.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
