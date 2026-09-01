## Description:

Pipedrive API integration with managed OAuth for managing deals, persons, organizations, activities, and pipelines through the maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, RevOps, support, and developer users can use this skill to inspect and update Pipedrive CRM records through authenticated API calls. It is suited for CRM workflows involving deals, contacts, organizations, activities, pipelines, notes, users, and related Pipedrive endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The raw API passthrough may reach more Pipedrive endpoints than the short scope list suggests.

Mitigation: Treat the skill as a broad Pipedrive API tool and require explicit confirmation before create, update, delete, messaging, billing, sharing, webhook, or other high-impact actions.

Risk: Authorizing Maton grants access to the selected Pipedrive account.

Mitigation: Before installation or connection creation, confirm that the user is comfortable authorizing Maton for that account and select only the scopes needed for the task when scope selection is available.

Risk: Multiple Pipedrive connections or Maton profiles can make the target account ambiguous.

Mitigation: List active connections first and specify the intended connection or profile before executing any write operation.

Risk: API keys and provider-issued tokens can be exposed through logs, files, command lines, or copied output.

Mitigation: Prefer OAuth through the maton CLI and never print, persist, export, or inspect credentials; use the raw HTTP fallback only when the CLI cannot be installed.

## Reference(s):

- [Pipedrive skill page](https://clawhub.ai/byungkyu/skills/pipedrive-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Pipedrive API Overview](https://developers.pipedrive.com/docs/api/v1)
- [Pipedrive Deals API](https://developers.pipedrive.com/docs/api/v1/Deals)
- [Pipedrive Persons API](https://developers.pipedrive.com/docs/api/v1/Persons)
- [Pipedrive Organizations API](https://developers.pipedrive.com/docs/api/v1/Organizations)
- [Pipedrive Activities API](https://developers.pipedrive.com/docs/api/v1/Activities)
- [Pipedrive Pipelines API](https://developers.pipedrive.com/docs/api/v1/Pipelines)
- [Pipedrive Stages API](https://developers.pipedrive.com/docs/api/v1/Stages)
- [Pipedrive Notes API](https://developers.pipedrive.com/docs/api/v1/Notes)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, SDK snippets, and API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce read and write API call plans and commands; write operations require explicit user confirmation.]

## Skill Version(s):

1.1.0 (source: server release metadata; skill frontmatter version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
