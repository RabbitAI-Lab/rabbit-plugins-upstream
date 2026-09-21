## Description:

A local reconciliation and receivables checker that runs 14 built-in checks per client directory and prints one conclusion line per client, with findings citing source files and line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance employees, general ledger accountants, and bookkeeping teams use this skill before monthly close to check reconciliation and receivables materials across multiple client directories. It reports per-client issues, source file references, line numbers, and checks that were not executed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat reconciliation findings as an audit opinion or accounting judgment.

Mitigation: Use the output as a worksheet check only, and have qualified finance or audit reviewers validate conclusions before relying on them.

Risk: Users may overlook checks that are explicitly withheld or not run.

Mitigation: Review the checks_not_run and sub_checks_not_run sections before relying on a result, especially for cross-client summaries and risk ranking.

Risk: Missing, empty, or misformatted client materials can lead to insufficient input or partial coverage.

Mitigation: Verify that each client directory includes the required tables, headers, and segmented materials before treating a run as complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/recon-receivables-pack-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON command output with per-client reconciliation findings and cited source lines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with no network use, no file writes, and explicit not-run check lists when material is missing or outside the free tier.]

## Skill Version(s):

1.0.30 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
