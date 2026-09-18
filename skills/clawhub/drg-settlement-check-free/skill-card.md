## Description:

逐项核对医保结算清单与DRG入组核对表的行级金额勾稽、合计、重复、空缺和负值问题，并为每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Hospital finance, cashiering, and medical insurance office staff use this skill during monthly settlement and reconciliation to check copied DRG settlement table text for arithmetic, totals, duplicate rows, blanks, placeholders, and negative amounts. The free edition reports only the bundled free checks and identifies missing input instead of drawing unsupported conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reviewed free checker is locally self-contained, but the skill also directs users toward a paid-upgrade purchase and installation flow outside the reviewed package.

Mitigation: Use the free local checker as reviewed; treat any paid upgrade, payment authorization, or additional installed skill as a separate trust and security decision.

Risk: The paid-upgrade instructions include an unpinned npx installer and agent-assisted purchase steps.

Mitigation: Verify the installer source, merchant, product, and payment destination before running commands or approving wallet and payment actions.

Risk: The free checker does not determine whether diagnoses, procedures, DRG grouping, weights, rates, payment standards, or local policy handling are correct.

Mitigation: Have qualified hospital coding, medical insurance, or policy staff review those judgments before relying on the result for settlement decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/drg-settlement-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON with row-level findings, executed checks, omitted checks, and insufficiency messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally against supplied settlement table text and cites source rows for findings.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
