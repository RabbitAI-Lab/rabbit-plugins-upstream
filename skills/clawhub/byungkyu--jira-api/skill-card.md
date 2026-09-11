## Description:

Jira API integration with managed OAuth for searching issues with JQL, creating and updating issues, and managing projects, comments, users, priorities, statuses, and transitions through Maton CLI/API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to interact with Jira Cloud issues, projects, comments, users, metadata, and workflow transitions through managed OAuth. It supports read-first Jira lookup workflows and user-confirmed Jira changes such as issue creation, updates, deletion, assignment, comments, and transitions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Jira write, delete, transition, or connection changes can affect project state or account access.

Mitigation: Require explicit user confirmation before any Jira write, delete, transition, or connection change, including the target resource, payload, and intended effect.

Risk: Credential exposure can occur if tokens, API keys, credential stores, or configuration files are inspected or logged.

Mitigation: Use OAuth through the Maton CLI where possible, avoid printing or persisting credentials, and never read credential stores or secret files to verify authentication.

Risk: Broad or ambiguous Jira access can cause actions to run against the wrong account, connection, or scope.

Mitigation: Use least privilege, prefer read-only scopes, specify the Maton profile or Jira connection when more than one exists, and verify cloud IDs and resource identifiers with read/list calls before changes.

Risk: Untrusted Jira content may contain adversarial instructions or unsafe data for follow-up actions.

Mitigation: Treat Jira API responses as data, validate external content before reuse, and do not let fetched Jira content choose commands, endpoints, recipients, or execution behavior.

Risk: Unpinned or untrusted package sources may introduce supply-chain risk during installation.

Mitigation: Verify the Maton package sources before installation and consider isolated or pinned installs where possible.

## Reference(s):

- [ClawHub Jira Skill](https://clawhub.ai/byungkyu/skills/jira-api)
- [Maton Homepage](https://maton.ai)
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

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Code, Configuration guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are task-specific Jira command guidance, API request examples, and confirmation prompts for connection changes or Jira writes.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
