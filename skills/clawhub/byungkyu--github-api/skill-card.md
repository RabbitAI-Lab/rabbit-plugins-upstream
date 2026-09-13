## Description:

GitHub API integration with managed OAuth for accessing repositories, issues, pull requests, commits, branches, users, code search, and workflow automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to inspect and manage GitHub repositories, issues, pull requests, branches, commits, users, and code search through Maton-managed OAuth. It also provides guidance for user-approved hosted functions and triggers when a GitHub workflow needs automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitHub OAuth or API key access can expose repositories, issues, pull requests, and other account data through the Maton connection.

Mitigation: Prefer OAuth, grant only the scopes needed for the task, and install only if Maton is trusted as the account intermediary.

Risk: Write, delete, merge, hosted function, trigger, or replay operations can make persistent or irreversible changes.

Mitigation: Default to read/list operations and require explicit user confirmation for every write, new connection, automation step, and destructive action.

Risk: Trigger destinations and event watch handlers can forward sensitive event payloads or execute local handler code.

Mitigation: Use only destinations the user controls and approves, review payloads and handler code before use, and avoid --exec unless the local script has been reviewed.

## Reference(s):

- [ClawHub GitHub Skill](https://clawhub.ai/byungkyu/skills/github-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [GitHub REST API Documentation](https://docs.github.com/en/rest)
- [GitHub Repositories API](https://docs.github.com/en/rest/repos/repos)
- [GitHub Issues API](https://docs.github.com/en/rest/issues/issues)
- [GitHub Pull Requests API](https://docs.github.com/en/rest/pulls/pulls)
- [GitHub Search API](https://docs.github.com/en/rest/search/search)
- [GitHub Rate Limits](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)
- [GitHub Trigger Reference](references/github/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with inline bash, JSON, Python, and raw HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should default to read/list operations and request explicit user approval for writes, new connections, hosted functions, triggers, and destructive actions.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
