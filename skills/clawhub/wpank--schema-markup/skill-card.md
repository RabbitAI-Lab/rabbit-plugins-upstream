## Description:

Add, fix, or optimize schema markup and structured data for pages that need JSON-LD, schema.org types, rich snippets, FAQ schema, product schema, review schema, or breadcrumb schema.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wpank](https://clawhub.ai/user/wpank)

### License/Terms of Use:


## Use Case:

Developers, site owners, and SEO practitioners use this skill to add, audit, and fix schema.org structured data for static sites, React/Next.js applications, and CMS or WordPress pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provided React JSON-LD pattern can be unsafe if schema data comes from users, CMS fields, products, reviews, or databases.

Mitigation: Use an HTML-safe JSON serializer or escape <, >, &, U+2028, and U+2029 before embedding JSON-LD.

Risk: Mutable remote install commands can install different content over time.

Mitigation: Prefer a pinned installer or reviewed commit, and review the skill before installing.

## Reference(s):

- [Schema Markup Examples](references/schema-examples.md)
- [Schema.org](https://schema.org)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)
- [ClawHub Skill Page](https://clawhub.ai/wpank/skills/schema-markup)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON, TSX, and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes validation checklists, schema.org property guidance, and implementation examples.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
