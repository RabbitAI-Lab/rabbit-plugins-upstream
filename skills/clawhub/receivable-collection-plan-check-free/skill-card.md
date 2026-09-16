## Description:

A Chinese-language local receivables checker that compares an accounts receivable collection plan and payment table for row-level arithmetic, totals, duplicate rows, blank placeholders, and negative amounts, with source-backed findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and treasury staff use this skill during month-end close, reconciliation, and cash planning to check receivables tables for deterministic calculation and consistency issues. It helps identify table-level discrepancies but does not determine credit risk, collection priority, legal exposure, or accounting policy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation and default output direct users toward an external paid upgrade, dependency installation, and purchase workflow.

Mitigation: Do not allow an agent to run the documented payment installation command or initiate a SkillPay purchase unless a human separately verifies the package, merchant, product, links, and each consent or payment step.

Risk: The free release omits five additional receivables checks, so users may overread it as complete coverage.

Mitigation: Review the reported `checks_not_run` list before relying on results, and use separate finance controls for omitted overdue, promise, aging, and write-off checks.

Risk: The skill performs table arithmetic and consistency checks, not credit, legal, ERP, or collection-policy analysis.

Mitigation: Treat findings as reconciliation support only and require finance review against source systems, contracts, and internal accounting policy before taking collection action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/receivable-collection-plan-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable terminal text or structured JSON with executed checks, omitted checks, findings, summary, and out-of-scope notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard libraries; sample evidence reports no network use.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
