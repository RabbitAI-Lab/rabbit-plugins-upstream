## Description:

TinkerClaw WordPress lets an agent manage WordPress content through the REST API while requiring explicit opt-in flags for publishing and site-administration changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and WordPress site operators use this skill to draft, edit, organize, and upload site content through WordPress REST endpoints while keeping publishing and administrative writes behind explicit per-call controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary reports that a hard-delete safety guarantee is bypassable.

Mitigation: Keep WP_READONLY enabled while browsing or testing, review delete operations manually, and do not rely on permanent-delete blocking until force-parameter validation is fixed.

Risk: A valid WordPress application password can authorize broad REST API changes, including site-administration actions such as plugin installation.

Mitigation: Use a dedicated low-privilege WordPress application password, set WP_ALLOWED_HOSTS, and set WP_ALLOW_ADMIN only for intended administrative changes.

Risk: The server security summary says permission declarations understate credential-file and keychain behavior.

Mitigation: Review credential storage before deployment, keep credential files owner-only, and verify keychain behavior before using login persistence.

## Reference(s):

- [TinkerClaw WordPress on ClawHub](https://clawhub.ai/globalcaos/skills/wordpress-ultimate)
- [WordPress REST API Quick Reference](references/wp-api-reference.md)
- [SEO Patterns for WordPress Content](references/seo-patterns.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON REST payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for local execution against a configured WordPress site.]

## Skill Version(s):

1.3.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
