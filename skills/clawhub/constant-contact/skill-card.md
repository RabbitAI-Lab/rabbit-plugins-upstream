## Description:

Constant Contact API integration with managed OAuth for reading, creating, updating, deleting, and bulk-modifying contacts, email campaigns, contact lists, tags, custom fields, segments, and marketing analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to administer Constant Contact marketing data through Maton-managed OAuth, with read/list operations as the default and explicit approval required for writes such as contact changes, campaign sending, scheduling, imports, exports, bulk list changes, and deletions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable Constant Contact operations can send or schedule campaigns, change contact data, perform imports or exports, modify lists in bulk, or delete resources.

Mitigation: Default to read/list calls, verify the target resource and intended effect, and require explicit user approval with specific identifiers before each write or high-impact action.

Risk: Credential exposure or overly broad authorization can give an agent unnecessary access to a Constant Contact account.

Mitigation: Prefer OAuth through the Maton CLI, keep scopes narrow, avoid printing or persisting tokens and API keys, and revoke unused Maton connections.

Risk: Using an ambiguous Maton account or connection can apply changes to the wrong Constant Contact account.

Mitigation: List connections first and specify the intended connection when more than one Constant Contact connection is available.

## Reference(s):

- [ClawHub Constant Contact Skill](https://clawhub.ai/byungkyu/skills/constant-contact)
- [Maton](https://maton.ai)
- [Constant Contact V3 API Overview](https://developer.constantcontact.com/api_guide/getting_started.html)
- [Constant Contact API Reference](https://developer.constantcontact.com/api_reference/index.html)
- [Constant Contact Technical Overview](https://developer.constantcontact.com/api_guide/v3_technical_overview.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a valid Constant Contact connection; write-capable operations require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
