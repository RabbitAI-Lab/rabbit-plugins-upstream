## Description:

差旅费报销与标准表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and reimbursement staff use this skill to check Chinese-language travel expense reimbursement tables against stated standards during monthly settlement, reconciliation, or audit workflows. It reports arithmetic mismatches, totals issues, duplicate rows, blank required fields, and negative amounts with source-backed findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free release explicitly does not run several checks, including meal allowance by days times standard and date-duration consistency checks.

Mitigation: Use the output's not-run list as a scope boundary and perform those checks separately before relying on reimbursement decisions.

Risk: The skill is presented in Chinese and expects Chinese travel expense table headers and terminology.

Mitigation: Use it only with compatible Chinese-language travel reimbursement tables, or validate column recognition with the included sample before processing real material.

Risk: Evidence notes stale or inaccurate telemetry wording because no telemetry implementation was found in inspected code.

Mitigation: Review current release behavior and user-facing telemetry statements before deployment in environments with strict data-handling disclosure requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/travel-standard-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Analysis, Shell commands, Guidance]

**Output Format:** [Human-readable console text or structured JSON findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on provided table text; reports insufficient input instead of drawing conclusions when required fields are missing.]

## Skill Version(s):

1.0.40 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
