## Description:

Euthyna guides security audit judgment for code, pull requests, changes, and existing vulnerability claims by requiring measured facts, evidence gates, and clear true-positive, false-positive, or inconclusive outcomes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and audit agents use this skill to review code changes, repositories, or vulnerability assertions and produce evidence-backed security audit decisions. It is intended to prevent unsupported findings from being delivered as confirmed vulnerabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification commands and proof-of-concept steps may run on the user's machine.

Mitigation: Review the exact command text before approval, run in a sandbox or temporary container when practical, and use an explicit working directory.

Risk: Audit reports are written to disk and may contain sensitive code-review details.

Mitigation: Choose a safe report location before starting and review the generated report before sharing it outside the audit context.

Risk: The skill documentation is Chinese-only.

Mitigation: Use reviewers or agents that operate reliably in Chinese, or translate the workflow before relying on it for an audit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/modusensus/skills/euthyna)
- [Bug class requirements](references/bug-classes.md)
- [Change audit workflow](references/change-audit.md)
- [Dependency audit workflow](references/dependency-audit.md)
- [Fact contract](references/fact-contract.md)
- [Fact producers](references/fact-producers.md)
- [Meta mechanisms](references/meta-mechanisms.md)
- [Verification gates](references/verification-gates.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code]

**Output Format:** [Markdown audit reports with evidence references, verdict labels, and inline shell commands or code snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires report output to be written to a file and supports gate checks for audit findings.]

## Skill Version(s):

0.4.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
