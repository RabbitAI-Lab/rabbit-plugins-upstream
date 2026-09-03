## Description:

Systematic root-cause debugging with verification for errors, stack traces, broken tests, flaky tests, regressions, and other unexpected behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to debug failing software systematically: reproduce the issue, form evidence-backed hypotheses, trace root cause, fix at the source, and verify the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Debugging artifacts such as diagnostic reports, CI logs, stack traces, repository remotes, absolute paths, or environment-derived output may contain sensitive project information.

Mitigation: Review and redact diagnostic reports and logs before sharing them outside the local workspace.

Risk: The skill may guide an agent to run tests, inspect git state, and collect local diagnostics as part of troubleshooting.

Mitigation: Use it only in workspaces where those actions are acceptable, and review proposed commands before execution when the environment is sensitive.

## Reference(s):

- [Competing Hypotheses](references/competing-hypotheses.md)
- [Defense in Depth](references/defense-in-depth.md)
- [Root Cause Tracing](references/root-cause-tracing.md)
- [Specialized Patterns](references/specialized-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands, code references, and debugging reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include diagnostic reports and verification evidence; sensitive logs and environment-derived output should be redacted before sharing.]

## Skill Version(s):

4.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
