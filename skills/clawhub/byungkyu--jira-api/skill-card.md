## Description:

Helps agents search and manage Jira Cloud issues, projects, and workflows through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Jira users and developers use this skill to find issues with JQL, manage issues and projects, and propose user-approved workflow automations through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Jira writes could change or delete data in the connected account.

Mitigation: Prefer read-only scopes and confirm the target and effect before every write.

Risk: Hosted automations can continue to act after initial setup.

Mitigation: Require explicit approval for setup and remove unused connections, functions, and triggers.

Risk: Trigger destinations can forward event data to third-party hosts.

Mitigation: Approve each destination separately, verify its exact host, and delete it when no longer needed.

## Reference(s):

- [Jira skill release](https://clawhub.ai/byungkyu/skills/jira-api)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Jira Cloud REST API introduction](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [JQL reference](https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command, API, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Jira responses and proposed actions depend on the connected account's permissions.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release; artifact metadata says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
