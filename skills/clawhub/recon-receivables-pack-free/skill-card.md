## Description:

A local reconciliation and receivables checker that runs 14 built-in checks over client worksheet materials and reports per-client conclusions with source file and line references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, general ledger, and bookkeeping teams use this skill before month-end close to check accounts payable, accounts receivable, bank reconciliation, intercompany, bill, guarantee, performance bond, and petty-cash materials. It helps identify arithmetic and reconciliation issues, missing materials, and checks that were not run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-supplied financial worksheets may contain sensitive business information.

Mitigation: Install and run only if comfortable processing those worksheets locally; evidence.security reports local-only execution without network use, file writes, persistence, or hidden privilege behavior.

Risk: Reconciliation findings may be mistaken for accounting, audit, assurance, or legal conclusions.

Mitigation: Treat output as a reconciliation aid, not an audit opinion; use qualified accounting or audit review for judgmental questions.

Risk: Incomplete materials, deleted headers, or missing section markers can cause checks to be skipped.

Mitigation: Review checks_not_run and sub_checks_not_run before relying on results, and rerun after fixing input structure or adding missing worksheets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/recon-receivables-pack-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON emitted to stdout, with agent-facing Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite client name, check name, source file, line number, category, and severity; insufficient or partial inputs list checks_not_run and sub_checks_not_run.]

## Skill Version(s):

1.0.26 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
