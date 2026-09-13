## Description:

青虎AI TikTok 单品分析帮助代理根据青虎数据接口批量查询商品详情、关联视频、直播、达人和评论，并输出单品爆发力、渠道依赖、备货和推广预算建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, ecommerce analysts, and agent users apply this skill to evaluate a known TikTok Shop product, determine whether growth is driven by video, live selling, or influencer distribution, and turn Qinghu API data into sourcing, inventory, and promotion-budget guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Qinghu API tokens from user input or environment variables.

Mitigation: Install only where those token variables are intended to be available to analysis workflows, and request user confirmation before API calls.

Risk: The skill can make metered Qinghu API calls.

Mitigation: Tell the user which Qinghu tools will be called, obtain consent before the first call in a session, and report actual point consumption from the response envelope.

Risk: Large result sets may be exported to local files.

Mitigation: Use exported files for detailed records, keep chat previews short, and avoid exposing exported data outside the user's intended workspace.

Risk: TikTok product conclusions may be misleading if API calls fail or data has collection lag.

Mitigation: Check protocol, envelope, and inner business success fields before using results, and describe data freshness or sample limits in the analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-product-analyst)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown analysis with optional JSON requests, shell or code snippets, and exported table files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should lead with a recommendation, include metric scope such as site and sample size, and report Qinghu point consumption when paid calls are made.]

## Skill Version(s):

0.1.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
