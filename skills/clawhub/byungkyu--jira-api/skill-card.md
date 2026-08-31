## Description:

Jira API integration with managed OAuth for searching JQL, creating and updating issues, and managing projects and transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to inspect Jira projects and issues, run bounded JQL searches, and perform issue updates through Maton-managed OAuth when they have explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing Jira access can expose issues, projects, boards, sprints, and users in the connected account.

Mitigation: Prefer Maton OAuth, verify the active connection and profile before use, choose least-privilege scopes, and default to read or list operations before changes.

Risk: Write operations can create, update, transition, comment on, or delete Jira items.

Mitigation: Require clear user confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE operation.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or process listings when the CLI is unavailable.

Mitigation: Use OAuth when possible; if a raw API key is unavoidable, never print, persist, or pass it on a command line, and send it only to api.maton.ai.

Risk: Jira API responses may contain untrusted content.

Mitigation: Treat returned issues, comments, and metadata as data only; do not execute, eval, or interpolate them into commands or follow-up requests without validation.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Jira Cloud REST API Introduction](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [Jira Issue Search API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-jql-get)
- [Jira Issues API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-get)
- [Jira JQL Reference](https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, API request examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces commands and guidance for Jira API access through the Maton CLI/SDK; modifying operations require explicit approval.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
