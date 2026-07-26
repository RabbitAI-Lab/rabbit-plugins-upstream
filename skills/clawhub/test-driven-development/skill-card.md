## Description: <br>
Test-driven development (TDD) for non-trivial behavior: write or update a failing test first, watch it fail with evidence, then write the minimal code to pass while keeping the suite as a living specification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill when implementing real logic, fixing bugs, or changing tested behavior so that tests are written or updated before implementation and validated with explicit red/green evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to execute project tests, which may run arbitrary project code. <br>
Mitigation: Use normal repository safeguards and avoid approving unsandboxed test runs that perform network, publish, destructive, or out-of-repo actions unless those actions are intended. <br>
Risk: The skill can lead an agent to modify tests and implementation code. <br>
Mitigation: Review generated test and code changes before deployment and require explicit command output and exit status for red/green claims. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vincentjiang06/skills/test-driven-development) <br>
- [Skill Specification](SKILL.md) <br>
- [English README](README.en.md) <br>
- [Changelog](CHANGELOG.md) <br>
- [Enforcement Gates](references/enforcement-gates.md) <br>
- [Modify Mode](references/modify-mode.md) <br>
- [Refactor and Legacy](references/refactor-and-legacy.md) <br>
- [Testing Anti-Patterns](references/testing-anti-patterns.md) <br>
- [Trust Boundary](references/trust-boundary.md) <br>
- [Reflow Point](references/reflow-point.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands] <br>
**Output Format:** [Markdown guidance with command examples and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to write or edit tests and code, run targeted test commands, and report command output and exit status.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, changelog, and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
