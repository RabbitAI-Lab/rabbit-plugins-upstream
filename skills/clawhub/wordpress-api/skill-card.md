## Description:

WordPress.com API integration with managed OAuth for managing posts, pages, sites, and content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to connect a WordPress.com account through Maton and manage WordPress.com posts, pages, site metadata, likes, users, and settings. It is suited for agent workflows that need read-first API access with explicit confirmation before account connection or content-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mediate access to a WordPress.com account and perform publishing, editing, liking, settings, or deletion actions.

Mitigation: Default to read and list calls, verify target identifiers and account context, and require explicit user confirmation before creating a connection or running any content-changing request.

Risk: OAuth scopes or the selected connection may grant broader access than the immediate task needs.

Mitigation: Review OAuth scopes and connection choice before use, select the least privilege option available, specify the intended connection when more than one exists, and revoke unused connections.

Risk: API-key mode exposes a long-lived credential more easily than the CLI OAuth flow.

Mitigation: Prefer OAuth through the Maton CLI, avoid printing or persisting API keys, send keys only to api.maton.ai, and rotate the key if exposure is suspected.

Risk: Unpinned CLI or SDK installation can introduce supply-chain drift.

Mitigation: Use pinned or locally isolated package installs where possible and review package sources before installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/wordpress-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [WordPress.com REST API Overview](https://developer.wordpress.com/docs/api/)
- [WordPress.com Getting Started Guide](https://developer.wordpress.com/docs/api/getting-started/)
- [WordPress.com REST API Reference](https://developer.wordpress.com/docs/api/rest-api-reference/)
- [WordPress.com OAuth Authentication](https://developer.wordpress.com/docs/oauth2/)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON examples, and Python or JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized WordPress.com connection.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
