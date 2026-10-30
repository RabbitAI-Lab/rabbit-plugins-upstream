## Description:

从结构施工图生成按楼层或浇筑区汇总的混凝土方量与钢筋估算，并提供尺寸和标号复核提示；结果仅供物资计划参考，不替代翻样、下料、对量或结算。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0 (server metadata; artifact states CC-BY-NC-SA-4.0)

## Use Case:

施工人员和结构工程团队可用它从 DWG/DXF 结构图整理楼层或浇筑区的混凝土计划量、标号分档与钢筋估算带，并生成复核提示。数量属于估算计划口径，需由合格人员独立核验后再用于采购或工程决策。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The offline opt-out may still allow dependency code to execute.

Mitigation: Review and correct the offline opt-out behavior, and inspect the dependency before relying on it.

Risk: Reports may claim checks that were not performed, and passing checks do not consistently establish correctness.

Mitigation: Have a qualified person independently verify quantities and audit conclusions before ordering materials or acting on them.

Risk: Local caches retain drawing-derived information.

Mitigation: Delete local caches when they are no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/tujian-suanliang)
- [Publisher profile](https://clawhub.ai/user/lisong2003-lgtm)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, CSV, JSON, Shell commands]

**Output Format:** [Quantity estimates, review checklists, and structured reports in Markdown, CSV, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Planning estimates with review flags; not design, fabrication, settlement, or certified quantities]

## Skill Version(s):

0.9.24 (source: server-resolved release metadata, artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
