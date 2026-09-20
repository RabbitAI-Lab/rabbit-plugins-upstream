## Description:

This skill checks property tax and urban land use tax worksheets by recalculating stated bases, tax amounts, installment amounts, declared tax, book tax, totals, duplicate rows, and missing fields, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and tax staff at organizations with owned property or land use this skill before filing to recalculate worksheet relationships for property tax and urban land use tax. It helps find arithmetic, declaration, bookkeeping, duplicate-row, and missing-field issues, but it does not provide tax advice or select local rates or exemptions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill processes tax worksheet data with a local Node runner, and security evidence notes inconsistent documentation about anonymous usage statistics.

Mitigation: Review the runner before using sensitive business records and run it only in an environment whose local execution and telemetry posture are acceptable.

Risk: The checks recalculate worksheet relationships but do not validate local policy choices such as deduction ratios, land grade tax standards, exemptions, or special lease rules.

Mitigation: Have a qualified tax reviewer confirm local rates, exemptions, and filing treatment before relying on results for submission.

Risk: The free release omits some checks that the artifact lists as outside this version, including some data-consistency and correction-list items.

Mitigation: Review the executed and withheld check lists in the output scope before treating a clean result as complete coverage.

## Reference(s):

- [ClawHub skill page: property-tax-land-use-check-free](https://clawhub.ai/chenqg618/skills/property-tax-land-use-check-free)
- [Publisher profile: chenqg618](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Console text or JSON result with worksheet findings, line references, missing-input status, and executed-scope details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns no conclusion; the runner is a local Node script over copied worksheet text or JSON input.]

## Skill Version(s):

1.0.51 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
