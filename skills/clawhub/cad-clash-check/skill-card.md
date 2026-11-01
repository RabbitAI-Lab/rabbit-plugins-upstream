## Description:

把各专业 DWG/DXF 图纸（或已解析识图产物）自动判专业、比对构件，输出跨专业碰撞候选位置与属性冲突清单（json+md）：优先消费 cad-file-reader 的 axis_networks[] 轴格区间做轴格定位（不同专业落入同轴格才判碰撞，坐标为佐证）；轴网缺失或不可用时如实降级为坐标判定并标 axis_missing=degraded。目标是图纸会审前的快速交叉核对；是 2D 图面重叠/冲突倾向提示，候选须人工复核，非 BIM 碰撞检测。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

建筑、结构与机电等专业的工程师可在图纸会审前，用它交叉检查 DWG/DXF 图纸或已解析的图纸数据，并整理需要人工复核的图面冲突候选。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incomplete axis coverage or degraded detection can omit clashes, so an empty report does not establish that drawings are clash-free.

Mitigation: Review axis coverage and degradation indicators, confirm drawings use comparable coordinates, and manually inspect results before treating a drawing as clear.

Risk: Generated reports may contain drawing information.

Mitigation: Use a trusted cad-file-reader installation and protect locally generated drawing reports.

## Reference(s):

- [ClawHub release page: cad-clash-check](https://clawhub.ai/lisong2003-lgtm/skills/cad-clash-check)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [JSON and Markdown reports, plus a JSON and Markdown construction plan template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports identify 2D conflict candidates and attributes for manual review; the skill does not calculate quantities.]

## Skill Version(s):

0.3.0 (source: frontmatter, manifest.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
