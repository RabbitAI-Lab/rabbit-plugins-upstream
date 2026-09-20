## Description:

Checks Chinese overtime-pay worksheets by recalculating hourly wage, 1.5x/2x/3x overtime rates, line totals, summary rows, duplicate people, and blanks, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

HR and finance staff use this skill before payroll to check overtime-pay worksheets for arithmetic errors in hourly wage conversion, overtime multipliers, overtime totals, summary rows, duplicate entries, and missing values. It is a worksheet arithmetic checker, not a legal opinion or validation of whether time records are accurate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker may use 21.75 as a stated assumption when the worksheet lacks 计薪天数.

Mitigation: Review any result that depends on the 21.75 assumption and confirm the intended payroll basis before using the finding.

Risk: The output can identify worksheet arithmetic issues but does not prove time records are accurate or provide legal advice.

Mitigation: Use the report as an arithmetic review aid and have qualified HR, finance, or legal reviewers assess employment-law and time-record questions.

Risk: The free version withholds some checks, including monthly overtime-hour limit, minimum-wage comparison, non-positive wages, negative overtime hours, and atypical pay-day checks.

Mitigation: Treat withheld checks as not evaluated and run separate review steps when those controls are required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/overtime-pay-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable terminal text or JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields and no conclusion; checks run locally from supplied worksheet text.]

## Skill Version(s):

1.0.33 (source: artifact/SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
