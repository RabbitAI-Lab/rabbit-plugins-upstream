## Description:

Jira API integration with managed OAuth for searching issues with JQL, creating and updating issues, managing projects and transitions, and configuring approved Jira-related automation through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Jira Cloud issues, projects, workflows, boards, sprints, and users from an agent session through an authenticated Maton connection. It supports routine Jira reads and approved writes, plus user-approved hosted functions and triggers for Jira-related automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Jira writes, connection changes, and automation setup can modify business data or create persistent behavior under the user's connected account.

Mitigation: Default to read and list operations, and require explicit user confirmation for connection creation, POST, PUT, PATCH, DELETE, hosted function deployment, trigger creation, and trigger destination changes.

Risk: OAuth tokens or API keys could be exposed if raw credentials are printed, exported, logged, or stored outside the credential manager.

Mitigation: Prefer Maton OAuth through the CLI, use the narrowest Jira scopes available, avoid raw API keys unless the CLI cannot be used, and rotate any key that was exposed.

Risk: Trigger destinations can forward future event data continuously, including personal or sensitive data from connected sources.

Mitigation: Review the destination host, payload fields, persistence, and credential handling before creation; prefer platform-controlled destinations and delete destinations that are no longer needed.

Risk: Hosted functions run with the deploying Maton account's identity and can access the account's approved connections.

Mitigation: Use user-authored or user-reviewed handlers, deploy Jira functions with DENY_ALL network policy unless a specific exception is approved, and summarize reachable connections before deployment or invocation.

## Reference(s):

- [ClawHub Jira Skill](https://clawhub.ai/byungkyu/skills/jira-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Jira API Introduction](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [Jira Search Issues with JQL](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-jql-get)
- [Jira Get Issue](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-get)
- [Jira Create Issue](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post)
- [Jira Transition Issue](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-transitions-post)
- [JQL Reference](https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated API calls, connection setup, hosted functions, or trigger configuration; write actions and automation setup require user approval.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
