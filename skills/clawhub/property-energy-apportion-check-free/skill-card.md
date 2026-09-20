## Description:

Checks Chinese property public energy meter and apportionment tables for row-level arithmetic, totals, ratios, duplicates, and missing fields, with each finding tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Property managers, property accountants, and regional finance reviewers use this skill before monthly billing, quarter-end review, or public ledger submission to check public energy apportionment tables for arithmetic and reconciliation issues. It reports insufficient input instead of producing unsupported conclusions when required table data is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a local Node.js script on property energy apportionment data.

Mitigation: Run it only in an environment approved for the input data and review the generated findings before using them for billing or dispute handling.

Risk: Security guidance notes contradictory wording about anonymous usage statistics, even though inspected code showed no material exfiltration behavior.

Mitigation: Confirm acceptable network behavior before deployment and prefer releases whose usage-statistics wording is unambiguous.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/property-energy-apportion-check-free)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Plain text or JSON findings from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include source line references, severity levels, executed checks, checks not run, and summary verdicts.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
