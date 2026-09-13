## Description:

TinkerClaw WordPress lets an agent manage WordPress posts, pages, tags, media, and selected administrative endpoints through the WordPress REST API with draft-by-default publishing gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and content teams use this skill to let an agent draft, edit, organize, and inspect WordPress content while requiring explicit consent for publishing and site-administration writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A WordPress application password can expose or modify site content if the account is over-privileged or the destination is misconfigured.

Mitigation: Use a dedicated least-privilege WordPress account, set WP_ALLOWED_HOSTS explicitly, and use WP_READONLY for browsing-only sessions.

Risk: Plugin, theme, user, and settings writes can change site behavior or execute code on the WordPress site.

Mitigation: Avoid admin-capable credentials unless the workflow requires them, and only set WP_ALLOW_ADMIN for an approved action.

Risk: Publishing content can make drafts public before the site owner has reviewed them.

Mitigation: Keep draft-by-default behavior in place and only set WP_ALLOW_PUBLISH after the owner confirms the exact content to publish.

Risk: Optional keychain storage and the optional curl_cffi path have caveats in the security guidance.

Mitigation: Prefer the default curl flow unless those optional paths have been reviewed for the local environment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/globalcaos/skills/wordpress-ultimate)
- [WordPress REST API Quick Reference](artifact/references/wp-api-reference.md)
- [SEO Patterns for WordPress Content](artifact/references/seo-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands, JSON request bodies, and WordPress REST API responses when scripts are executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires WP_URL, WP_USER, and WP_APP_PASSWORD; write operations are gated by per-call control flags.]

## Skill Version(s):

1.3.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
