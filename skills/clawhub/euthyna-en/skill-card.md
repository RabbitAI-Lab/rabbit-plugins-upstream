## Description:

Guides evidence-based code security audits by checking vulnerability claims against six gates and requiring an auditable report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to audit repositories and code changes, verify suspected vulnerabilities, and distinguish supported findings from inconclusive observations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local audit or verification commands may execute against the target project.

Mitigation: Confirm exact commands before execution and use an isolated environment for reproduction when practical.

Risk: The audit writes a persistent report and may target an existing report path on repeated runs.

Mitigation: Confirm the report destination and review or back up any existing file before re-running the audit.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/modusensus/skills/euthyna-en)
- [Verification gates](references/verification-gates.md)
- [Change audit](references/change-audit.md)
- [Fact producers](references/fact-producers.md)

## Skill Output:

**Output Type(s):** [Markdown, Security audit findings, Shell commands, Guidance]

**Output Format:** [Markdown audit report saved to disk, with evidence, verdicts, and reproduction steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings without sufficient evidence are downgraded to observations; unavailable measurements are marked not evaluable.]

## Skill Version(s):

0.6.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
