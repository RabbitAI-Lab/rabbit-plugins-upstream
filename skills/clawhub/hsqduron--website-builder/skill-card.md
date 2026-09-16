## Description:

This skill helps agents create, modify, and troubleshoot SaaS website pages, including static sections, HTML/CSS/JS pages, Twig-style dynamic templates, website data access, custom forms, product enquiries, online queries, and site content updates through a user-provided MCP service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hsqduron](https://clawhub.ai/user/hsqduron)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, website operators, and agents use this skill to plan SaaS websites, generate editable page code, connect pages to site data, and manage website content after the user supplies site-scoped MCP credentials. It is intended for building and maintaining business websites, landing pages, forms, product pages, enquiry flows, and related CMS-backed pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad live website and database mutations through a site-scoped MCP token.

Mitigation: Install only when the operator is comfortable granting that access, require explicit confirmation before write, delete, upload, cache, homepage, URL, or database changes, and verify the target site and object IDs before execution.

Risk: Security evidence flags deceptive product-rating metadata guidance.

Mitigation: Require the publisher or operator to remove fabricated rating guidance and ensure structured data reflects real, supportable page content before deployment.

Risk: Remote URL imports for files or product images can expose the MCP backend to unsafe fetch behavior if backend protections are insufficient.

Mitigation: Avoid remote sourceUrl imports unless the backend has SSRF protections; prefer reviewed local uploads or trusted asset sources.

Risk: Generated form and online-query code can collect user data and run custom JavaScript.

Mitigation: Review privacy notices, field handling, validation, upload behavior, and JavaScript encoding before publishing forms or query pages.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/hsqduron/skills/website-builder)
- [AI Free Page Data Calling Guide](references/AIPage.md)
- [Website MCP Tool Reference](references/mcp-tools.md)
- [Advanced Data Interface Documentation](references/advanced-data-interface.md)
- [Custom Form Base Example](references/customform-democode-base.md)
- [Product Enquiry Guide](references/product-enquiry.md)
- [Product Enquiry Complete Example](references/product-enquiry-democode.md)
- [Online Query Example](references/online_query_democode.html)
- [Common Website Pages Guide](references/website-common-pages.md)
- [Website Builder FAQ](references/FAQ.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML, CSS, JavaScript, Twig-style templates, JSON-LD, MCP tool-call instructions, and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include live-site write proposals that require user confirmation and site-scoped MCP credentials before execution.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
