## Description:

将单个工程招标或中标披露整理为八项逐字卡，逐项保留原句与来源锚，并标明缺失信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

采购、招投标及相关研究人员可用它整理单个工程项目的招标公告、中标公示或结果公告，核对披露口径并追溯每项原文。它不提供投标建议或中标预测。

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: 启用可选 Cue 服务时，API 凭据和提交的招标材料可能离开本地处理环境。

Mitigation: 启用前核实凭据发送目的地、费用和数据保留方式；发送非公开附件或批注前取得授权。

Risk: 转手来源或缺失披露可能导致信息不完整或金额、日期有误。

Mitigation: 保留缺项标记，并对照官方披露核验引文、金额和日期。

Risk: 安装来源未经审阅或未固定版本会降低供应链可追溯性。

Mitigation: 优先使用经过审阅且固定版本的安装来源。

## Reference(s):

- [披露环节链与来源锚记法](artifact/references/bid-chain.md)
- [Cue data service configuration](https://cuecue.cn/hub/mcp)
- [Cue attachment parsing configuration](https://cuecue.cn/hub/omni-reader)
- [Cue API key page](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [中文五段式招投标披露 Markdown 卡片，含逐字引文与来源锚]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [覆盖八项披露；缺失项明确标注「未检索到」；预测与判断标注「[待人工]」。]

## Skill Version(s):

0.1.0 (source: SKILL.md frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
