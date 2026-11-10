## Description:

Collects Taobao product details, customer reviews, and shop listings through a paid data API, with pagination and JSON response saving.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT

## Use Case:

External sellers, analysts, and developers use the skill to retrieve Taobao product attributes, reviews, and shop listings for product selection analysis, review insights, and catalog monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports a benign verdict with medium confidence and partial coverage, noting undeclared tool scope and environment-derived file writes.

Mitigation: Review commands and local file writes before execution, protect the API key, and confirm runtime permissions.

Risk: Data collection calls deduct platform points, and empty pages may still be charged.

Mitigation: Check the live prices and balance first, limit pages and batch size, and stop when a page is empty.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cuiyunhai/skills/taobao-shop-data)
- [Data API platform](https://zlh.aidata366.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration guidance]

**Output Format:** [JSON API responses and Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are paginated; collection endpoints are metered.]

## Skill Version(s):

1.0.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
