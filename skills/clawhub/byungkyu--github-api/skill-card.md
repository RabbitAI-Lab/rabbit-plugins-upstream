## Description:

GitHub API integration with managed OAuth for accessing repositories, issues, pull requests, commits, branches, and users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to interact with GitHub repositories, issues, pull requests, code search, commits, branches, users, and approved automation through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party Maton CLI and OAuth gateway that operate with the GitHub account and scopes the user authorizes.

Mitigation: Install only when the user accepts that trust boundary, prefer OAuth over long-lived API keys, choose read-only and least-privilege scopes where possible, and verify CLI package provenance before global installation.

Risk: Write operations and GitHub automation can change repositories, issues, pull requests, branches, or downstream workflows.

Mitigation: Default to read/list calls, require explicit user confirmation for every write, new connection, function, trigger, destination, deploy, or invocation, and show the target resource and intended effect before execution.

Risk: Persistent trigger destinations can continuously forward event data outside the platform if configured to a third-party host.

Mitigation: Keep destinations on api.maton.ai or *.maton.app unless the user names and trusts a specific host, disclose the payload and persistence, and avoid trigger destinations unless the user explicitly requested them.

## Reference(s):

- [GitHub REST API Documentation](https://docs.github.com/en/rest)
- [Repositories API](https://docs.github.com/en/rest/repos/repos)
- [Issues API](https://docs.github.com/en/rest/issues/issues)
- [Pull Requests API](https://docs.github.com/en/rest/pulls/pulls)
- [Search API](https://docs.github.com/en/rest/search/search)
- [GitHub REST API Rate Limits](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code, API calls]

**Output Format:** [Markdown with inline bash, JSON, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authenticated GitHub connection; defaults to read/list calls with explicit approval for writes and automation.]

## Skill Version(s):

1.2.2 (source: release evidence; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
