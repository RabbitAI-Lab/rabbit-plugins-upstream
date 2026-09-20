## Description:

Checks low-value consumables and revolving-material ledgers for arithmetic roll-forward errors, total-line mismatches, duplicate rows, blanks, and amortization overages, with each finding citing the source row.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Cost accountants and warehouse teams use this skill before monthly inventory and expense close or annual stocktaking to reconcile low-value consumables ledgers. It helps verify roll-forward calculations and identify ledger issues, but it does not replace accounting policy judgment, inventory counts, tax analysis, or audit procedures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The inspected package presents local checking behavior, but its help text mentions anonymous statistics controls that the security review says should be removed or fixed.

Mitigation: Install only if that privacy wording is acceptable, and have the publisher correct the statistics wording before broader deployment.

Risk: Users may overread ledger findings as accounting, tax, inventory, or audit conclusions.

Mitigation: Use the output as a reconciliation aid and have qualified personnel verify amortization method, item classification, tax timing, stock count, and audit treatment.

Risk: The free edition does not run several checks, including negative ending quantity, negative ending amount, negative amortization amount, unusual amortization method, and over-issue checks.

Mitigation: Review the reported checks-not-run list and perform separate procedures when those conditions matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/low-value-consumables-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Console text or JSON report with cited ledger findings, summary counts, executed checks, and checks not run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided ledger text or a JSON input file; the free edition reports omitted checks separately.]

## Skill Version(s):

1.0.15 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
