## Description:

This skill runs a local free foreign-trade monthly self-check for export rebate calculations, export declaration and foreign-exchange collection write-off checks, and foreign-currency settlement and exchange-gain or loss checks from segmented tabular input.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashiering, and operations users at export businesses use this skill during monthly close or reconciliation to check segmented foreign-trade tables for arithmetic, totals, duplicate identifiers, blanks, and line-level evidence. It helps agents run local checks and report missing inputs without making tax, accounting, or filing determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags a suspicious upgrade path because documentation and default output steer users toward an unpinned external install and purchase workflow.

Mitigation: Use the packaged local free checker unless the external package and payment flow have been independently verified and every install, wallet authorization, or payment step is approved by the user.

Risk: Users may mistake arithmetic and reconciliation findings for tax, accounting, filing, or compliance determinations.

Mitigation: Treat results as reproducible table checks only, review source documents and applicable rules separately, and have qualified staff confirm any filing or accounting decision.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/export-monthly-selfcheck-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance, Shell commands]

**Output Format:** [Terminal text or JSON result objects with findings, per-check status, summaries, missing-input advice, and withheld-check notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard-library code; the free release executes three checks and lists two checks that are not included.]

## Skill Version(s):

1.0.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
