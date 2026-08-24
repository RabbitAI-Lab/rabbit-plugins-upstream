## Description:

青虎AI TikTok 单品分析：批量查商品详情，拆解它关联的带货视频、直播与达人，读商品评论，量化单品的全网爆发力与渠道依赖度（靠视频、靠直播还是靠达人矩阵），为货源采购与推广预算提供数据支撑。当用户要分析 TikTok 某个商品、看某款靠什么渠道起量、评估单品爆发力、看商品评论口碑、判断备货和推广预算时必须触发。关键词：青虎AI、TikTok、TikTok Shop、单品分析、爆发力、渠道依赖、带货视频、直播、商品评论、备货、推广预算。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and analysts use this skill to analyze known TikTok Shop products, evaluate channel drivers across videos, livestreams, and influencers, review comments, and decide inventory and promotion budgets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Qinghu bearer token and may spend Qinghu credits when API calls are approved.

Mitigation: Before approving calls, confirm the request is about TikTok or TikTok Shop analysis, confirm use of the Qinghu token, and report credit consumption from the API response envelope.

Risk: Product conclusions can be misleading if an API call fails or returns only a limited sample, such as capped comment data or T+1 data.

Mitigation: Check the protocol result, parsed business response, success code, sample size, site, and reporting period before presenting conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-product-analyst)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown summary with optional exported table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes conclusion-first product judgment, channel-structure analysis, review themes, inventory and budget guidance, and reported Qinghu credit consumption when API calls are made.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
