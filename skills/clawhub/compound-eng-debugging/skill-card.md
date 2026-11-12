## Description:

Systematic root-cause debugging with verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to investigate errors, broken or flaky tests, regressions, and other failures. It helps them establish an evidence-backed cause, make authorized repairs, and verify the result or report remaining uncertainty.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic collection may capture credentials or sensitive environment details that could be exposed when logs or reports are shared.

Mitigation: Review what the diagnostic script captures and redact secrets and customer data before sharing outputs.

Risk: The security review found that some described operations do not clearly match the debugging purpose, and the diagnostic script was only partially inspected.

Mitigation: Review the diagnostic script and proposed operations before running them.

## Reference(s):

- [Baseline and data handling](references/baseline-and-data-handling.md)
- [Competing hypotheses](references/competing-hypotheses.md)
- [Defense in depth](references/defense-in-depth.md)
- [Repair and escalation](references/repair-and-escalation.md)
- [Reproduction and investigation](references/reproduction-and-investigation.md)
- [Root cause tracing](references/root-cause-tracing.md)
- [Specialized patterns](references/specialized-patterns.md)
- [Diagnostic collection script](scripts/collect-diagnostics.sh)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Code]

**Output Format:** [Markdown debugging report with evidence, commands, and code changes as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a proposed fix and verification steps; distinguishes diagnosis from verified repair.]

## Skill Version(s):

5.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
