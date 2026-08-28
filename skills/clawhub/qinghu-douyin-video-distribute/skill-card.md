## Description:

青虎AI 抖音爆款视频跟卖与铺货：从抖音关键词视频数据和热搜榜发现正在起量的带货视频，转换短链拿到正式链接与视频数据，用 1688 以图搜款采集同款货源，再经晓风 ERP 选模板一键铺货到抖店，打通「爆款发现-链接采集-极速上架」链路。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators and agents use this skill to discover rising Douyin product videos, find same-product suppliers on 1688, and distribute selected items to Douyin shops through Xiaofeng ERP after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use Qinghu credentials and ERP-linked shop accounts for external data access and shop distribution actions.

Mitigation: Use it only in a trusted workspace, provide only the needed credential, confirm the ERP account and template, and review a preview before allowing actual distribution.

Risk: Exported spreadsheets or cached files may contain product, supplier, account, or operational data.

Mitigation: Store exported files in trusted locations, limit sharing, and remove local working files when they are no longer needed.

Risk: Following hot-selling products can involve brand authorization, patent, or copied-video material concerns.

Mitigation: Verify product rights and create original selling materials before listing or distributing items.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-douyin-video-distribute)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Xiaofeng ERP backend](https://xfdyorder.zzbtool.com/zzb_super_goods_xf/index.html#/index)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with structured lists and optional exported table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report video candidates, supplier links, ERP account/template selections, distribution previews, final success or failure counts, and failure reasons.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
