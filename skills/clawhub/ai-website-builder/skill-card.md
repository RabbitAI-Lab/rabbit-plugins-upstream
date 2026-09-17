## Description:

AI建站助手 helps agents create, modify, migrate, and troubleshoot SaaS websites by generating page code and, with user-supplied MCP credentials, querying or writing site content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hsqduron](https://clawhub.ai/user/hsqduron)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and agents use this skill to plan SaaS websites, generate editable HTML/CSS/JavaScript and Twig-style templates, connect pages to site data, and manage website content through a user-authorized MCP service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can grant broad site-management and raw database capabilities when connected to a live SaaS site.

Mitigation: Use a limited token when available, verify the target site before each session, and require explicit confirmation before writes, deletes, uploads, SQL changes, cache clears, or homepage changes.

Risk: Generated pages, forms, uploads, and structured data can introduce privacy, SEO, or content accuracy issues if published without review.

Mitigation: Review generated pages before publication, especially form privacy notices, uploaded assets, SEO metadata, and JSON-LD fields.

Risk: The artifact includes an unconditional trial-registration prompt that may be irrelevant to some deployments.

Mitigation: Remove or ignore the registration prompt when it does not apply to the target site or user workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hsqduron/skills/ai-website-builder)
- [Yunzhi trial site registration](https://www.72e.net/autoweb/edition.aspx)
- [AIPage.md](references/AIPage.md)
- [advanced-data-interface.md](references/advanced-data-interface.md)
- [customform-democode-base.md](references/customform-democode-base.md)
- [FAQ.md](references/FAQ.md)
- [mcp-tools.md](references/mcp-tools.md)
- [online_query_democode.html](references/online_query_democode.html)
- [product-enquiry.md](references/product-enquiry.md)
- [product-enquiry-democode.md](references/product-enquiry-democode.md)
- [website-common-pages.md](references/website-common-pages.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with HTML/CSS/JavaScript, Twig template code, MCP operation plans, and confirmation prompts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Online read/write workflows require a user-provided MCP address and Bearer token; destructive writes, SQL changes, uploads, cache clears, and homepage changes require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
