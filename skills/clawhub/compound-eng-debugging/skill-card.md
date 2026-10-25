## Description:

Guides systematic root-cause debugging and verification for errors, failing tests, flaky behavior, and regressions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to reproduce failures, trace root causes, test repairs, and report verification results. It also supports read-only diagnosis when changes are not authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic output may expose credentials, environment values, customer data, or identifying project details when shared.

Mitigation: Review and redact diagnostics, commands, and probe output before sharing them outside the workspace.

Risk: Ad hoc unpinned npx commands may run dependencies outside the project's established workflow.

Mitigation: Prefer existing project test commands over ad hoc unpinned npx commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-debugging)
- [Baselines and diagnostic data](references/baseline-and-data-handling.md)
- [Reproduction and investigation](references/reproduction-and-investigation.md)
- [Root cause tracing](references/root-cause-tracing.md)
- [Competing hypotheses](references/competing-hypotheses.md)
- [Repair and escalation](references/repair-and-escalation.md)
- [Defense in depth](references/defense-in-depth.md)
- [Specialized debugging patterns](references/specialized-patterns.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Code, Shell commands]

**Output Format:** [Markdown with diagnostic findings and optional code or commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports observed symptoms, root cause or uncertainty, fix or proposed fix, evidence, regression coverage, related findings, and status.]

## Skill Version(s):

5.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
