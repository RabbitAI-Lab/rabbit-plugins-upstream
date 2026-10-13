## Description:

Guides systematic root-cause debugging and verification for errors, failing or flaky tests, and regressions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to reproduce failures, test competing causes, make authorized repairs, and verify that the original problem is resolved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic reports, logs, commands, or external searches may reveal credentials, customer data, hostnames, or local paths.

Mitigation: Review and redact sensitive details before sharing or searching; keep credentials in environment variables rather than command text.

Risk: Debugging may run local tests, add temporary probes, or propose a change before its cause is confirmed.

Mitigation: Authorize execution and edits, keep experiments reversible, remove temporary probes, and verify a repair against the original failure.

## Reference(s):

- [ia-debugging on ClawHub](https://clawhub.ai/iliaal/skills/compound-eng-debugging)
- [Reproduction and investigation](references/reproduction-and-investigation.md)
- [Baselines and diagnostic data](references/baseline-and-data-handling.md)
- [Repair and escalation](references/repair-and-escalation.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands]

**Output Format:** [Markdown with diagnostic findings, verification results, and optional code changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an optional local diagnostic report.]

## Skill Version(s):

5.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
