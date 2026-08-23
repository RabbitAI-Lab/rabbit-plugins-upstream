## Description: <br>
Essential Docker commands and workflows for container management, image operations, and debugging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill as a Docker command reference for container lifecycle work, image management, Docker Compose workflows, networking, volumes, system cleanup, and debugging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Docker removal, prune, volume, and compose-down examples can delete containers, images, volumes, or other Docker resources. <br>
Mitigation: Review commands before running them, confirm targets and flags, and avoid destructive cleanup commands on systems with important unsaved Docker state. <br>
Risk: Example database commands include placeholder credentials. <br>
Mitigation: Replace placeholders with secure secret handling appropriate for the deployment environment. <br>


## Reference(s): <br>
- [Docker documentation](https://docs.docker.com/) <br>
- [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) <br>
- [Compose file reference](https://docs.docker.com/compose/compose-file/) <br>
- [Docker binary requirement](artifact/_meta.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline bash, Dockerfile, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Docker command-line tooling for examples that users choose to run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact/_meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
