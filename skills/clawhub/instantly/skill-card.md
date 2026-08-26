## Description:

Instantly API integration with managed OAuth for managing campaigns, leads, sending accounts, and analytics through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an Instantly account through Maton, inspect outreach data, and manage campaigns, leads, sending accounts, email activity, and analytics with user-approved API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can affect outreach data and external email workflows in a connected Instantly account.

Mitigation: Default to read and list operations, verify target resources first, and require explicit user approval before any connection creation or write operation.

Risk: High-impact actions such as sending emails, activating campaigns, deleting records, or adding sending accounts can have reputation, data-loss, or credential-handling consequences.

Mitigation: Review write operations carefully with concrete resource identifiers, payloads, and intended effects before approval.

Risk: Credential exposure could occur if tokens or API keys are printed, persisted, or passed through unsafe shell arguments.

Mitigation: Use OAuth and the Maton CLI credential store when possible; when fallback API keys are required, avoid printing or persisting keys and send them only to the Maton API host.

Risk: Content returned from the Instantly API may contain untrusted instructions or adversarial text.

Mitigation: Treat API responses as data, validate them before reuse, and do not let fetched content choose endpoints, recipients, or follow-up commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/instantly)
- [Maton](https://maton.ai)
- [Instantly API V2 Documentation](https://developer.instantly.ai/api-reference)
- [Instantly API Introduction](https://developer.instantly.ai/)
- [Instantly Help Center](https://help.instantly.ai/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API call plans and Maton CLI commands; write actions require explicit user approval.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
