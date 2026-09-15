## Description:

Logs AI incidents such as runaway behavior, mistakes, or hallucinations into a JSONL ledger with severity, model, action, and retrospective fields, and supports list and report summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and AI governance teams use this skill to record and review AI incidents in a local ledger so repeated mistakes, model failures, and follow-up actions can be tracked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The global install command is mutable and may resolve to a different package or version over time.

Mitigation: Install from a trusted source and pin the package version or source commit before deployment.

Risk: Incident descriptions in the JSONL ledger may contain sensitive operational details.

Mitigation: Store the ledger in a private location and avoid recording secrets, credentials, or unnecessary personal data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-incident-log)
- [LGD Hub homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance]

**Output Format:** [Plain text summaries, optional JSON reports, and JSONL ledger records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local filesystem output; zero third-party runtime dependencies.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
