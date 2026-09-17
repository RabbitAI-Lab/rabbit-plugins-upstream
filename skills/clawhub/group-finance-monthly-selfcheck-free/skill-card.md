## Description:

Runs a local, deterministic monthly finance self-check for group intercompany reconciliation, supplier payable reconciliation, and accounts receivable aging inputs, with source-backed findings and no conclusion when required material is missing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and treasury staff use this skill during monthly close, reconciliation, and review cycles to check pasted group finance tables for arithmetic consistency, totals, duplicates, blanks, and aging-bucket issues. It supports review workflows but does not replace accounting judgment, audit, tax, or legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional upgrade path asks users to run an unpinned external installer and then follow newly installed purchase or setup instructions.

Mitigation: Use only the bundled free local checker unless the external package source has been independently trusted and the newly installed onboarding instructions have been reviewed before execution.

Risk: Finance self-check findings can be mistaken for professional assurance or accounting advice.

Mitigation: Treat the output as a reproducible arithmetic and consistency review, then route material issues or judgment calls to qualified finance, audit, tax, or legal reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/group-finance-monthly-selfcheck-free)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Plain text or JSON findings with cited source rows, summary counts, omitted checks, and insufficient-input guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on supplied text input; does not use the network for the bundled free checks and withholds conclusions when required input is missing.]

## Skill Version(s):

1.0.4 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
