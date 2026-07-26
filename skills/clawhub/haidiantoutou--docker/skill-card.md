## Description: <br>
Docker containers, images, Compose stacks, networking, volumes, debugging, production hardening, and the commands that keep real environments stable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haidiantoutou](https://clawhub.ai/user/haidiantoutou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill for Docker container, image, Compose, networking, volume, debugging, and production hardening guidance during containerized application work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Docker cleanup, prune, publish, and privileged-container commands can affect images, volumes, hosts, or exposed services if run without review. <br>
Mitigation: Inspect suggested commands before execution and confirm backups for important Docker volumes or images before cleanup. <br>
Risk: The skill provides operational guidance rather than executable code, so incorrect command selection could disrupt a real Docker environment. <br>
Mitigation: Review proposed commands and configuration against the target environment before applying them. <br>


## Reference(s): <br>
- [ClawHub Docker Skill Page](https://clawhub.ai/haidiantoutou/skills/docker) <br>
- [Skill Homepage](https://clawic.com/skills/docker) <br>
- [Essential Commands](artifact/commands.md) <br>
- [Compose Traps](artifact/compose.md) <br>
- [Image Building Traps](artifact/images.md) <br>
- [Infrastructure Traps](artifact/infrastructure.md) <br>
- [Security Traps](artifact/security.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and Docker or Compose snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the docker binary when commands are executed; supports linux, darwin, and win32 environments per ClawHub metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
