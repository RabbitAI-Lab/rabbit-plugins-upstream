## Description:

Pipedrive API integration with managed OAuth for managing deals, persons, organizations, activities, and pipelines in Pipedrive CRM.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, sales operations teams, and agents use this skill to read and manage Pipedrive CRM records through Maton-authenticated API calls. It supports CRM lookups, approved record changes, connection management, and optional user-approved automation around Pipedrive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pipedrive writes or deletions can modify or remove CRM records.

Mitigation: Default to read and list operations, and review each requested write or deletion with the user before approving it.

Risk: Long-lived API keys can expose account access if copied into environment variables or logs.

Mitigation: Prefer OAuth through Maton and use the operating system credential store; use API keys only when needed and avoid dumping raw responses or credentials.

Risk: Triggers and destinations create persistent data flows from connected services.

Mitigation: Create triggers only after explicit approval, scope event sources narrowly, and send events only to hosts the user controls or has approved.

## Reference(s):

- [ClawHub Pipedrive Skill](https://clawhub.ai/byungkyu/skills/pipedrive-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Pipedrive API Overview](https://developers.pipedrive.com/docs/api/v1)
- [Pipedrive Deals API](https://developers.pipedrive.com/docs/api/v1/Deals)
- [Pipedrive Persons API](https://developers.pipedrive.com/docs/api/v1/Persons)
- [Pipedrive Organizations API](https://developers.pipedrive.com/docs/api/v1/Organizations)
- [Pipedrive Activities API](https://developers.pipedrive.com/docs/api/v1/Activities)
- [Time Trigger Reference](references/time/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, JSON]

**Output Format:** [Markdown with bash, Python, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an approved Pipedrive connection.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
