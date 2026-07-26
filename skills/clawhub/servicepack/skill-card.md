## Description: <br>
servicepack helps developers build Go service or daemon projects from a clone-and-own template with concurrent service management, dependency-ordered startup, readiness gating, retries, CLI commands, logging, and graceful shutdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when starting or extending a Go service project that needs long-running workers, dependency-aware startup, retry behavior, readiness signaling, service-specific commands, and graceful shutdown. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Running make own rewrites the module, removes the existing git history for that clone, and initializes a new repository. <br>
Mitigation: Run make own only once, at the start, in a fresh clone that does not contain work you need to preserve. <br>
Risk: The template owns framework files and update commands can overwrite framework-managed paths. <br>
Mitigation: Keep custom service logic in user-owned service and command files, and avoid hand-editing framework-owned paths described by the skill. <br>
Risk: Generated or custom services may introduce their own network surfaces, credentials, or environment variables. <br>
Mitigation: Review generated services, configuration variables, and deployment-specific behavior before building or deploying the resulting service. <br>


## Reference(s): <br>
- [Setup Guide](references/setup.md) <br>
- [ClawHub servicepack skill page](https://clawhub.ai/psyb0t/skills/servicepack) <br>
- [servicepack repository](https://github.com/psyb0t/servicepack) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code examples and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Go toolchain and is intended to guide changes in a user-owned servicepack clone.] <br>

## Skill Version(s): <br>
1.2.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
