## Description:

A local shared-cost and allocation checker that runs six built-in checks per store directory and prints one conclusion line per store with source file and line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and cost-accounting teams for multi-store or multi-project businesses use this skill before monthly or quarterly settlement to run six shared-cost checks across store directories and review one conclusion line per store with source file and line citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Store-level accounting inputs may contain sensitive payment, insurance commission, warehouse charge, or scrap-sale settlement data.

Mitigation: Run the checker only in an approved local environment and provide only materials the user is authorized to process.

Risk: The checker performs arithmetic and consistency checks, but it does not replace accounting, audit, tax, compliance, or management-policy judgment.

Mitigation: Have finance or accounting reviewers confirm findings, allocation policy, tax treatment, and any business decision before relying on the output.

Risk: The free edition reports per-store conclusions and does not include cross-store rollups, risk ranking, common-issue grouping, or ledger export.

Mitigation: Treat the output as per-store review support and do not represent omitted paid-edition features as completed analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/shared-cost-pack-free)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain text conclusions and findings printed to stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite store name, check name, source file, line number, category, and concrete numbers when available.]

## Skill Version(s):

1.0.17 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
