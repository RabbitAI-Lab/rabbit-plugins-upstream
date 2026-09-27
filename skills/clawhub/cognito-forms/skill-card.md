## Description:

Cognito Forms API integration with managed OAuth for accessing forms, managing entries, and retrieving documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, and developers use this skill to manage Cognito Forms forms, entries, and documents through Maton-authenticated API calls, and to set up approved automation through functions or triggers when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Cognito Forms account data through a Maton-managed connection.

Mitigation: Use OAuth where possible, select only needed scopes, specify the intended connection when multiple connections exist, and revoke unused connections.

Risk: Write, delete, connection, hosted function, or automation actions can change data or create ongoing behavior.

Mitigation: Default to read and list calls, then require explicit user approval for the target resource, payload, and intended effect before any modifying operation.

Risk: Raw HTTP fallback requires a long-lived Maton API key that can leak through environment variables, logs, shell history, or pasted output.

Mitigation: Prefer the Maton CLI credential store; use raw HTTP only where the CLI cannot be installed, avoid printing secrets, and rotate the key if it is exposed.

Risk: Trigger destinations can keep forwarding future event data until removed.

Mitigation: Create persistent destinations only after the user approves the exact URL, data fields, persistence, and credential handling, and delete destinations that are no longer needed.

## Reference(s):

- [Cognito Forms API Overview](https://www.cognitoforms.com/support/475/data-integration/cognito-forms-api)
- [Cognito Forms REST API Reference](https://www.cognitoforms.com/support/476/data-integration/cognito-forms-api/rest-api-reference)
- [Cognito Forms API Reference](https://www.cognitoforms.com/support/476/data-integration/cognito-forms-api/api-reference)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Catalog](references/time/triggers.md)
- [Google Mail Trigger Catalog](references/google-mail/triggers.md)
- [GitHub Trigger Catalog](references/github/triggers.md)
- [Slack Trigger Catalog](references/slack/triggers.md)
- [Stripe Trigger Catalog](references/stripe/triggers.md)
- [Calendly Trigger Catalog](references/calendly/triggers.md)
- [HubSpot Trigger Catalog](references/hubspot/triggers.md)
- [Linear Trigger Catalog](references/linear/triggers.md)
- [Notion Trigger Catalog](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with CLI commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include authenticated API-call plans and least-privilege approval prompts.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
