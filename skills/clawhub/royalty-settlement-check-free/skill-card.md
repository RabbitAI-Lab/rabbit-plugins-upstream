## Description:

版税与授权金结算核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External business users such as royalty accountants, publishers, IP owners, and content-company commercial teams use this skill to check royalty and licensing settlement tables at quarterly or semiannual settlement, statement, and audit-review points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free version does not perform several business checks, including contract-rate consistency, tier-rate switching, advance royalty offset, and duplicate settlement across different identifiers.

Mitigation: Review the listed withheld checks before relying on the result, and use additional contract, accounting, or full-version review for those cases.

Risk: Materials with missing or unrecognized table headers do not produce a conclusion.

Mitigation: Provide the royalty settlement table with recognizable headers and treat insufficient-input output as no conclusion rather than as a clean result.

Risk: Security guidance notes stale or inconsistent wording about anonymous statistics in script comments.

Mitigation: Review the release behavior and disable or avoid optional statistics behavior where required by local policy before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/royalty-settlement-check-free)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Guidance]

**Output Format:** [Human-readable console report or structured JSON with cited findings, missing-input guidance, executed checks, withheld checks, and result status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local table checks cite source rows and do not produce a positive conclusion when input is insufficient.]

## Skill Version(s):

1.0.42 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
