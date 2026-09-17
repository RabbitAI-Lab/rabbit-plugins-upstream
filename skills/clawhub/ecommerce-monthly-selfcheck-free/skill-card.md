## Description:

电商财务月度自查包（免费版） locally checks segmented ecommerce finance reconciliation material for platform settlement, promotion subsidy write-off, and livestream commission or slot-fee settlement, citing source lines and returning reproducible findings when enough data is provided.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations staff use this skill during monthly ecommerce close to run deterministic checks on pasted platform settlement, promotion subsidy, and livestream commission tables. It supports offline arithmetic and cross-check review, but does not replace bookkeeping, audit, tax, or payment verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says the skill includes unsafe paid-upgrade installation instructions involving an @latest installer and payment flow.

Mitigation: Do not copy or run the paid-upgrade prompt unless the package, version, publisher, and payment flow are separately verified outside this skill.

Risk: The release security summary says the skill can report a clean top-level result when no checks actually ran.

Mitigation: Review per_check and sections_done before trusting the top-level verdict, and treat missing or zero executed checks as inconclusive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ecommerce-monthly-selfcheck-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON containing executed checks, withheld checks, per-check status, findings, summary verdict, and local-execution metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows when available; insufficient input returns missing-material guidance instead of a reconciliation conclusion.]

## Skill Version(s):

1.0.5 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
