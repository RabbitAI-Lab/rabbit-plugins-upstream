## Description:

Guides evidence-backed code security audits and validates vulnerability claims against six gates before reporting findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to audit code changes, assess security regressions, and verify suspected vulnerabilities. It requires traceable evidence and treats unverified claims as observations rather than confirmed findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit commands may read repository history, coverage, and dependency metadata and write reports containing sensitive code details.

Mitigation: Limit access to authorized repositories and review report contents and destination before sharing.

Risk: Proof-of-concept and verification commands may execute locally.

Mitigation: Review and explicitly approve each command before execution; prefer an isolated environment.

Risk: The separately installed euthyna CLI is not included in the skill package.

Mitigation: Verify the CLI's provenance before installing or running it; mark measurements unavailable if the tool cannot be trusted or obtained.

## Reference(s):

- [ClawHub release](https://clawhub.ai/modusensus/skills/euthyna)
- [Verification gates](references/verification-gates.md)
- [Fact producers](references/fact-producers.md)
- [Fact contract](references/fact-contract.md)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Shell commands, Guidance]

**Output Format:** [Markdown audit report with evidence citations, verdicts, and reproduction commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings must pass six verification gates; inconclusive claims remain explicitly unverified.]

## Skill Version(s):

0.6.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
