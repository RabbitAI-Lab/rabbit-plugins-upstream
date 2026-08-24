## Description:

This skill helps agents identify Douyin blue-ocean product opportunities by combining Douyin trend and video signals with 1688 sourcing checks and margin-oriented prioritization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, product researchers, and ecommerce operators use this skill to find niche Douyin product opportunities, validate content demand against supply, and collect 1688 sourcing candidates before ranking by margin and priority.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can make paid Qinghu API calls.

Mitigation: Confirm the planned tools with the user before calling them, report costs using the returned Qinghu point cost, and stop when authorization is missing or unclear.

Risk: QINGHU_TOKEN or QHKIT_TOKEN can expose access to the user's Qinghu account.

Mitigation: Treat tokens as secrets, read them only from the user or environment when needed, and do not paste them into ordinary output.

Risk: Douyin trend or video activity may be mistaken for ecommerce demand.

Mitigation: Cross-check trends with keyword video data, hashtag data, 1688 supply, and margin assumptions before recommending a product opportunity.

Risk: A matching 1688 listing may not have the same quality as the product seen in Douyin content.

Mitigation: Flag sourcing uncertainty and recommend sample validation before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-douyin-bluesea-collector)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, API Calls, Guidance]

**Output Format:** [Markdown summaries with links to exported tabular files when record sets are large]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should lead with conclusions, label numeric assumptions and sample scope, and keep large datasets in exported files instead of long chat tables.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
