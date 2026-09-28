## Description:

GitHub API integration with managed OAuth for accessing repositories, issues, pull requests, commits, branches, users, and related automation through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with GitHub repositories, issues, pull requests, commits, branches, users, search, and event-driven workflows through a Maton-managed connection. It is suited for read-first repository operations and carefully approved writes or automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act through a Maton-connected GitHub account and may reach sensitive repository data or perform write actions.

Mitigation: Use OAuth where possible, authorize only the repositories and scopes needed for the task, default to read/list calls, and confirm every write or new connection with the user.

Risk: Functions, triggers, and persistent destinations can continue acting on future GitHub events after setup.

Mitigation: Review each function or trigger before creation, get separate approval for persistent destinations, scope automation narrowly, and remove unused automations or connections when the task is complete.

Risk: Raw API-key use can expose a long-lived Maton credential if printed, logged, persisted, or passed through child processes.

Mitigation: Prefer OAuth and the Maton CLI credential store; use raw HTTP with MATON_API_KEY only when the CLI cannot be installed, and never print, log, persist, or pass the key on a command line.

Risk: Event payloads and API responses can contain untrusted or personal data.

Mitigation: Treat fetched content as data, extract only fields needed for the task, avoid logging raw responses, and never execute or interpolate third-party payload content into shell commands or code.

## Reference(s):

- [GitHub REST API Documentation](https://docs.github.com/en/rest)
- [Repositories API](https://docs.github.com/en/rest/repos/repos)
- [Issues API](https://docs.github.com/en/rest/issues/issues)
- [Pull Requests API](https://docs.github.com/en/rest/pulls/pulls)
- [Search API](https://docs.github.com/en/rest/search/search)
- [GitHub Rate Limits](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include GitHub API responses; the skill requires network access, a Maton account, and task-specific user approval for writes, new connections, functions, triggers, or persistent destinations.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
