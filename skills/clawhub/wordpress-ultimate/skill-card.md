## Description:

TinkerClaw WordPress lets an agent manage WordPress content through REST API shell helpers, with draft-by-default posting, explicit publish and admin gates, host allowlisting, and media upload support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and content teams use this skill to let an agent draft, edit, organize, publish, and upload WordPress content through the WordPress REST API while requiring explicit approval for publishing and site-administration writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential handling and consent gates have gaps that should be reviewed before granting WordPress site access.

Mitigation: Use a dedicated least-privilege WordPress account with a revocable application password, keep credentials in an owner-only WP_ENV_FILE, and review or fix the scripts before relying on high-impact consent gates.

Risk: The skill can perform high-impact WordPress operations allowed by the configured account, including publishing content and administrative plugin, theme, user, or settings writes.

Mitigation: Set WP_ALLOWED_HOSTS explicitly, keep WP_READONLY enabled when only reading, and avoid WP_ALLOW_PUBLISH or WP_ALLOW_ADMIN unless the specific change has been deliberately approved.

Risk: Installing or activating WordPress plugins runs code on the target site.

Mitigation: Treat plugin and theme changes as site-administration actions, use WP_ALLOW_ADMIN only for reviewed operations, and prefer a constrained WordPress account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/wordpress-ultimate)
- [WordPress REST API Quick Reference](references/wp-api-reference.md)
- [SEO Patterns for WordPress Content](references/seo-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, HTML/Gutenberg examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May print WordPress REST API JSON responses from helper scripts; no separate post-processing contract is declared.]

## Skill Version(s):

1.3.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
