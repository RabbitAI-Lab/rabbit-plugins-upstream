## Description:

从 DWG/DXF 结构图读取 cad-file-reader 契约，按楼层/浇筑区输出混凝土、钢筋估算带和物资计划草稿；不替代翻样、下料与结算。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

施工员和技术员可用它从结构施工图生成按楼层或浇筑区划分的混凝土计划量与钢筋估算带，用于物资计划和方案比选。结果是计划口径估算，不适用于翻样下料、工程对量或结算。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports purpose and implementation mismatches, installation concerns, and estimate integrity concerns with medium confidence; the scan was partial.

Mitigation: Review the skill's purpose and installation behavior and pin dependency versions before installation. Independently check generated quantities against the source drawings and treat estimates and verification statements as unverified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lisong2003-lgtm/skills/tujian-suanliang)
- [Base contract](references/base-contract.md)
- [Usage examples](references/usage-examples.md)
- [Runtime guide](docs/runtime.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, CSV, JSON, XLSX, Guidance]

**Output Format:** [Quantity reports and planning tables in Markdown, CSV, JSON, or XLSX, with review notes and missing-input guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Planning estimates with explicit assumptions and missing-item notes; rebar is reported as an estimate band. Not suitable for bar detailing, takeoff settlement, or final measurement.]

## Skill Version(s):

0.9.40 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
