## Description:

Checks rent collection and arrears ledgers for row-level arithmetic, totals, duplicate rows, blanks, and negative values, with each finding tied back to the source row.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and property operations staff use this skill during monthly rent closing or reconciliation to check rent collection and arrears tables before reporting or follow-up collection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is marked suspicious because the free checker includes an upsell path that asks an assistant to install unpinned external code and proceed through a paid SkillPay flow.

Mitigation: Use the local free checker by default; before any paid upgrade, independently verify the package, version, source, permissions, and purchase terms, and require explicit human approval for each install and payment step.

Risk: The skill is Chinese-language and narrowly scoped to rent-ledger table reconciliation, so users may over-read its output as contract, tax, or accounting advice.

Mitigation: Treat findings as table-reconciliation cues only, and have qualified staff review contract interpretation, tax treatment, accounting treatment, and collection decisions.

Risk: The free version intentionally omits several checks that are listed as paid-version scope.

Mitigation: Read the reported checks_not_run list and do not treat a clean free-version result as coverage for omitted checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/rent-collection-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid-version purchase information referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON check results from local ledger reconciliation commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input returns missing requirements instead of a conclusion; paid-version checks are listed as not run.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
