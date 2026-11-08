## Description:

安装算量：从安装图纸/扫描索引出概算清单底稿和物资计划草稿——管线按规格分档、电线芯线与预留展开、电缆/桥架/给排水/喷淋/支吊架/设备数量；不替代翻样下料结算，不出金额。

This skill is for research and development only.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Building MEP estimators and engineers use this skill to turn drawing scans into rough quantity takeoff workbooks and material planning drafts, then review flagged assumptions against the source drawings and project rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the release suspicious for a reported capability mismatch and unclear tool scope.

Mitigation: Review the documented commands and script scope before installation, and run only workflows needed for the project.

Risk: The scan reports that a validator selected through an environment setting may be executed.

Mitigation: Inspect the selected validator path and use a trusted, fixed path before running validation.

Risk: The scan reports an unpinned dependency.

Mitigation: Review dependency sources and pin a reviewed version before setup.

Risk: Security analysis was partial because a local reference was missing, so scan evidence is incomplete.

Mitigation: Resolve the missing-reference gap and complete a full security review before relying on a clean assessment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/anzhuang-suanliang)
- [Publisher profile](https://clawhub.ai/user/lisong2003-lgtm)
- [Dual-caliber quantity rules](artifact/references/dual_caliber_rules.json)
- [Standard rules and scope](artifact/references/standard_rules.json)
- [Loss, reserve, and threshold rules](artifact/references/loss_rules.json)
- [CAD reader contract](artifact/references/base-contract.md)
- [Runtime guidance](artifact/docs/runtime.md)

## Skill Output:

**Output Type(s):** [Files, Analysis, Guidance]

**Output Format:** [Excel quantity takeoff and material-plan workbook (XLSX) with reviewable tables and notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft quantities with confidence, matching, and review notes; no prices or settlement quantities.]

## Skill Version(s):

0.4.34 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
