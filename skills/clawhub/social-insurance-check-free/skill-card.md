## Description:

Checks Chinese social insurance and housing fund declaration details for row-level arithmetic mismatches, aggregate consistency, duplicate people, and blank or placeholder fields, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, payroll, and operations staff use this skill during monthly closing, payroll, and reconciliation to check copied social insurance and housing fund declaration tables before acting on discrepancies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes paid-edition onboarding text that directs users toward mutable external code execution and a separate purchase flow.

Mitigation: Use the free local checker path only unless the external package, exact version, source, and payment flow have been independently reviewed and manually approved.

Risk: The free checker lists ratio, base-limit, and base-consistency checks as withheld, and the security evidence says ratio-related summary wording is unreliable.

Mitigation: Treat the output as limited to the executed free checks, review checks_withheld before relying on results, and do not treat the report as legal, payroll-policy, or audit advice.

Risk: Insufficient or malformed input causes the tool to produce no conclusion rather than a successful compliance finding.

Mitigation: Provide declaration details with recognizable headers and source rows, and interpret 'no findings' only as passing the executed arithmetic and data-quality checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/social-insurance-check-free)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable Chinese text or pretty-printed JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, source line, evidence text, advice, executed checks, withheld checks, and insufficiency messages.]

## Skill Version(s):

1.0.7 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
