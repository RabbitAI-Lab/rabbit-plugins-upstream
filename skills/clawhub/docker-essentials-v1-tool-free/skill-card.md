## Description: <br>
Helps developers maintain legacy Docker V1 environments with classic container lifecycle, image management, basic Compose V1 orchestration, and compatibility-checking guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to manage containers, images, and docker-compose workflows in legacy Docker V1 environments and to assess readiness for migration to Docker V2. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can propose Docker commands that stop or delete containers, images, and volumes. <br>
Mitigation: Require explicit user approval before destructive Docker operations such as rm, rmi, prune, docker-compose down -v, or forced container removal. <br>
Risk: The skill can propose commands that push images to registries or run commands as root inside containers. <br>
Mitigation: Review registry targets, credentials, and container privilege level before execution, and restrict root container shell access to intentional maintenance tasks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/docker-essentials-v1-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash, YAML, Dockerfile, and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose Docker and docker-compose commands that operate on local containers, images, volumes, registries, and container shells.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
