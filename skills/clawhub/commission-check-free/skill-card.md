## Description:

提成计算表逐项核对，覆盖逐行算术、合计勾稽、重复与空缺检测，并让每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, warehouse, and operations staff use this skill during month-end settlement, payroll, reconciliation, or inventory checks to audit sales commission tables for arithmetic consistency, totals, duplicate people, and blanks. It returns findings with source line references and states missing inputs instead of issuing a conclusion when evidence is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes prompts and links that steer users or agents into an external paid install and purchase workflow using mutable remote code.

Mitigation: Do not let an agent run the npx install or purchase flow automatically; verify the package, version, merchant, price, permissions, and payment destination separately, and require the user to complete any wallet authorization or payment confirmation themselves.

Risk: The free checker does not execute withheld checks such as laddered commission recalculation, rate-range validation, negative commission checks, or inconsistent rates for the same person.

Mitigation: Treat results as coverage-limited arithmetic checks; review the listed non-executed checks before making payroll, audit, or reimbursement decisions.

Risk: Commission and payroll tables can contain sensitive employee and compensation data.

Mitigation: Prefer the local free checker path and avoid sending source tables to unrelated external services or payment/install workflows unless the organization has approved that disclosure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/commission-check-free)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable terminal output or JSON report with findings, source lines, summaries, and missing-input messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node standard library against JSON input or pasted tabular text; the artifact claims no network use for the free checker, but includes external paid-upgrade instructions.]

## Skill Version(s):

1.1.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
