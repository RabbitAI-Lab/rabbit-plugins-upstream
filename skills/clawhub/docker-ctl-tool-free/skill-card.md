## Description: <br>
Helps individual developers inspect local Podman or Docker containers, including status, logs, resource usage, health, and configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to ask an agent for local container inspection workflows, command examples, and troubleshooting guidance for Podman or Docker environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local container inspection can expose sensitive logs, configuration, environment variables, ports, and mounts. <br>
Mitigation: Use only where the agent is authorized to inspect local containers, treat outputs as sensitive, and review results before sharing them. <br>
Risk: Callback, export, write, create, or deployment-management actions can send data out or change local state if used unintentionally. <br>
Mitigation: Avoid callback URLs unless intentional, and manually confirm any create, export, write, or deployment-management action before execution. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell-command examples and structured inspection output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local container status, logs, resource usage, ports, mounts, environment variables, and configuration details.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
