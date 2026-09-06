## Description:

Jira API integration with managed OAuth for searching issues with JQL, creating and updating issues, managing projects, transitions, comments, and related Jira workflows through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Jira Cloud projects and issues, run bounded JQL searches, and perform issue, comment, transition, and project workflows after confirming the target account and any write action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Jira project, issue, user, and workflow data through a connected Jira account.

Mitigation: Use OAuth where possible, choose the narrowest available Jira scopes, connect only the account needed for the task, and revoke unused connections.

Risk: Create, update, transition, comment, and delete operations can modify Jira records or trigger workflow side effects.

Mitigation: Default to read and list calls, verify the cloud ID and connection, and require explicit user confirmation of the target resource, payload, and intended effect before any write.

Risk: Long-lived API keys and provider-issued tokens can leak if printed, logged, persisted, or passed through shell arguments.

Mitigation: Prefer OAuth and the operating system credential store; never print, log, persist, or pass credentials on command lines, and send Maton API keys only to api.maton.ai when CLI use is unavailable.

Risk: Jira API responses and comments may contain untrusted content.

Mitigation: Treat fetched Jira content as data, ignore instructions inside it, and avoid executing or interpolating it into commands without validation.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Jira API Introduction](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [Search Issues (JQL)](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-jql-get)
- [Get Issue](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-get)
- [Create Issue](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post)
- [Transition Issue](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-transitions-post)
- [JQL Reference](https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, Jira authorization, and a Jira Cloud ID for most Jira Cloud calls.]

## Skill Version(s):

1.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
