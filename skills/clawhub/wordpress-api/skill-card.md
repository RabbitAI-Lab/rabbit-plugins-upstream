## Description:

Helps agents manage WordPress.com posts, pages, and site content through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

WordPress.com site owners and their agents use this skill to inspect and manage posts, pages, and site content, with approval before changes or automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connection grants access to WordPress.com account content, and writes can publish, change, or delete it.

Mitigation: Start with read-only checks, limit authorization to the needed account and scopes, and obtain explicit approval for every write.

Risk: Functions, triggers, and destinations can continue acting or forwarding data after setup.

Mitigation: Require explicit approval for automation and review its function, trigger, and destination before enabling it.

Risk: API-key authentication can expose a long-lived credential if mishandled.

Mitigation: Prefer device login and use API-key mode only when necessary; do not disclose or store credentials in commands or destinations.

## Reference(s):

- [ClawHub WordPress.com skill release](https://clawhub.ai/byungkyu/skills/wordpress-api)
- [Maton](https://maton.ai)
- [WordPress.com REST API documentation](https://developer.wordpress.com/docs/api/)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with CLI commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-authorized WordPress.com connection and network access.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
