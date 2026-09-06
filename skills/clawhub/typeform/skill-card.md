## Description:

Typeform API integration with managed OAuth for creating forms, managing responses, and accessing insights through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect a Typeform account, inspect forms and responses, and perform approved form-management API calls. It is suited for agents that need guided Typeform access while keeping credentials in Maton-managed OAuth or credential storage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on a connected Typeform account through Maton.

Mitigation: Use OAuth where possible, choose the narrowest Typeform scopes available, and confirm the intended account before connecting or acting.

Risk: Form changes or deletions can alter or remove Typeform resources.

Mitigation: Review proposed form changes, target identifiers, payloads, and deletion effects before approving any write operation.

Risk: Long-lived API keys are more exposed than OAuth-backed CLI credentials.

Mitigation: Prefer OAuth login and avoid printing, logging, exporting, or persisting credentials.

## Reference(s):

- [ClawHub Typeform Skill](https://clawhub.ai/byungkyu/skills/typeform)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Typeform API Overview](https://www.typeform.com/developers/get-started)
- [Typeform Forms API](https://www.typeform.com/developers/create/reference/retrieve-forms)
- [Typeform Responses API](https://www.typeform.com/developers/responses/reference/retrieve-responses)
- [Typeform Workspaces API](https://www.typeform.com/developers/create/reference/retrieve-workspaces)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, configuration, code]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing instructions for Maton CLI and SDK use; API responses are returned by Typeform through Maton.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
