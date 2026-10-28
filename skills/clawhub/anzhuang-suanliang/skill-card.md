## Description:

从安装工程 DWG 或扫描索引生成概算清单底稿与物资计划草稿，供图纸复核和专业算量结果交叉核对。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

External MEP estimators and engineers use the skill to prepare rough installation quantities and material-plan drafts from building drawings, then review unmatched or estimated items against drawings and professional software. The results support budgeting and material planning but do not replace detailing, settlement, or contractual measurement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup opt-out may still allow dependency code to run because its ordering needs correction.

Mitigation: Use reviewed CAD and bus installations, explicitly select trusted client paths, avoid automatic development-copy discovery, and do not rely on SKILL_NO_BASE=1 to block every dependency action until the ordering is fixed.

Risk: Shared project retrieval may ignore the requested revision.

Mitigation: Verify shared project revisions manually before using retrieved data.

Risk: Quantity drafts can contain unmatched or estimated values that are unsuitable for direct ordering.

Mitigation: Cross-check quantity drafts and flagged items against drawings and professional software before ordering materials.

## Reference(s):

- [Loss, reserve, and threshold rules](artifact/references/loss_rules.json)
- [Standard quantity rules](artifact/references/standard_rules.json)
- [Estimate-to-material mapping rules](artifact/references/dual_caliber_rules.json)
- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/anzhuang-suanliang)

## Skill Output:

**Output Type(s):** [Analysis, Files, JSON, Guidance]

**Output Format:** [XLSX workbooks and JSON scan indexes or reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft quantities with confidence and review flags; no monetary amounts.]

## Skill Version(s):

0.4.24 (source: server-resolved release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
