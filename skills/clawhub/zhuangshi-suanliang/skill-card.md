## Description:

根据房间类型、建筑说明、建筑图、结构图、房间装修表、做法表和节点详图，快速出装饰概算和物资计划；可导入 cad-file-reader 的长度/面积测量候选作为待核对输入，做法映射、洞口扣减、损耗、材料台账和清单量仍由本技能计算。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

施工员和技术人员可用本技能根据房间、做法及图纸资料编制装饰工程概算和物资计划，并查看计算依据、缺项与复核提示。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency controls may not reliably prevent an installed CAD runtime from executing.

Mitigation: Have the dependency bypass corrected and verify runtime behavior; do not rely on SKILL_NO_BASE=1 to prevent execution.

Risk: Discovered sharing clients may run without a sufficiently narrow trust boundary.

Mitigation: Restrict sharing to an explicitly trusted client.

Risk: Cached project data or imported practice codes may not match current project drawings.

Mitigation: Check cached data against current drawings and manually verify imported practice codes.

## Reference(s):

- [ClawHub release](https://clawhub.ai/lisong2003-lgtm/skills/zhuangshi-suanliang)

## Skill Output:

**Output Type(s):** [Files, CSV, Markdown]

**Output Format:** [XLSX workbook, CSV tables, and a Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes calculation details, references, missing-item checks, and review prompts; estimates are not for settlement, final quantity reconciliation, as-built measurement, or formal quotations.]

## Skill Version(s):

0.9.23 (source: frontmatter, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
