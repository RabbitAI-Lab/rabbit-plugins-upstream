## Description: <br>
Goenv guides agents in helping Go developers install and use the github.com/psyb0t/goenv library, a two-state ENV-based prod/dev helper with default-to-prod behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add or review a small prod/dev switch in Go applications, including install commands, import examples, and ENV behavior checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The ENV switch only distinguishes exact lowercase dev from prod, so staging, test, empty, or mistyped values resolve to prod. <br>
Mitigation: Confirm that a two-state dev/prod model and default-to-prod behavior match the application's deployment semantics before adopting it. <br>
Risk: The skill guides installation of a third-party Go module. <br>
Mitigation: Review and pin the module as part of normal dependency intake before use in production code. <br>


## Reference(s): <br>
- [Goenv ClawHub skill page](https://clawhub.ai/psyb0t/skills/goenv) <br>
- [goenv repository homepage](https://github.com/psyb0t/goenv) <br>
- [setup & reference](references/setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with Go and shell snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Focuses on the ENV variable, Go toolchain usage, and the library's exact dev/prod behavior.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
