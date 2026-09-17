## Description:

Runs a local free-tier reconciliation check for member points and stored-value card write-off tables, including row-level recalculation, total checks, duplicate detection, blank detection, and cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and retail operations users can use this skill during monthly closing, reconciliation, or inventory review to check member points and stored-value card reconciliation tables before relying on the results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented paid-upgrade path can run unpinned remote package code and load another skill.

Mitigation: Use the free local checker only unless the package, merchant, product, payment page, and newly installed skill instructions have been independently verified in a controlled environment.

Risk: Normal output includes a paid-upgrade prompt that may distract from reviewing the actual reconciliation findings.

Mitigation: Review the free-tier report scope and findings first, and ignore the paid-upgrade prompt unless a separate purchase review is intended.

Risk: The free tier omits several checks that users might assume were performed.

Mitigation: Read the reported checks_not_run and checks_out_of_scope fields before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/retail-member-points-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON reconciliation report with findings, cited source rows, scope, summary, and exit status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; the free release reports withheld checks and does not make a positive conclusion when input is insufficient.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
