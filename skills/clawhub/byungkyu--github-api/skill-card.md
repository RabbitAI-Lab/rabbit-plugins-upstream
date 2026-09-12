## Description:

GitHub API integration with managed OAuth for accessing repositories, issues, pull requests, commits, branches, and users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect and manage GitHub repositories, issues, pull requests, branches, commits, releases, and users through Maton-managed OAuth. It is suited to GitHub automation where read/list operations are preferred and write operations require explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitHub account access is brokered through Maton, so misuse or misplaced trust in that gateway could expose repository data or account actions.

Mitigation: Install only when Maton is trusted for the target GitHub account, prefer OAuth, and grant only the scopes needed for the task.

Risk: Write, delete, merge, or connection-creation operations can modify GitHub state or grant access beyond the current task.

Mitigation: Default to read/list calls, verify exact resource identifiers and connection IDs, and require explicit user approval before any POST, PUT, PATCH, DELETE, merge, or new connection.

Risk: Long-lived API keys or provider-issued tokens can leak through logs, shell history, files, or child process environments.

Mitigation: Use OAuth where possible, keep credentials in the operating system credential store, avoid printing or persisting tokens, and rotate any key that was exposed.

Risk: GitHub API responses and repository content may contain untrusted instructions or data.

Mitigation: Treat fetched content as data, avoid executing or interpolating it into shell commands, and let the user's task determine follow-up endpoints and actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/github-api)
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

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON snippets, API paths, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are task-scoped guidance for using Maton CLI or HTTPS calls against GitHub; write operations require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
