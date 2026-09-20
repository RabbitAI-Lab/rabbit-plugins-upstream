## Description:

Checks tuition refund tables by recalculating consumed tuition, refundable tuition, refund differences, total rows, duplicate students, and blank or placeholder fields, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Education and training finance or operations staff use this skill to check copied or exported tuition refund table text for arithmetic mismatches, total-row errors, duplicate student rows, blank fields, and missing required columns. It supports refund reconciliation and does not decide contract terms, legality, or audit completeness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Refund arithmetic findings may be mistaken for legal advice or a complete audit.

Mitigation: Use the output as a reconciliation aid only; review contract terms, refund policies, and legal requirements separately.

Risk: Incomplete, malformed, or headerless table input can prevent reliable conclusions.

Mitigation: Provide copied or exported table text with the required headers, and treat insufficient-input messages as a request for more source material rather than as a pass.

Risk: The free edition omits several checks, including over-consumed hours, consumed tuition exceeding paid tuition, negative refundable tuition, threshold-based difference checks, and non-positive hour or unit-price checks.

Mitigation: Review the listed withheld and out-of-scope checks before relying on the result, and run additional controls when those checks matter.

Risk: Documentation mentions anonymous usage statistics, while the security evidence says no networking code was present in the inspected files and documentation is inconsistent.

Mitigation: Follow local telemetry policy before deployment and review runtime behavior in controlled environments when no-network operation is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tuition-refund-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON findings with source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires copied or exported table text with recognizable headers; results are deterministic reconciliation findings, not legal advice or a full audit.]

## Skill Version(s):

1.0.45 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
