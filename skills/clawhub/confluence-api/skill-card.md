## Description:

Confluence API integration with managed OAuth for managing pages, spaces, blogposts, comments, attachments, and properties through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Confluence Cloud pages, spaces, blogposts, comments, attachments, and properties via Maton with OAuth-managed access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify Confluence content through Maton.

Mitigation: Use OAuth where possible, choose the narrowest Confluence scopes available, specify the intended connection when multiple accounts exist, and review every proposed write or deletion before approving it.

Risk: Granting Maton access to Confluence can expose workspace content to an external service.

Mitigation: Confirm the user trusts Maton and is comfortable granting Confluence access before installing or connecting an account.

Risk: Long-lived API keys can leak through logs, shell history, process listings, or saved files.

Mitigation: Prefer OAuth; when an API key is unavoidable, keep it out of command arguments and logs, avoid persisting it, and rotate it if exposed.

## Reference(s):

- [ClawHub Confluence Skill](https://clawhub.ai/byungkyu/skills/confluence-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Confluence REST API V2 Documentation](https://developer.atlassian.com/cloud/confluence/rest/v2/intro/)
- [Confluence REST API V2 Reference](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/)
- [Confluence Storage Format](https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and user approval before new connections or modifying Confluence content.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
