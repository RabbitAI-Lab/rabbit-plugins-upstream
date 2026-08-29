## Description:

Harvest every ken: ceiling comment into one ledger, so brute-force deferrals get tracked instead of forgotten. One-shot report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rajnandan1](https://clawhub.ai/user/rajnandan1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use ken-debt to scan a repository for ken: comments that mark brute-force ceilings and produce a concise debt ledger with revisit triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository scans may include file paths and comment text that reveal internal implementation details.

Mitigation: Run the skill only in repositories the user intends to inspect, and review the report before sharing it.

Risk: Persisting a ledger changes the workspace.

Mitigation: Write a ledger only after an explicit user request and use a clear destination such as KEN-DEBT.md.

## Reference(s):

- [Project homepage](https://github.com/rajnandan1/ken)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with optional shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only by default; optional ledger file output only when the user requests persistence.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
