## Description: <br>
Install and use the RunAPI CLI as the universal execution layer for running RunAPI models, checking authentication, passing JSON requests, waiting for tasks, and automating terminal workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to install, authenticate, and operate the RunAPI CLI from local machines, servers, or CI jobs for model execution, pricing, file upload, callback listener, and skill installation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote install scripts and CLI binaries can affect the host environment. <br>
Mitigation: Prefer the Homebrew install path when available, and review remote install scripts before using them in privileged or CI environments. <br>
Risk: RunAPI credentials or listener secrets may persist on disk or appear in process lists when handled unsafely. <br>
Mitigation: Keep RUNAPI_API_KEY in environment-scoped secrets, import tokens through stdin when needed, avoid placing secrets in project config, and remove saved credentials when the host no longer needs them. <br>


## Reference(s): <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [RunAPI models homepage](https://runapi.ai/models) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON/TOML snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes credential-handling guidance and command examples for RunAPI CLI workflows.] <br>

## Skill Version(s): <br>
0.2.12 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
