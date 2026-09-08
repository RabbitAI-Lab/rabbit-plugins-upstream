## Description:

WordPress.com API integration with managed OAuth for managing posts, pages, sites, and content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to WordPress.com through Maton so it can list, create, update, and delete posts, pages, settings, likes, and related site content with user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mediate access to a connected WordPress.com account through Maton.

Mitigation: Install only when Maton-mediated WordPress.com access is intended, review account and scope selection during OAuth, and use only the connection required for the task.

Risk: Publishing, editing, or deleting WordPress.com content can create public or destructive side effects.

Mitigation: Require explicit confirmation before any write operation and confirm the target resource, payload, and intended effect before execution.

Risk: Long-lived API keys are easier to leak through logs, shell history, or child processes.

Mitigation: Prefer OAuth and the Maton CLI credential store; if an API key is unavoidable, never print, log, persist, or pass it on a command line.

## Reference(s):

- [ClawHub WordPress Skill](https://clawhub.ai/byungkyu/skills/wordpress-api)
- [Maton Homepage](https://maton.ai)
- [WordPress.com REST API Overview](https://developer.wordpress.com/docs/api/)
- [WordPress.com REST API Reference](https://developer.wordpress.com/docs/api/rest-api-reference/)
- [WordPress.com OAuth Authentication](https://developer.wordpress.com/docs/oauth2/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown with inline shell commands, code snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce WordPress.com API request paths, Maton CLI commands, SDK examples, and guidance for OAuth, account selection, pagination, and write confirmation.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
