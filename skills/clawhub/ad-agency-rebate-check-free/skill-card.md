## Description:

广告代理返点与框架返点核对（免费版） helps finance and operations users locally check ad-agency rebate and framework rebate tables for arithmetic mismatches, total-row inconsistencies, duplicate rows, missing values, and negative amounts with source-grounded findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashiering, and business-operations teams use this skill during monthly or quarterly close to check ad-agency rebate and framework rebate tables for arithmetic mismatches, missing values, duplicate rows, negative amounts, and total-row inconsistencies. It is a free-tier checker and does not decide contract terms, tax treatment, or whether source ad-spend data is true.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill promotes an optional external paid installation path and prints upgrade links in normal results.

Mitigation: Use the free checker only for local rebate-table audits; do not follow the optional SkillPay or npx purchase workflow unless the package, publisher, and paid skill are independently verified.

Risk: Human-readable output may include upsell text alongside audit findings.

Mitigation: Use the --json output mode when clean machine-readable results are needed for review, logging, or downstream processing.

Risk: The free version withholds several checks and does not assess contract terms, tax treatment, or the truth of source ad-spend data.

Mitigation: Treat findings as table-consistency checks only and route contract, tax, source-data, and omitted-check questions to qualified reviewers or separate tooling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ad-agency-rebate-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Optional full-version purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON findings from local Node.js command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include executed checks, withheld checks, row and period counts, severity counts, verdict, and cited table lines; insufficient input returns missing requirements instead of a conclusion.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
