## Description: <br>
Guides agents through building Go services and daemons from the psyb0t/servicepack clone-and-own template, including service scaffolding, lifecycle hooks, dependency ordering, retries, readiness gating, CLI commands, logging, configuration, and graceful shutdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create or extend Go service and daemon projects from the servicepack template, especially when they need concurrent long-running workers, dependency-aware startup, retry behavior, readiness gating, or scaffolded multi-service binaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: `make own` removes the clone's existing git history and rewrites project/module files. <br>
Mitigation: Run `make own` only once, at the start, in a fresh disposable clone of the servicepack template. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/servicepack) <br>
- [Project homepage](https://github.com/psyb0t/servicepack) <br>
- [Setup reference](references/setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Go code examples, shell commands, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.2.15 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
