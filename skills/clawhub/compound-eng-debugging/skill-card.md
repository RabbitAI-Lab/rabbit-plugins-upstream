## Description: <br>
Systematic root-cause debugging with verification for errors, stack traces, broken tests, flaky tests, regressions, and unexpected behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to debug software failures by reproducing issues, forming evidence-grounded hypotheses, tracing root causes, and verifying fixes with tests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent to run local tests and debugging commands. <br>
Mitigation: Review commands before execution and run them only in the intended workspace or project context. <br>
Risk: Diagnostic reports can expose local paths, username, git remote URL, and repository metadata. <br>
Mitigation: Review and redact diagnostic reports before sharing them outside the workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-debugging) <br>
- [Specification](SPEC.md) <br>
- [Analysis of Competing Hypotheses](references/competing-hypotheses.md) <br>
- [Defense-in-Depth Validation](references/defense-in-depth.md) <br>
- [Root Cause Tracing](references/root-cause-tracing.md) <br>
- [Specialized Debugging Patterns](references/specialized-patterns.md) <br>
- [Diagnostic collection script](scripts/collect-diagnostics.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline code and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce debug reports, diagnostic commands, and verification steps; optional diagnostics can generate a local Markdown report containing environment and repository metadata.] <br>

## Skill Version(s): <br>
4.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
