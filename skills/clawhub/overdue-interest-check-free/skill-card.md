## Description:

A free deterministic checker for overdue-interest worksheets that recalculates interest, checks day counts, reviews totals, detects duplicate or missing entries, and cites source line numbers for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, legal, and collections users can run this skill before month-end close, demand letters, or litigation preparation to check overdue-interest worksheet arithmetic. It supports arithmetic review and missing-input detection, not legal advice or a conclusion about enforceability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat arithmetic findings as legal conclusions about debt validity, limitation periods, or enforceability.

Mitigation: Use the output as calculation support only and route legal conclusions to qualified reviewers.

Risk: Incomplete or malformed worksheet input can lead to missing checks or no conclusion.

Mitigation: Provide a table with recognizable headers and review any missing-input messages before relying on results.

Risk: The free version omits checks for judicial rate limits, date anomalies, non-positive principal or rates, and negative booked interest.

Mitigation: Review the omitted-check list and run additional validation when those issues matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/overdue-interest-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Skill documentation](artifact/SKILL.md)
- [Sample input](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON report with source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on local worksheet text input; does not read Excel files directly; returns no conclusion when required inputs are missing.]

## Skill Version(s):

1.0.33 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
