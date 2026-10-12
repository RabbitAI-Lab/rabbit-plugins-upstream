## Description:

根据房间类型、图纸及装修做法生成装饰工程概算和物资计划，并将 CAD 测量候选保留为待核对输入。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

施工人员和造价人员用房间信息、图纸及项目做法编制可复核的装饰概算和材料需求计划；CAD 测量结果只作为待确认的输入。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may download, install and run a CAD dependency in the user's local skills directory; network-use descriptions are inconsistent.

Mitigation: Review the dependency before installation; in controlled or offline environments set SKILL_NO_BASE=1 and manage the CAD dependency manually.

Risk: Generated quantities and example prices may be inaccurate or mistaken for approved commercial figures.

Mitigation: Have qualified staff check inputs, CAD candidates, project rules, quantities and current prices; do not use drafts for settlement or formal quotations.

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/lisong2003-lgtm/skills/zhuangshi-suanliang)
- [技能使用说明](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV files, Excel workbook]

**Output Format:** [Markdown report, CSV tables, and six-sheet XLSX workbook]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes calculation bases, missing-item checks and material quantities; estimates are drafts, not final pricing or settlement figures.]

## Skill Version(s):

0.9.6 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
