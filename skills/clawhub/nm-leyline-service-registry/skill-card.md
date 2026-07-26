## Description: <br>
Registers external services with health checks, central config, and unified execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to design or use a registry for coordinating multiple external AI or service CLIs with shared configuration, health checks, quotas, failover, and unified execution results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad local command execution through configured external service CLIs can run unintended binaries or commands. <br>
Mitigation: Restrict service commands to trusted binaries and review generated command templates before execution. <br>
Risk: Prompt or file routing through failover and parallel execution can send sensitive content to unexpected third-party providers. <br>
Mitigation: Approve the destination service before sending prompts or files, avoid sensitive files unless explicitly approved, and review failover or parallel execution flows. <br>


## Reference(s): <br>
- [Service Configuration](modules/service-config.md) <br>
- [Execution Patterns](modules/execution-patterns.md) <br>
- [Leyline plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with Python, YAML, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes registry, health check, service selection, retry, failover, and parallel execution patterns.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
