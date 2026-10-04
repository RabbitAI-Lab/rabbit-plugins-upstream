## Description:

Guides systematic root-cause debugging of errors, broken or flaky tests, and regressions with evidence-backed verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to reproduce failures, trace their causes, test narrow fixes, and report verification results or unresolved uncertainty.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic reports, commands, and captured artifacts may expose credentials or sensitive project details when shared.

Mitigation: Review and redact paths, hostnames, git remotes, stack traces, tokens, connection strings, customer data, and environment values before sharing.

Risk: Debugging experiments and repairs may change a working tree or be mistaken for a verified fix.

Mitigation: Scope edits to the evidenced cause, preserve existing work, revert disproved experiments, and report fresh reproduction and regression results before claiming repair.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-debugging)
- [Baselines and diagnostic data](references/baseline-and-data-handling.md)
- [Reproduction and investigation](references/reproduction-and-investigation.md)
- [Root cause tracing](references/root-cause-tracing.md)
- [Repair and escalation](references/repair-and-escalation.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Code, Shell commands, Markdown]

**Output Format:** [Markdown debugging report with supporting commands and verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports symptom, root cause or uncertainty, fix or proposed fix, evidence, regression coverage, related findings, and status.]

## Skill Version(s):

5.0.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
