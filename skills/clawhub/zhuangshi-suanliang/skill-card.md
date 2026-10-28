## Description:

根据房间类型、建筑说明、建筑图、结构图、房间装修表、做法表和节点详图，快速出装饰概算和物资计划；可导入 cad-file-reader 的长度/面积测量候选作为待核对输入，做法映射、洞口扣减、损耗、材料台账和清单量仍由本技能计算。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

施工员、技术员和造价人员可用它根据房间做法及图纸资料编制装饰概算草稿、物资计划和可复核的工程量台账。CAD 测量候选仅作为待核对输入，正式口径仍需结合项目做法、节点详图和适用规范复核。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may bypass the dependency opt-out before running dependency code.

Mitigation: Confirm the opt-out is checked before any dependency code executes; use the offline mode when dependency setup is not wanted.

Risk: Optional synchronization may execute an unverified local client, and retrieved project entries may be stale or mismatched.

Mitigation: Select and review the synchronization client explicitly or skip synchronization; check retrieved entries for project identity and recency before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/zhuangshi-suanliang)
- [README.md](artifact/README.md)
- [Quantity takeoff rules](artifact/rules/清单工程量规则.json)
- [National standards reference rules](artifact/rules/国家规范要求.json)

## Skill Output:

**Output Type(s):** [Analysis, CSV files, XLSX workbooks, Markdown reports, Review guidance]

**Output Format:** [CSV and XLSX quantity and materials ledgers, Markdown report, and review items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates estimate quantities from material order quantities and records formulas, assumptions, evidence, and items requiring confirmation.]

## Skill Version(s):

0.9.25 (source: server-resolved release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
