## Description:

Docker核心操作指南 helps agents provide Chinese-language Docker operational guidance across container lifecycle management, image management, Docker Compose, networking, volumes, debugging, and system maintenance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and automation users can use this skill to ask an agent for Docker commands, Compose configuration, troubleshooting steps, and operational guidance. It is most relevant when the user wants help managing local or server Docker environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to propose or execute broad Docker operations, including destructive cleanup, deletion, and volume removal commands.

Mitigation: Require command previews and explicit user approval before deletions, prune operations, docker-compose down -v, network or volume removal, sudo commands, or Docker permission changes.

Risk: Docker commands can materially change the local machine or server environment when run in the wrong context.

Mitigation: Confirm the target Docker host, container names, image names, paths, and port mappings before execution, and prefer read-only inspection commands for diagnosis.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/docker-essentials)
- [Skill Homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown with inline bash, Dockerfile, Docker Compose, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include command sequences, troubleshooting tables, and structured JSON-style result examples.]

## Skill Version(s):

1.0.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
