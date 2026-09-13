## Description:

Cognito Forms API integration with managed OAuth for accessing forms, entries, and documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to work with Cognito Forms through a Maton connection: listing forms, managing entries, retrieving documents, and setting up user-approved automation around form data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party Maton CLI or SDK and a Maton account to access Cognito Forms data.

Mitigation: Install only if the user trusts Maton as the provider, review the package source before installing the CLI or SDK, and keep the reviewed CLI version pinned unless deliberately upgrading.

Risk: API keys and connection credentials can expose form data if handled broadly or stored in unsafe places.

Mitigation: Prefer OAuth, avoid exporting long-lived API keys, and rely on the operating system credential store or the platform-injected runtime credential where applicable.

Risk: Write and delete operations can change or remove Cognito Forms data.

Mitigation: Default to read and list operations first, then require explicit user confirmation of the target resource, payload, and intended effect before any write or delete.

Risk: Triggers and destinations can run continuously or forward data after setup.

Mitigation: Enable automation only after explicit approval, scope triggers narrowly, avoid third-party forwarding unless the user asked for it, and review or remove destinations that are no longer needed.

## Reference(s):

- [Cognito Forms API Overview](https://www.cognitoforms.com/support/475/data-integration/cognito-forms-api)
- [Cognito Forms REST API Reference](https://www.cognitoforms.com/support/476/data-integration/cognito-forms-api/rest-api-reference)
- [Cognito Forms API Reference](https://www.cognitoforms.com/support/476/data-integration/cognito-forms-api/api-reference)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/cognito-forms)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash, JSON, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, raw HTTP examples, and approval checkpoints for write, delete, connection, function, or trigger actions.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
