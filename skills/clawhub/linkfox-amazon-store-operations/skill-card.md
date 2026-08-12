## Description:

LinkFox Amazon Store Operations helps agents run Amazon SP-API store workflows for authorization, orders, listings, pricing, catalog lookup, reports, feeds, customer feedback, uploads, and A+ Content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and developers use this skill to manage Seller Central workflows through LinkFox, including store authorization, order handling, listing changes, pricing checks, report downloads, feed uploads, customer feedback review, file uploads, and A+ Content management.

### Deployment Geography for Use:

Amazon marketplaces supported by the skill, including United States, United Kingdom, Germany, Japan, France, Italy, and Spain.

## Known Risks and Mitigations:

Risk: The skill can access sensitive Amazon seller operations and data, including orders, reports, listings, feeds, uploads, A+ Content, and buyer or address data.

Mitigation: Install only when this level of Amazon seller access is acceptable, and confirm seller, marketplace, and authorization context before use.

Risk: Full API responses may be saved locally, and inline output can expose sensitive data in the agent transcript.

Mitigation: Avoid inline output for sensitive results and delete local LinkFox session files when they are no longer needed.

Risk: A changed LINKFOX_TOOL_GATEWAY value could route requests somewhere unexpected.

Mitigation: Review the configured LINKFOX_TOOL_GATEWAY endpoint before running the skill.

Risk: Write operations can change Amazon seller account state, including listings, feeds, shipments, uploads, and A+ Content.

Mitigation: Require explicit user confirmation of key parameters before write operations and review returned submission, feed, report, or processing identifiers.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-operations)
- [Quick Start](references/quick-start.md)
- [Authorization Flow](references/authorization-flow.md)
- [Amazon Store Auth](references/linkfox-amazon-store-auth.md)
- [Orders](references/linkfox-amazon-store-orders.md)
- [Listings](references/linkfox-amazon-store-listings.md)
- [Pricing](references/linkfox-amazon-store-pricing.md)
- [Catalog](references/linkfox-amazon-store-catalog.md)
- [Reports](references/linkfox-amazon-store-report.md)
- [Report Types](references/report-types.md)
- [Feeds](references/linkfox-amazon-store-feeds.md)
- [Customer Feedback](references/linkfox-amazon-store-customer-feedback.md)
- [Uploads](references/linkfox-amazon-store-uploads.md)
- [A+ Content](references/linkfox-amazon-store-aplus-content.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts may save full API responses under the working directory and summarize large responses unless inline output is requested.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
