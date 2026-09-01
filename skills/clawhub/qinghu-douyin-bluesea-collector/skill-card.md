## Description:

青虎AI 抖音蓝海爆品采集：结合抖音热搜榜与关键词下的视频数据，从小众高需求的细分场景切入找蓝海爆品，避开红海大词竞争，并接 1688 关键词搜索与以图搜款完成货源采集。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators and product researchers use this skill to identify lower-competition Douyin product opportunities, validate content demand, compare 1688 supply, estimate margin, and prioritize candidate products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Qinghu API token that may be exposed to the agent environment.

Mitigation: Use a scoped token where possible, provide it only through approved secret handling, and remove it from the environment when the workflow is complete.

Risk: Qinghu API calls can consume credits, including calls described as free by upstream tool metadata.

Mitigation: Review the planned tools and expected cost before the first call, then rely on the returned pointCost value for final cost reporting.

Risk: Large Douyin or 1688 result sets may be saved as local export files.

Mitigation: Review exported files before sharing, keep only the files needed for the decision, and delete them when no longer needed.

Risk: Hot-search or supply data can be misleading if treated as proof of demand or product quality.

Mitigation: Cross-check scene heat, video performance, supplier availability, margin assumptions, and sample quality before acting on recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-douyin-bluesea-collector)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown summaries with exported table files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include concise previews, export links, margin assumptions, priority rankings, and Qinghu point-cost reporting.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
