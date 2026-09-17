## Description:

建筑企业月度自查包（免费版） checks three categories of construction monthly reconciliation material: subcontract settlement and output value, progress payments and retention, and project output value and progress confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and construction operations staff use this skill during monthly close, reconciliation, or inventory checkpoints to check pasted tabular construction records for arithmetic consistency, totals, duplicates, blanks, and missing required material. The free edition reports source-cited findings for three included check categories and identifies withheld categories as not executed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags that the skill steers users toward unpinned remote payment tooling and a paid add-on installation workflow.

Mitigation: Do not run the SkillPay npx command or start the paid-product workflow unless the user explicitly intends to install external payment tooling and has reviewed the source, version, and payment steps.

Risk: The free edition executes only three check categories and leaves wage-account payment and earned-value analysis checks unexecuted.

Mitigation: Review the reported checks_not_run or withheld-checks output before treating the result as complete monthly construction reconciliation coverage.

Risk: Insufficient or unrecognized input can prevent checks from running, which could be mistaken for a clean result.

Mitigation: Require the expected section headers and table columns, and treat insufficient-input status as no conclusion rather than no issue found.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chenqg618/skills/construction-monthly-selfcheck-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance, Shell commands]

**Output Format:** [Human-readable text or JSON from a local Node.js command, with source-cited reconciliation findings and status metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on pasted or JSON-wrapped tabular input; exits with an insufficient-input status instead of issuing a clean conclusion when required material is missing.]

## Skill Version(s):

1.0.5 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
