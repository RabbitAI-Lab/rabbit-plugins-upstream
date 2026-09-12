## Description:

Helps agents analyze Ozon competitor shops with Qinghu data by identifying active products, shop trends, sales structure, and promising new listings for follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Ozon sellers and ecommerce analysts use this skill to compare competitor shops, inspect product and shop trend data, identify new products gaining traction, and prepare practical follow-up recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use a Qinghu API token from user input or environment variables.

Mitigation: Keep the token scoped and private, pass it only as the documented Bearer authorization header, and avoid displaying it in agent responses or exported files.

Risk: The skill performs external Qinghu data calls that may consume Qinghu credits.

Mitigation: Review the planned tool list and cost prompt before approving calls, and use the returned pointCost value as the authoritative usage record.

Risk: HTTP 200 responses or non-error envelopes may still contain failed business results.

Mitigation: Validate protocol errors, result.isError, and the parsed inner response code and success fields before treating a call as successful.

Risk: Competitor-shop follow-up recommendations may involve brand authorization, patent, or marketplace compliance questions.

Mitigation: Check product rights, platform rules, and authorization requirements before sourcing or listing products based on the analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-shop-intercept)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with API call examples and optional exported table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May export local table files when returned record arrays contain 10 or more rows.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
