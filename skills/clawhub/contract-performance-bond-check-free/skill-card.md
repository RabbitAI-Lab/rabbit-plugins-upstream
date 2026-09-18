## Description:

Checks contract performance bond and guarantee ledgers for row-level arithmetic, totals, duplicate rows, blanks, placeholders, and negative amounts, with findings tied to source rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and treasury staff use this skill during monthly close, reconciliation, or inventory checks to validate performance deposit and guarantee ledgers before follow-up action. It is intended for local review of user-provided ledger text, not for legal, bank-authenticity, or policy-compliance determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The paid-upgrade flow asks an assistant to run an unpinned external installer and continue into a purchase or install workflow.

Mitigation: Verify the exact package version and source, avoid blind `@latest` installs, and require explicit human review before any payment, wallet authorization, or installation.

Risk: The free edition omits several checks, including over-refund, expired guarantee timing, negative guarantee balance, deposit-ratio, and zero-deposit fee checks.

Mitigation: Review `scope.checks_not_run` and do not treat the free result as covering legal, bank, or policy-compliance questions outside the stated arithmetic and ledger checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/contract-performance-bond-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid-version purchase instructions referenced by the artifact](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON result objects with findings, scope, summary, notes, and withheld checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source row numbers; insufficient input returns missing-field guidance instead of a pass/fail conclusion.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
