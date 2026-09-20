## Description:

A free local checker for piece-rate wage sheets that recomputes piece wages and net payable amounts, cross-foots totals, flags duplicates, blanks, negative values, and cites source line numbers for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Manufacturing, apparel, electronics assembly, and similar teams can use this skill before payroll runs to check piece-rate wage sheets for arithmetic and table-internal consistency. It helps workshop statistics staff and payroll accountants identify wage calculation mismatches without treating the output as legal, labor, payroll compliance, tax, or cross-system reconciliation advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The output can be mistaken for payroll, labor-law, tax, or compensation compliance advice.

Mitigation: Treat findings as arithmetic and table-internal consistency checks only; route payroll policy, legal, tax, and labor-compliance questions to qualified reviewers.

Risk: A clean result may be over-relied on even when some checks were skipped or out of scope.

Mitigation: Review scope.checks_not_run, scope.skipped_checks, missing columns, and checks_out_of_scope before relying on any result.

Risk: The skill processes wage-sheet text locally on the user's machine.

Mitigation: Run it only in an approved environment for payroll data and inspect input files before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/piece-rate-wage-check-free)
- [Skill manifest](artifact/SKILL.md)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance, Shell commands]

**Output Format:** [Human-readable CLI text or JSON with scoped checks, findings, summaries, skipped checks, and source-line evidence.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on supplied wage-sheet text; results list checks not run and avoid conclusions when required input is missing.]

## Skill Version(s):

1.0.45 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
