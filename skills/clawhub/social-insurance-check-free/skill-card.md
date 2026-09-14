## Description:

Checks Chinese social-insurance and housing provident-fund declaration tables for row-level arithmetic errors, total reconciliation issues, duplicate people, and blank or placeholder fields, with each finding tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Payroll, HR operations, finance, or business-operations users use this skill to sanity-check Chinese social-insurance and provident-fund declaration details before filing or reconciliation. It identifies deterministic arithmetic and completeness issues, but results should be reviewed before filings or business decisions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Extra checks can run when full, credit, or token fields are supplied, beyond the advertised free scope.

Mitigation: Use only the intended table input fields unless enhanced checks are deliberately wanted, and review reported executed and skipped checks in the output.

Risk: Payroll and social-insurance findings may affect filings or business decisions.

Mitigation: Have payroll, finance, or compliance staff verify outputs against source records and applicable policy before filing or acting on the result.

Risk: Insufficient or malformed input can produce no conclusion rather than a clean pass.

Mitigation: Provide tables with recognizable headers and treat absent findings only as a pass for the checks that the output says actually ran.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/social-insurance-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON reports with source-line citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on pasted text or JSON social-insurance/provident-fund tables with headers; insufficient input returns no conclusion.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
