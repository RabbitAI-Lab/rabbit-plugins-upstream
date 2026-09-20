## Description:

Checks copied utility allocation tables for row-level arithmetic, total-row consistency, duplicate tenants, and blank or placeholder values, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, property-management, and operations users can use this skill to check copied utility allocation tables during monthly reconciliation. It helps identify arithmetic mismatches, incorrect total rows, duplicate tenant rows, and missing or placeholder values without treating the result as legal, tax, or allocation-policy advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may rely on this free release for checks it explicitly does not perform, including withheld paid checks, legal or tax advice, and judgments about whether an allocation rule is fair.

Mitigation: Use the output only for the listed table-arithmetic and data-quality checks, and review missing-scope items before making billing, legal, tax, or policy decisions.

Risk: The artifact help text references an anonymous usage-statistics message, while security evidence reports no evidence of network access.

Mitigation: Treat the server security evidence as authoritative for release review, and have the publisher correct misleading user-facing text before relying on that claim in public documentation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/utility-allocation-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON findings with source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts copied utility allocation table text; materials that lack recognizable headers or rows produce an insufficient-input response rather than a conclusion.]

## Skill Version(s):

1.0.43 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
