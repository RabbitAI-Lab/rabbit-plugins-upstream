## Description:

物业公共收益公示与分成核对把小区公共收益台账逐项复算，检查业主分成金额、季度小计、合计、重复登记、空缺、负值和比例范围，并为每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External property managers, owners' committees, and audit reviewers use this skill to check residential community public-income ledgers before publication or review. It recomputes stated amounts from provided ledger text and reports line-cited discrepancies without making legal, audit, or local-regulation judgments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime text mentions anonymous usage statistics, but the inspected package did not implement a network call, creating a documentation-consistency concern for users with strict local-only requirements.

Mitigation: Confirm the package behavior before deployment and update the user-facing text if no telemetry is implemented.

Risk: The skill does not decide whether property-income ratios, transfer amounts, due status, or local legal requirements are compliant.

Mitigation: Use the output as ledger arithmetic support and have qualified reviewers validate legal, audit, and local-regulatory conclusions.

Risk: The free version withholds several checks, including compliance attribution, maintenance-fund transfer review, arrears detection, and a full pre-publication action list.

Mitigation: Review the withheld-check list in each output and do not treat a clean free-version result as coverage of those omitted areas.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/property-public-income-check-free)
- [Artifact SKILL.md](artifact/SKILL.md)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable console text or structured JSON with findings, summary totals, executed checks, withheld checks, and line-cited advice.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js on pasted or JSON-wrapped ledger text; outputs insufficient-input status instead of conclusions when required columns or rows are missing.]

## Skill Version(s):

1.0.48 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
