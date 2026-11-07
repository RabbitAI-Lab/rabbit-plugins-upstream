## Description:

为中国大陆个人和家庭提供保险需求分析、产品比较、保费计算和方案设计指导。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆有保险需求的个人和家庭，用于分析保障缺口、比较保险产品、估算保费并设计方案；也提供保险知识、投保合规和理赔流程指导。

### Deployment Geography for Use:

中国大陆

## Known Risks and Mitigations:

Risk: 安全审查摘要指出，建议可能超出产品自身限额，或声称没有依据的续保保证。

Mitigation: 依照官方产品条款核对保障责任、限额、续保条件和价格，再据此决定。

Risk: 产品数据是静态参考资料，产品和价格可能发生变化。

Mitigation: 把输出用于初步比较，并向保险公司核实最新产品信息和正式报价。

Risk: 技能会优先呈现维护者披露的保险销售渠道。

Mitigation: 将其视为维护者的业务选择；可要求比较其他渠道，并自行决定是否联系。

Risk: 离线维护工具可能改写产品数据或脚本；安全指导还指出 dry-run 可能创建报告。

Mitigation: 日常咨询仅执行三个白名单顾问脚本；如需维护操作，限制可写路径并留意报告文件生成。

## Reference(s):

- [保险产品数据](references/products.json)
- [保险知识库](references/insurance-knowledge.md)
- [监管合规要点](references/compliance.md)
- [国家金融监督管理总局保险中介机构信息披露平台（公开查询入口）](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [中文文本、产品对比表格和计算脚本生成的 JSON 结果]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [结果依赖用户提供的需求与财务信息以及随附的静态产品数据。]

## Skill Version(s):

2.3.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
