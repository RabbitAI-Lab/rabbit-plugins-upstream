## Description:

Helps agents access Cognito Forms to list forms, manage entries, and retrieve submitted documents through an authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People managing Cognito Forms submissions use this skill to inspect forms and entries, update or delete entries with approval, and retrieve documents. Developers can use its connection and automation guidance for approved workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected account can expose or change Cognito Forms business data.

Mitigation: Use read-only access where possible and confirm the target and effect before each write or deletion.

Risk: Raw API keys can expose a long-lived credential.

Mitigation: Prefer the Maton CLI's managed login; use raw API keys only when the CLI cannot be used.

Risk: Trigger destinations can continuously forward event data.

Mitigation: Obtain separate approval for each destination and verify its endpoint and expected data before enabling it.

## Reference(s):

- [Cognito Forms API overview](https://www.cognitoforms.com/support/475/data-integration/cognito-forms-api)
- [Maton homepage](https://maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include form entries or document links containing sensitive business or personal data.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
