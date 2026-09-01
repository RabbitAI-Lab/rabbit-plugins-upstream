## Description:

Helps agents analyze Shopee category opportunities with Qinghu data by drilling from level-one to level-three categories and comparing category scale, growth, competition, trends, and price distribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and agent users use this skill to choose Shopee sites and categories, compare market capacity and competition, and identify high-growth low-competition level-three category opportunities. It produces concise category recommendations, price-band guidance, saturation warnings, and exported detail files when result sets are large.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Qinghu API token for data access.

Mitigation: Use only intended Qinghu credentials, avoid sharing tokens in chat when an environment variable is available, and rotate or revoke tokens if exposed.

Risk: Qinghu data calls may consume paid credits.

Mitigation: Obtain user authorization before calls, report actual Qinghu credit consumption from the response envelope, and stop when authorization is missing or unclear.

Risk: Large market data exports may contain sensitive business research.

Mitigation: Review exported files before sharing them, store them only where appropriate, and delete them when the analysis no longer needs them.

Risk: Category recommendations can be misleading if site, billing period, category ID, or result status is wrong.

Mitigation: Confirm the Shopee site and accounting period, derive category IDs from category tools, and treat a call as successful only after protocol, result, and inner business status checks pass.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-category-bluesea)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow authorization check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Concise Markdown with recommendation summaries, JSON/API request snippets, and optional exported local data files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large result sets are summarized in chat and delivered as exported files when available.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
