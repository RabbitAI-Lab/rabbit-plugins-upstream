## Description:

青虎AI TikTok 达人带货建联：从达人库按站点和类目筛达人，批量查达人详情、达人视频列表与带货商品列表，反向从商品和店铺找关联带货达人，精准匹配高 ROI 达人，避免盲目寄样。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and operators use this skill to find, evaluate, and prioritize TikTok Shop influencers for product seeding and outreach. It supports forward discovery by region and category plus reverse discovery from competitor products or shops.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses Qinghu API credentials and may consume a token from the environment when present.

Mitigation: Confirm the intended Qinghu account before use and avoid exposing tokens in prompts, logs, or exported files.

Risk: Qinghu data calls may spend Qinghu credits.

Mitigation: Review the planned tools before approving calls and report actual credit consumption from the Qinghu response envelope.

Risk: Large influencer result sets may be exported to local files that persist after the session.

Mitigation: Store exported files only where appropriate for the data and remove them when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-influencer)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with optional shell command examples and exported table files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs prioritize concise recommendations, ranked influencer tiers, key evidence for each influencer, outreach suggestions, and Qinghu credit usage when paid calls are made.]

## Skill Version(s):

0.1.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
