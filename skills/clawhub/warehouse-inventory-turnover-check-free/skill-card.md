## Description:

Checks Chinese warehouse turnover and slow-moving inventory tables for arithmetic, totals, duplicates, blanks, and negative quantities or amounts, with source-cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and inventory operations teams use this skill during monthly close, reconciliation, or stocktaking to recalculate warehouse turnover and slow-moving stock figures. It helps identify table-level arithmetic mismatches, missing fields, duplicate warehouse-material rows, and negative quantity or amount entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker steers users or agents toward an external payment and skill-installation workflow.

Mitigation: Do not paste the included purchase prompt or run the npx installer unless the user independently trusts the payment workflow, accepts external code execution, and intends to initiate the paid skill flow.

Risk: Promotional upgrade text can mix with human-readable audit output.

Mitigation: Use JSON output when clean audit results are needed, and review the listed checks_not_run before treating the result as complete.

Risk: The free release omits several inventory checks that are listed as withheld.

Mitigation: Treat omitted checks as not executed, not as passed, and keep the scope.checks_not_run list with any downstream summary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/warehouse-inventory-turnover-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON audit results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input produces no conclusion; the free release lists checks that were not run.]

## Skill Version(s):

1.0.3 (source: server evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
