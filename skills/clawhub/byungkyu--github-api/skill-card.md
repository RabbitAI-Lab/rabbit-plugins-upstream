## Description:

GitHub API integration with managed OAuth for accessing repositories, issues, pull requests, commits, branches, users, and related workflow automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to inspect and manage GitHub repositories, issues, pull requests, commits, branches, users, and searches through Maton-managed OAuth access. It is suited to agent workflows that need GitHub API calls while preserving explicit approval for new connections and write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitHub actions are routed through Maton and may require granting GitHub OAuth scopes.

Mitigation: Install only when this routing model is acceptable, prefer least-privilege or read-only scopes, and grant only the scopes needed for the current task.

Risk: Write operations can modify or delete GitHub resources such as repositories, branches, issues, pull requests, releases, collaborators, or repository contents.

Mitigation: Default to read or list calls, confirm the exact target account, repository, connection, payload, and reversibility before any create, update, merge, transfer, or delete operation.

Risk: The raw API-key fallback uses a long-lived Maton API key that can leak through environment exposure, logs, shell history, or persisted files.

Mitigation: Prefer OAuth through the Maton CLI, use the raw API-key path only when the CLI cannot be installed, never print or persist the key, and rotate it if exposed.

Risk: Content returned from GitHub may contain untrusted or adversarial instructions.

Mitigation: Treat API responses as data, avoid executing returned content, and keep endpoint selection and follow-up actions under the user's explicit task context.

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
- [GitHub REST API Rate Limits](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and optional Python or JavaScript code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide Maton CLI, SDK, or raw HTTPS calls; GitHub API responses may be JSON.]

## Skill Version(s):

1.2.0 (source: server release metadata; frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
