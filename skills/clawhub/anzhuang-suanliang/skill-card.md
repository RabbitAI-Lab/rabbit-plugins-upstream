## Description:

从安装工程 DWG 或扫描索引提取概算清单底稿与物资计划草稿，估算多类安装工程管线、设备和材料数量，并支持图审查量与专业软件结果交叉核对。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

安装工程师和项目团队可用此技能从 DWG 图纸或已有扫描索引整理概算工程量底稿与物资计划草稿，并核对匹配情况和待复核项。结果需结合图纸、合同和专业软件复核，不能替代结算计量或翻样。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional data sharing may run automatically discovered programs, and documented safeguards may not match the code.

Mitigation: Use a reviewed CAD dependency and explicitly select a trusted bus client; do not rely on the offline switch alone to prevent dependency setup.

Risk: Cached scan data or inferred pipe sizes may not match the current drawings.

Mitigation: Check cached data against the current drawings and manually verify inferred pipe sizes before using estimates.

## Reference(s):

- [安装算量 ClawHub 页面](https://clawhub.ai/lisong2003-lgtm/skills/anzhuang-suanliang)
- [标准约束参考](artifact/references/standard_rules.json)
- [双口径映射参考](artifact/references/dual_caliber_rules.json)
- [损耗规则参考](artifact/references/loss_rules.json)

## Skill Output:

**Output Type(s):** [Files, JSON, Spreadsheets, Review guidance]

**Output Format:** [JSON scan indexes and multi-sheet Excel workbooks (.xlsx)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft quantities and material plans with confidence levels and review flags; excludes prices and settlement quantities.]

## Skill Version(s):

0.4.26 (source: SKILL.md frontmatter, CHANGELOG.md, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
