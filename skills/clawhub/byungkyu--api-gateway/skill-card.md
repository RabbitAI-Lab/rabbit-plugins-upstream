## Description:

Call third-party APIs through Maton's managed API gateway without managing authentication directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access external apps such as email, CRM, issue tracking, spreadsheets, and automation triggers through Maton. The skill is intended to start with read actions when possible and require confirmation for account authorization or data-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill brokers access to selected third-party accounts and can perform powerful write or delete operations.

Mitigation: Prefer OAuth, grant only the narrowest required scopes, start with read actions when possible, and require explicit confirmation before every write or delete.

Risk: Trigger destinations can create persistent automatic data forwarding to external URLs.

Mitigation: Use only user-specified trusted destination hosts, disclose what data will be forwarded and that delivery is ongoing, and avoid public inspection endpoints.

Risk: Maton credentials or provider-issued tokens could be exposed if printed, logged, persisted, or embedded in destination headers or templates.

Mitigation: Keep credentials in OAuth/keyring flows where possible, never print or store tokens, and do not place Maton or provider credentials in trigger destination headers or body templates.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, API request examples, app connection guidance, and trigger configuration guidance.]

## Skill Version(s):

1.0.142 (source: server release metadata; artifact frontmatter metadata.version is 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
