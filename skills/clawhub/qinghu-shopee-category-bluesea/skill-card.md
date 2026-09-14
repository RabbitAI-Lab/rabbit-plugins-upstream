## Description:

This skill helps agents research Shopee category opportunities with Qinghu data by drilling into first-, second-, and third-level categories, comparing size, growth, concentration, trends, and price distribution to identify lower-competition niches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, sellers, and ecommerce analysts use this skill to evaluate Shopee sites and categories before choosing a new store direction or niche. It supports category-level decisions, including opportunity ranking, saturation checks, site comparison, and price-band recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Qinghu API token for external data access.

Mitigation: Provide the token only through the documented environment variables or direct user input, and avoid exposing it in logs, shared transcripts, or committed files.

Risk: Qinghu API calls may consume paid points.

Mitigation: Require user approval before API calls, report actual Qinghu point usage from the response envelope, and stop when authorization or parameters are unclear.

Risk: The skill is specialized for Shopee category research and may be a poor fit for broader marketplace strategy.

Mitigation: Use it for category-level Shopee decisions, and choose a more specific skill for non-Shopee strategy or product-level selection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-category-bluesea)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise recommendations, optional tables or exported files, and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs usually include top category recommendations, recommended price bands, saturated-category cautions, site advice, and Qinghu point usage when paid API calls run.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
