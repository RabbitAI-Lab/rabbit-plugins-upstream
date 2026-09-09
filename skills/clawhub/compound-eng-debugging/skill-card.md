## Description:

Systematic root-cause debugging with verification for errors, stack traces, broken tests, flaky tests, regressions, and other failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to reproduce failures, evaluate competing root-cause hypotheses, make narrow repairs when authorized, and report verification evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic reports and pasted probe output may contain local system, repository, path, username, hostname, IP address, token, customer data, SQL fragment, or environment details.

Mitigation: Review and redact diagnostic reports and command output before sharing them in chat, bug reports, or external searches.

Risk: The bundled diagnostic script can collect system information, Git state, remotes, working directory, runtime versions, package managers, and selected environment values.

Mitigation: Run diagnostics only within the caller's authority and treat generated reports as sensitive until reviewed.

## Reference(s):

- [Baselines and diagnostic data](references/baseline-and-data-handling.md)
- [Reproduction and investigation](references/reproduction-and-investigation.md)
- [Root Cause Tracing](references/root-cause-tracing.md)
- [Analysis of Competing Hypotheses](references/competing-hypotheses.md)
- [Defense-in-Depth Validation](references/defense-in-depth.md)
- [Repair, escalation, and diagnostic traps](references/repair-and-escalation.md)
- [Specialized Debugging Patterns](references/specialized-patterns.md)
- [Diagnostic collection script](scripts/collect-diagnostics.sh)
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-debugging)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands]

**Output Format:** [Markdown debug report with evidence, verification results, and inline commands or code when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include the seven-field debug report: SYMPTOM, ROOT CAUSE, FIX, EVIDENCE, REGRESSION, RELATED, and STATUS.]

## Skill Version(s):

4.5.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
