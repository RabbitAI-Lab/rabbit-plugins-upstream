## Description: <br>
Goenv helps agents add or explain a tiny Go prod/dev environment switch around `github.com/psyb0t/goenv`, which reads `ENV` and returns `dev` only for the exact value `dev`, otherwise `prod`. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when a Go project needs a small dependency-free way to branch behavior between prod and dev, or when an existing project already imports `github.com/psyb0t/goenv` and needs consistent usage guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The library models only two environments and treats anything other than exact ENV=dev as prod. <br>
Mitigation: Confirm that a two-state prod/dev switch is appropriate before adopting it; use a fuller configuration library when staging, test, CI, or local environments need distinct handling. <br>
Risk: The skill may add a third-party Go module to the user's project. <br>
Mitigation: Review and pin the module as part of normal dependency management, then run go build and go test after integration. <br>
Risk: The exported Type is a string alias and does not provide compile-time enum safety. <br>
Mitigation: Use the provided constants consistently or define stricter project-local validation when arbitrary environment strings must be rejected. <br>
Risk: The artifact notes a Go 1.25 or newer requirement. <br>
Mitigation: Confirm the project toolchain version before installing the dependency. <br>


## Reference(s): <br>
- [goenv setup and reference](references/setup.md) <br>
- [goenv GitHub project](https://github.com/psyb0t/goenv) <br>
- [Goenv ClawHub release page](https://clawhub.ai/psyb0t/skills/goenv) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with Go and shell code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose importing the Go module, setting the ENV variable, and running go get, go build, or go test.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
