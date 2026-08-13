## Description: <br>
Create and manage Docker sandboxed VM environments for safe agent execution when running untrusted code, exploring packages, or isolating agent workloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to create isolated Docker Desktop sandbox VMs for safer agent execution, untrusted package exploration, network policy testing, and reproducible experiments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mounted workspaces can expose selected host files to sandboxed commands. <br>
Mitigation: Use a disposable or carefully chosen workspace when testing untrusted code. <br>
Risk: Outbound network access may remain broader than intended if the sandbox is left in an allow-by-default posture. <br>
Mitigation: Use deny-by-default network rules and allow only required hosts where practical. <br>
Risk: Detached runs can continue without active observation. <br>
Mitigation: Avoid detached runs unless needed, and inspect or stop long-running sandbox work after use. <br>
Risk: Reset and remove commands perform destructive cleanup of sandbox state. <br>
Mitigation: Treat reset and rm commands as destructive operations and confirm the target sandbox before running them. <br>


## Reference(s): <br>
- [Docker Desktop Sandbox Documentation](https://docs.docker.com/desktop/features/sandbox/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash and JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Docker Desktop 4.49+ with the docker sandbox plugin.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
