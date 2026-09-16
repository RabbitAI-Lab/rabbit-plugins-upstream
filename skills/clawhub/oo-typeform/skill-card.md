## Description:

Provides agents with schema-first, read-oriented access to Typeform account data, forms, workspaces, and form responses through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to retrieve Typeform user, form, workspace, and response data from a connected Typeform account without calling the Typeform API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Typeform request and response data is routed through OOMOL.

Mitigation: Install and use the connector only for Typeform accounts whose data can be processed through OOMOL, especially when forms contain sensitive responses.

Risk: Setup instructions include remote installer scripts for the oo CLI.

Mitigation: Prefer a verified, signed, or checksum-checked oo CLI installation method before using the connector.

Risk: Connector execution depends on the live action schema and connected account scopes.

Mitigation: Inspect the action schema with `oo connector schema` before execution and reconnect Typeform only when an auth, scope, or credential error requires it.

## Reference(s):

- [ClawHub Typeform Skill](https://clawhub.ai/oomol/skills/oo-typeform)
- [Typeform Homepage](https://www.typeform.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; response data may include Typeform account and response contents.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
