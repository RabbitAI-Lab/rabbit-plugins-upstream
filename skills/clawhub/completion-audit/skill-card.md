## Description:

Independently audits claimed task outcomes by deriving completion criteria and checking fresh evidence before work is declared complete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, reviewers, and agent operators use this skill to audit whether a claimed task result is actually complete. It is suited for acceptance checks where completion must be tied to observable criteria, source artifacts, logs, tests, or direct system evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to inspect local task artifacts when auditing a completion claim.

Mitigation: Limit the audit to evidence relevant to the stated completion criteria and avoid exposing sensitive values in the returned evidence summary.

Risk: A completion claim may be marked NOT PROVEN when authoritative evidence is unavailable, even if the work was likely completed.

Mitigation: Record the missing verification source explicitly and rerun the audit when the relevant tests, logs, database checks, or system access become available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/raguets/skills/completion-audit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Markdown audit with criteria, evidence, statuses, verdict, and remaining work]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No code execution, persistence, credential handling, or network behavior is described by the security evidence.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter metadata.version is 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
