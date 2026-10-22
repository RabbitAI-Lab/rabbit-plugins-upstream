## Description:

从安装工程 DWG/扫描索引提取概算清单底稿与物资计划草稿：按回路规格分档管线，展开电线芯线与预留，估算电缆、桥架、给排水、喷淋、支吊架和设备数量。目标是概算出量、物资计划、图审查量和专业软件结果交叉核对；不替代翻样、下料、结算，也不输出金额。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

开发人员和机电工程师可用此技能从安装工程 DWG 或扫描索引生成概算清单底稿、物资计划草稿和核对清单，并与图纸及专业算量软件交叉核验。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 首次依赖安装可能执行依赖代码；SKILL_NO_BASE=1 不能保证已存在运行时不会执行。

Mitigation: 安装前审查自动设置脚本；不要把 SKILL_NO_BASE=1 当作执行隔离措施。

Risk: 可选状态同步可能运行未经验证的本地脚本，或复用来源与时效不明的缓存记录。

Mitigation: 仅在客户端代码可信且缓存记录来源及时效已核实时启用同步。

Risk: 估算工程量可能不准确，不应直接作为最终施工或订货依据。

Mitigation: 人工核实所有估算数量，并与图纸及专业算量软件交叉校验。

## Reference(s):

- [双口径规则](references/dual_caliber_rules.json)
- [工程量标准规则](references/standard_rules.json)
- [损耗规则](references/loss_rules.json)
- [ClawHub 技能发布页](https://clawhub.ai/lisong2003-lgtm/skills/anzhuang-suanliang)

## Skill Output:

**Output Type(s):** [JSON, Spreadsheets, Analysis, Guidance]

**Output Format:** [JSON 扫描索引和多工作表 XLSX 工作簿]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [工程量为估算值，需人工复核；不输出金额或结算量。]

## Skill Version(s):

0.4.21 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
