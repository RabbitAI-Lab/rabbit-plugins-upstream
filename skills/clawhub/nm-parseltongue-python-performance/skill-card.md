## Description: <br>
Profiles Python code for performance bottlenecks and memory issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to profile Python applications, identify CPU and memory bottlenecks, apply optimization patterns, and verify improvements with benchmarks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can activate on broad Python performance terms and provide optimization advice when the user did not intend to enter a profiling workflow. <br>
Mitigation: Narrow activation triggers or require the user to confirm that profiling or optimization guidance is desired before applying recommendations. <br>
Risk: The skill references optional third-party profiling and benchmarking tools such as py-spy and pytest-benchmark. <br>
Mitigation: Review each tool before installing it in a project environment and follow local dependency approval practices. <br>
Risk: Optimization suggestions may reduce maintainability or introduce regressions if applied without measurement. <br>
Mitigation: Profile first, benchmark changes, and keep changes that demonstrate measurable improvement without unacceptable memory or behavior regressions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-parseltongue-python-performance) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/parseltongue) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; suggested commands and code should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
