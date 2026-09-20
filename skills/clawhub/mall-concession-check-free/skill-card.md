## Description:

商场联营抽成与保底核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and reconciliation staff use this skill during monthly closing, account reconciliation, or inventory review to check mall concession rent tables for arithmetic consistency, total-row rollups, duplicate rows, blanks, and negative amounts. It supports table consistency review only and does not provide legal, tax, contract, or sales-policy advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may over-rely on arithmetic findings as legal, tax, contract, or sales-policy advice.

Mitigation: Use the skill for table consistency checks only, and have qualified reviewers confirm contract terms, tax treatment, sales definitions, and policy decisions.

Risk: Input tables may contain sensitive business information such as sales, rent, fees, and tenant details.

Mitigation: Review input data before use and follow the organization's data handling rules for business-sensitive reconciliation materials.

Risk: Incomplete, malformed, or missing table headers can prevent checks from running or limit the conclusions produced.

Mitigation: Provide the full table with recognizable headers and review any missing-input notices before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/mall-concession-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON containing source-cited reconciliation findings, missing-input notices, executed check lists, and withheld-check disclosures.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs as a local Node.js checker over user-provided table text or JSON input; output may include line-level findings and exit status.]

## Skill Version(s):

1.0.54 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
