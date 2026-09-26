## Description:

Jira API integration with managed OAuth for searching issues with JQL, creating and updating issues, managing projects, and transitioning Jira workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support teams use this skill to work with Jira Cloud issues, projects, comments, users, and workflow transitions through a Maton-managed Jira connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton-mediated Jira access can read or modify resources allowed by the selected Jira connection.

Mitigation: Confirm the Jira account, connection, and cloud ID before use; default to read/list operations and require explicit user approval for any write.

Risk: Function, trigger, destination, delete, and raw API-key workflows can create persistent automation, remove access, or expose long-lived credentials if used carelessly.

Mitigation: Review the exact target, payload, destination host, and persistence behavior before running these workflows; prefer OAuth through the Maton CLI and remove unused connections or automation.

## Reference(s):

- [Jira API Introduction](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [Search Issues (JQL)](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-jql-get)
- [Create Issue](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post)
- [Transition Issue](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-transitions-post)
- [JQL Reference](https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Time trigger catalog](references/time/triggers.md)
- [GitHub trigger catalog](references/github/triggers.md)
- [Google Mail trigger catalog](references/google-mail/triggers.md)
- [Slack trigger catalog](references/slack/triggers.md)
- [Stripe trigger catalog](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Jira Cloud connection; write actions require explicit user confirmation.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
