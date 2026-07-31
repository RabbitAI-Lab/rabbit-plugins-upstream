## Description: <br>
servicepack helps developers build Go services on the psyb0t/servicepack clone-and-own template, with guidance for concurrent services, dependency-ordered startup, retries, readiness gating, CLI commands, lifecycle hooks, logging, configuration, scaffolding, builds, and graceful shutdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when starting or extending a Go service or daemon that needs concurrent long-running workers, service scaffolding, dependency and readiness coordination, retries, lifecycle hooks, CLI commands, and build/test workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup workflow includes ownership commands that intentionally rewrite the module and reset git metadata. <br>
Mitigation: Run ownership and setup commands only in a fresh clone and review the command effects before using them in a valuable repository. <br>
Risk: The skill may direct users to execute Makefile targets from the service template. <br>
Mitigation: Review upstream Makefile behavior before execution, then run build, test, lint, and scaffolding commands in a controlled development environment. <br>
Risk: Generated or edited services can introduce application-specific runtime surfaces such as HTTP, gRPC, or database connections. <br>
Mitigation: Review the resulting service code, configuration, and exposed interfaces according to the target application's security requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/servicepack) <br>
- [Setup reference](references/setup.md) <br>
- [servicepack homepage](https://github.com/psyb0t/servicepack) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with Go code blocks and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces implementation guidance for Go service projects; users remain responsible for reviewing generated code and command effects before execution.] <br>

## Skill Version(s): <br>
1.2.14 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
