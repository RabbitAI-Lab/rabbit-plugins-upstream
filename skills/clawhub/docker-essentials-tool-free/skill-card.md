## Description: <br>
Provides Docker container lifecycle, image, Docker Compose, network, and volume management guidance for developer workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to have an agent propose or run Docker CLI and Docker Compose commands for local containerized development, single-host multi-container applications, and container troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad Docker CLI authority, including destructive cleanup operations that may remove containers, images, networks, or volumes. <br>
Mitigation: Before prune, rm -f, rmi, volume rm, or docker compose down -v actions, require the agent to show the exact target resources and obtain explicit confirmation. <br>
Risk: Docker commands may mount local directories, expose ports, enter containers, or interact with private registry credentials. <br>
Mitigation: Review generated commands before execution, restrict mounts and ports to the intended development scope, and handle private registry credentials outside shared prompts or logs. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Docker CLI commands, Docker Compose YAML, Dockerfile snippets, and troubleshooting guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on local Docker Engine and Docker Compose availability; command execution depends on the host agent's tool permissions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
