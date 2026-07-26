## Description: <br>
Production-grade WordPress REST API integration for managing posts, pages, media, WooCommerce products, Elementor content, SEO meta, ACF, and JetEngine fields. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[benkalsky](https://clawhub.ai/user/benkalsky) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content operators use this skill to retrieve, draft, create, update, and audit WordPress content through REST APIs on sites where they have explicit credentials. It supports controlled WordPress administration for posts, pages, media, WooCommerce, SEO metadata, custom fields, and pre-sale site audits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live WordPress site content, products, media, SEO metadata, and custom fields. <br>
Mitigation: Use it only for intended WordPress administration, require explicit approval for target site, IDs, fields, status, and final write action, and prefer draft status before publishing. <br>
Risk: Credentialed WordPress and WooCommerce access can expose or modify production data if over-privileged credentials are used. <br>
Mitigation: Use a dedicated low-privilege WordPress user or WooCommerce key, keep credentials in environment variables or a protected local config, and rotate or revoke credentials when no longer needed. <br>
Risk: Batch and seed operations can apply changes across multiple posts or sites. <br>
Mitigation: Run dry-run mode first, review the planned changes, and require explicit execution flags such as --execute, --allow-all, or approved group targeting before applying changes. <br>
Risk: Plaintext HTTP WordPress endpoints can send Basic Auth credentials unencrypted. <br>
Mitigation: Prefer HTTPS for production sites and set WP_REQUIRE_HTTPS=1 when plaintext HTTP should be refused instead of warned. <br>
Risk: Remote media and local file inputs can introduce unsafe reads or fetches if boundaries are relaxed. <br>
Mitigation: Keep local reads scoped with WP_ALLOWED_FILE_ROOTS, require explicit opt-in for remote media URLs, and use the skill's HTTPS-only and private-address blocking behavior for remote fetches. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/benkalsky/skills/wordpress-api-pro) <br>
- [WordPress REST API Reference](references/api-reference.md) <br>
- [Gutenberg Block Format](references/gutenberg-blocks.md) <br>
- [Official WordPress REST API Documentation](https://developer.wordpress.org/rest-api/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration examples, and structured text output from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce dry-run plans, WordPress REST API request results, audit findings, and operational guidance for credentialed WordPress sites.] <br>

## Skill Version(s): <br>
3.8.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
