## Description:

A local audit worksheet checker that runs 14 bundled consistency checks across audited entity workpaper directories and reports per-entity findings with source file and line references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External accounting and audit users can run this skill locally to check audit adjustment workpapers, trial balances, impairment schedules, depreciation and amortization schedules, provisions, cash counts, and penalty or settlement tables. It supports consistency review, not audit judgment or assurance opinions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit workpapers may contain sensitive financial data.

Mitigation: Run the Node-based checker only in an environment approved for the workpapers being reviewed.

Risk: Consistency-check results could be mistaken for audit opinions or accounting judgments.

Mitigation: Treat findings as review signals and have qualified audit or finance personnel evaluate materiality, accounting treatment, and final conclusions.

Risk: Not-run and out-of-scope checks can leave gaps in review coverage.

Mitigation: Review the reported not-run and out-of-scope sections before relying on the result summary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/audit-adjustment-pack-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Terminal text or JSON with per-entity check results, findings, not-run scope, and source file line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally over user-provided audit workpaper text; sample and batch modes are available.]

## Skill Version(s):

1.0.27 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
