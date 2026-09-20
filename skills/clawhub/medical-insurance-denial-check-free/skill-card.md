## Description:

医保拒付与申诉核对（免费版）逐项核对医保拒付与申诉核对表，复算金额、核对合计、检测重复、空缺和负数，并为结论提供原文行号依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashiering, billing, and reconciliation staff use this skill during periodic medical-insurance settlement checks to verify tabular denial and appeal calculations before follow-up work. It supports local review of arithmetic consistency, totals, duplicate denial numbers, blank placeholders, and negative amounts without deciding whether an individual denial should be appealed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a local Node.js script on files selected by the user, and the release text inconsistently mentions anonymous usage statistics.

Mitigation: Install and run it only where local Node execution on selected files is acceptable; review the security summary and use normal network controls if telemetry uncertainty matters.

Risk: The free edition omits several denial and appeal checks and does not decide whether an individual denial should be appealed.

Mitigation: Use the listed findings as reconciliation support only, review withheld and out-of-scope checks, and have qualified billing or medical-insurance staff make appeal decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/medical-insurance-denial-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Terminal text or structured JSON containing executed checks, findings, scope, summary, missing-input guidance, and withheld checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on user-provided table text or a JSON input file; returns explicit insufficient-input results instead of conclusions when required columns or rows are missing.]

## Skill Version(s):

1.0.44 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
