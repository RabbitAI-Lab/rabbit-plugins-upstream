## Description:

Checks employee welfare and education expense ledgers for recalculation errors, total-line mismatches, duplicate rows, blanks, and negative amounts, with findings tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting staff use this skill during monthly close, reconciliation, or ledger review to check Chinese-language employee welfare and education expense tables for deterministic arithmetic and data-quality issues. It reports missing inputs instead of producing a conclusion when the ledger is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact embeds paid-version instructions that direct an agent to run an unpinned remote npx installer and start a purchase workflow.

Mitigation: Use only the free local checker unless the user separately verifies the package source and version, intentionally wants the paid workflow, and personally confirms any payment or wallet authorization.

Risk: The free edition withholds several checks and leaves tax treatment decisions outside scope, so a clean result is not a complete tax review.

Mitigation: Review the reported checks_not_run and out-of-scope items, and validate tax treatment against current authority or a qualified reviewer before filing or relying on the result.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/welfare-limit-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Console text or JSON result objects with line-level findings, executed checks, withheld checks, and insufficient-input messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Free edition executes a bounded local check set and lists checks not run; input files over 4M characters are rejected.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
