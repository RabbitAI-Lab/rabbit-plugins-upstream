## Description:

根据房间和图纸信息生成装饰工程概算、工程量明细与物资计划，并将 CAD 测量候选保留为待核对输入。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Construction estimators and site engineers use this skill to prepare preliminary decoration cost estimates and material procurement plans from room schedules, drawings, construction methods, and measurements. CAD measurements remain review candidates rather than final quantities; project documents and current standards require independent checking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may download and execute the external cad-file-reader dependency even though the skill claims not to use the network.

Mitigation: Review the dependency before installation; in locked-down or offline environments set SKILL_NO_BASE=1 and CAD_AUTO_SETUP=0 and install/review cad-file-reader separately.

Risk: Preliminary quantities and built-in prices may be mistaken for approved project estimates or final measurements.

Mitigation: Verify CAD candidates, calculation assumptions, project rules, rates, and current standards before using results for procurement or pricing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/zhuangshi-suanliang)
- [Skill README](README.md)
- [Quantity calculation rules](rules/清单工程量规则.json)
- [Standards reference index](rules/国家规范要求.json)

## Skill Output:

**Output Type(s):** [Files, Analysis, Guidance]

**Output Format:** [Excel workbook, CSV tables, and Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes calculations, estimate and material-plan totals, reference sources, and items requiring review; not a final quote or settlement quantity.]

## Skill Version(s):

0.9.7 (source: server-resolved ClawHub release; packaged frontmatter and changelog say 0.9.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
