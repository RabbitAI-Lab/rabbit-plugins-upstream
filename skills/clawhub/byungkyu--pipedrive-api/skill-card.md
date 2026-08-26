## Description:

Pipedrive API integration with managed OAuth for managing deals, persons, organizations, activities, and pipelines through the maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to access Pipedrive CRM data and perform sales workflow tasks through an authenticated Maton connection. It supports read/list operations by default and can modify CRM records when the user explicitly confirms the target resource, payload, and intended effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad raw API access can affect more Pipedrive CRM data than the skill's narrower advertised scope.

Mitigation: Authorize only the minimum available Pipedrive scopes, prefer read/list calls first, and require explicit user confirmation for any non-listed endpoint or POST, PUT, PATCH, or DELETE request.

Risk: Writes may target the wrong Pipedrive account or connection when multiple connections exist.

Mitigation: Specify the intended Maton connection for writes and confirm the target resource, payload, and expected effect before execution.

Risk: Long-lived API keys or provider-issued credentials could leak through logs, files, shell history, or command arguments.

Mitigation: Prefer OAuth through the Maton CLI, avoid printing or persisting credentials, and send raw HTTP credentials only to api.maton.ai when CLI use is impossible.

## Reference(s):

- [Pipedrive Skill on ClawHub](https://clawhub.ai/byungkyu/skills/pipedrive-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Pipedrive API Overview](https://developers.pipedrive.com/docs/api/v1)
- [Pipedrive Deals API](https://developers.pipedrive.com/docs/api/v1/Deals)
- [Pipedrive Persons API](https://developers.pipedrive.com/docs/api/v1/Persons)
- [Pipedrive Organizations API](https://developers.pipedrive.com/docs/api/v1/Organizations)
- [Pipedrive Activities API](https://developers.pipedrive.com/docs/api/v1/Activities)
- [Pipedrive Pipelines API](https://developers.pipedrive.com/docs/api/v1/Pipelines)
- [Pipedrive Stages API](https://developers.pipedrive.com/docs/api/v1/Stages)
- [Pipedrive Notes API](https://developers.pipedrive.com/docs/api/v1/Notes)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, SDK snippets, raw HTTP examples, and safety guidance for Pipedrive API operations.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
