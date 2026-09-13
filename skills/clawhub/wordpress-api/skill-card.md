## Description:

WordPress.com API integration with managed OAuth for managing posts, pages, sites, and content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with WordPress.com content through Maton-managed OAuth, including reading, creating, updating, and deleting posts, pages, site metadata, and settings after user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional hosted-function automation can run with the deploying Maton account's broader access.

Mitigation: Use direct maton api calls for ordinary work; deploy hosted functions only when explicitly requested, from an account with only the needed WordPress connection, with reviewed handlers and DENY_ALL network policy.

Risk: WordPress writes, deletes, and new connections can modify content or authorize access.

Mitigation: Default to read and list operations, require explicit user confirmation for POST, PUT, PATCH, DELETE, and connection creation, and revoke unused connections promptly.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key when the CLI cannot be installed.

Mitigation: Prefer OAuth through the Maton CLI; if raw HTTP is necessary, keep the key in the environment only, never log or print it, send it only to api.maton.ai, and rotate it if exposed.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/byungkyu/skills/wordpress-api)
- [Maton Homepage](https://maton.ai)
- [WordPress.com REST API Overview](https://developer.wordpress.com/docs/api/)
- [WordPress.com Getting Started Guide](https://developer.wordpress.com/docs/api/getting-started/)
- [WordPress.com REST API Reference](https://developer.wordpress.com/docs/api/rest-api-reference/)
- [WordPress.com OAuth Authentication](https://developer.wordpress.com/docs/oauth2/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell, JSON, and Python snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an active WordPress.com connection; write actions and new connections require user confirmation.]

## Skill Version(s):

1.2.2 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
