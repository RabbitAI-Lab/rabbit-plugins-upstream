## Description:

青虎AI 抖音爆款视频跟卖与铺货：从抖音关键词视频数据和热搜榜发现正在起量的带货视频，转换短链拿到正式链接与视频数据，用 1688 以图搜款采集同款货源，再经晓风 ERP 选模板一键铺货到抖店。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Douyin sellers and commerce operators use this skill to find rising product videos, identify matching 1688 suppliers, and prepare or execute Douyin shop distribution through Qinghu and Xiaofeng ERP workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Qinghu API calls can consume Qinghu credits.

Mitigation: Require user confirmation before the first tool call, use returned pointCost as the source of truth, and report converted Qinghu credit usage when paid calls occur.

Risk: The workflow can use Qinghu tokens and Xiaofeng ERP authorization tied to a real commerce account.

Mitigation: Ask the user to provide or confirm credentials and authorized accounts, avoid exposing tokens in output, and never guess which ERP account to use when multiple accounts are available.

Risk: Confirmed distribution actions can list products to a Douyin shop.

Mitigation: Restate the product links, target account, and template before execution; prefer a preview run before final listing.

Risk: Following trending products can introduce brand, patent, or copied-media infringement risk.

Mitigation: Tell the user to verify brand authorization and infringement exposure before distribution, and recommend creating original listing media instead of copying another creator's video.

Risk: Poor supplier choice can harm fulfillment quality and shop performance.

Mitigation: Check supplier price, minimum order quantity, qualifications, and shipping speed before recommending or distributing a product.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-douyin-video-distribute)
- [ClawHub Publisher Profile](https://clawhub.ai/user/autoagc)
- [Qinghu MCP API Endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API Keys Dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Xiaofeng ERP Console](https://xfdyorder.zzbtool.com/zzb_super_goods_xf/index.html#/index)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration guidance]

**Output Format:** [Concise Markdown summaries with optional exported table files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports video candidates, supplier links, purchase details, selected account/template, per-item distribution status, failure reasons, and Qinghu credit usage when applicable.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
