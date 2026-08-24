## Description:

青虎AI TikTok 选品决策帮助代理人联动商品榜、视频榜、达人库、店铺商品列表和商品详情，输出 TikTok 选品报告并支持 1688 货源采集与晓风 ERP 铺货流程。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and commerce analysts use this skill to compare TikTok product demand, content momentum, influencer supply, competitor shops, sourcing options, and listing readiness before deciding which products to pursue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses paid Qinghu data calls.

Mitigation: List the tools and expected purpose before the first call, get user approval, and report actual Qinghu credit consumption from the returned pointCost value.

Risk: The skill may need a Qinghu API token from the user or environment.

Mitigation: Use the token only for Qinghu API calls, avoid echoing it in responses or exported files, and distinguish transient 401 responses from invalid credentials before asking for a new token.

Risk: The skill can produce local exported data files.

Mitigation: Tell the user where exports are written and keep summaries concise so large datasets are shared as files rather than pasted into chat.

Risk: ERP listing actions can affect storefront operations.

Mitigation: Require separate confirmation of the links and template before invoking any Xiaofeng ERP listing action.

## Reference(s):

- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow authorization check](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown report with concise conclusions, supporting evidence, optional exported data files, and command or API-call snippets when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should state measurement scope such as site, accounting period, cycle, and sample size; large record sets are exported instead of pasted into chat.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
