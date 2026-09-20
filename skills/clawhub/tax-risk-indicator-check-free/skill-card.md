## Description:

Checks Chinese tax-risk self-check tables for row-level arithmetic, total-line consistency, duplicates, blanks, and negative amounts, with findings tied to the source table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, accounting, and tax operations users can use this skill to self-check a Chinese tax-risk indicator table before monthly or quarterly close. It helps identify arithmetic mismatches, total-row errors, duplicate periods, blank placeholders, and negative amounts without presenting the output as a full tax-compliance review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the free-version result as a full tax-compliance review even though reference-rate, revenue/output, cost/input, and retained-credit checks are omitted.

Mitigation: Use the result for local arithmetic and consistency checks only; perform omitted checks separately or consult a qualified tax reviewer before relying on the table for compliance decisions.

Risk: The skill may return no conclusion when the provided table is missing required headers or usable rows.

Mitigation: Provide a tax-risk self-check table with the required columns and review insufficient-input messages before interpreting the absence of findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tax-risk-indicator-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Skill definition](artifact/SKILL.md)
- [Sample input](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable CLI text or structured JSON findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include check scope, omitted checks, row references, severity counts, and insufficient-input messages when required table content is missing.]

## Skill Version(s):

1.0.43 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
