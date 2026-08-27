## Description:

Harvest every ken: ceiling comment into one ledger, so brute-force deferrals get tracked instead of forgotten.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rajnandan1](https://clawhub.ai/user/rajnandan1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scan repository comments for ken: debt markers and produce a concise ledger of brute-force ceilings, upgrade triggers, and missing triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning repository comments can surface internal implementation notes or debt markers.

Mitigation: Run the skill only in repositories intended for review and inspect the generated ledger before sharing it outside the project.

Risk: Persisting the ledger creates or updates a repository file when requested.

Mitigation: Keep the default read-only behavior unless a ledger file is explicitly needed, and review the destination path before writing.

## Reference(s):

- [Project homepage](https://github.com/rajnandan1/ken)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [Markdown report with inline shell commands and optional ledger file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only by default; may write a ledger file only when explicitly requested.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
