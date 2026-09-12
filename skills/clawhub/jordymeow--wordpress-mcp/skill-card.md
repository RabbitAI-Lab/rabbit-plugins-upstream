## Description:

Manage WordPress sites via MCP (Model Context Protocol) through AI Engine for content editing, SEO analysis, analytics, media management, taxonomy operations, social scheduling, multilingual workflows, and WordPress administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jordymeow](https://clawhub.ai/user/jordymeow)

### License/Terms of Use:


## Use Case:

Developers, site operators, and content teams use this skill to connect an agent to a WordPress site through AI Engine's MCP Server, discover enabled tools, and perform site management workflows such as drafting posts, updating media, auditing SEO, managing translations, and operating WooCommerce features when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent broad administrative control over a configured WordPress site.

Mitigation: Install only for sites where agent administration is acceptable, use least-privilege and revocable tokens, and keep optional high-impact feature groups disabled unless needed.

Risk: The artifact recommends storing bearer-token connection details in TOOLS.md, which can expose powerful credentials if stored insecurely.

Mitigation: Avoid storing real tokens in plaintext shared files; use secure secret storage or temporary tokens when possible.

Risk: Enabled tools can delete content, issue refunds, write SQL, edit plugins or themes, publish public content, or change site-wide configuration.

Mitigation: Require explicit human review before destructive actions, refunds, SQL writes, plugin or theme edits, public posting, and site-wide configuration changes.

## Reference(s):

- [WordPress MCP Skill Page](https://clawhub.ai/jordymeow/skills/wordpress-mcp)
- [AI Engine WordPress Plugin](https://wordpress.org/plugins/ai-engine/)
- [SEO Engine WordPress Plugin](https://wordpress.org/plugins/seo-engine/)
- [Feature Tools Reference](references/features.md)
- [Core WordPress Tools Reference](references/core-tools.md)
- [Developer Tools Reference](references/dev-tools.md)
- [SEO Engine Tools Reference](references/seo-tools.md)
- [WooCommerce Tools Reference](references/woocommerce-tools.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-RPC examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool availability is site-specific; agents should run tools/list before using WordPress MCP tools.]

## Skill Version(s):

3.3.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
