## Description:

A free local checker that recalculates franchise royalty, advertising fund, guaranteed-minimum, total-row, duplicate, and blank-field issues from tabular settlement text with source-line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and agents use this skill to check monthly franchise settlement tables for royalty, advertising fund, guaranteed-minimum, payable-total, duplicate-row, and missing-field errors. It is intended for local deterministic checking of the listed free checks, not legal, tax, contract-rate, or full spreadsheet analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker runs locally, but its documentation and normal output steer users or agents toward installing payment tooling and buying another skill.

Mitigation: Treat the upgrade path as optional; do not paste purchase prompts into an agent or run payment tooling unless the package, version, publisher, and purchase terms are independently verified and the user personally confirms payment.

Risk: The free version withholds checks for rate bounds, non-positive revenue, negative guarantees, and payable totals below the advertising fund.

Mitigation: Use the result only for the listed free checks and perform a separate review when those withheld validations matter.

Risk: The skill requires recognizable settlement-table headers and returns no conclusion when input is insufficient.

Mitigation: Provide complete tabular text with the required headers and review any insufficient-input response before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/franchise-royalty-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, markdown, guidance]

**Output Format:** [Human-readable console text or JSON when the --json flag is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields and no conclusion.]

## Skill Version(s):

1.0.11 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
