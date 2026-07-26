## Description: <br>
Debug running Docker containers and Compose services. Use when inspecting container logs, exec-ing into running containers, diagnosing networking issues, checking resource usage, debugging multi-stage builds, troubleshooting health checks, or fixing Compose service dependencies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gitgoodordietrying](https://clawhub.ai/user/gitgoodordietrying) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to troubleshoot Docker containers and Compose services by inspecting logs, running diagnostic shell commands, checking networking and resource usage, and debugging builds and health checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Docker logs, copied files, and environment inspection can expose secrets or sensitive operational details. <br>
Mitigation: Confirm the target container, image, network, or Compose project before running examples; redact secrets before sharing logs, environment output, or copied configuration. <br>
Risk: Root shells, nsenter, and namespace-sharing debug containers can increase access to container or host resources. <br>
Mitigation: Use least-privilege debugging first and reserve root or namespace-sharing access for cases where normal container inspection is insufficient. <br>
Risk: Docker prune examples can remove unused resources, and volume pruning can delete data. <br>
Mitigation: Review what Docker will remove before cleanup and avoid volume pruning unless the data is confirmed disposable or backed up. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gitgoodordietrying/skills/container-debug) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline bash, Dockerfile, and YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Docker CLI availability in the user's environment; commands should be reviewed and adapted before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
