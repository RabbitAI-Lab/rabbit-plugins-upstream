## Description:

WordPress.com API integration with managed OAuth for managing posts, pages, sites, and content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to WordPress.com through Maton-managed OAuth, inspect account and site data, and create, update, or delete posts, pages, and site content after user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing Maton brokers access to WordPress.com content through the user's connection.

Mitigation: Approve each connection and write action separately, use the narrowest available authorization scope, and default to read or list calls before changing content.

Risk: Hosted functions and triggers can automate ongoing access or persistent data forwarding.

Mitigation: Use only user-authored or user-reviewed handlers, keep function network policy at DENY_ALL when possible, and require explicit approval for each trigger, destination, and transmitted field set.

Risk: Raw HTTP or long-lived API key workflows can expose credentials if used casually.

Mitigation: Prefer OAuth through the Maton CLI and operating-system credential storage; use raw HTTP with MATON_API_KEY only when the CLI cannot be installed.

## Reference(s):

- [WordPress.com REST API Overview](https://developer.wordpress.com/docs/api/)
- [WordPress.com API Reference](https://developer.wordpress.com/docs/api/rest-api-reference/)
- [WordPress.com OAuth Authentication](https://developer.wordpress.com/docs/oauth2/)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-approved WordPress.com authorization.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
