## Description:

从安装工程 DWG 或扫描索引生成概算清单底稿和物资计划草稿，汇总管线、设备与材料估算并标出需人工复核的项目。

This skill is for research and development only.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Construction estimators and MEP engineers use the skill to draft installation quantity takeoffs and material plans from drawings or scan indexes, then review uncertain matches against the source drawings. It does not provide pricing or final settlement quantities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First run may download and execute a separate CAD reader dependency.

Mitigation: Review the dependency before installation; preinstall a trusted copy and set CAD_SKILL_DIR, or use SKILL_NO_BASE=1 for reduced-function offline operation.

Risk: Unmatched drawings or inferred lengths can produce inaccurate draft quantities.

Mitigation: Check flagged items against drawings and professional takeoff tools before procurement or decisions; do not use estimates as settlement quantities.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/anzhuang-suanliang)
- [Standard and calculation rules](artifact/references/standard_rules.json)
- [Dual-caliber mapping rules](artifact/references/dual_caliber_rules.json)
- [Allowances and loss rules](artifact/references/loss_rules.json)

## Skill Output:

**Output Type(s):** [Files, Analysis]

**Output Format:** [Multi-sheet XLSX workbook and JSON scan index]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft estimates include unmatched items and review notes; measurement candidates are not final quantities.]

## Skill Version(s):

0.4.17 (source: frontmatter, manifest.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
