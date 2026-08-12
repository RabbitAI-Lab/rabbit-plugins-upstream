## Description: <br>
Helps agents build, debug, harden, and ship Docker containers, images, Compose stacks, and related CI workflows while excluding Kubernetes cluster scheduling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, DevOps engineers, and operators use this skill to create and review Dockerfiles, Compose files, CI build steps, registry workflows, runtime hardening, debugging procedures, and local operational notes for Docker-based systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide Docker command execution, including operations that may change or delete containers, images, networks, or volumes. <br>
Mitigation: Review Docker commands before execution, require explicit confirmation for destructive operations, and name the affected resources before running prune, volume removal, or Compose deletion commands. <br>
Risk: The skill keeps local Docker operations notes under ~/Clawic/data/, including host, volume, registry-pointer, and deploy metadata. <br>
Mitigation: Install only if local operational note storage is acceptable, keep notes on the local machine, and store credential pointers instead of secret values. <br>
Risk: Users may paste registry tokens, SSH keys, image secrets, or other credentials while asking for Docker help. <br>
Mitigation: Do not save pasted secret values; replace them with pointers such as env:, keychain:, 1password:, vault:, or file: references before writing any local note. <br>


## Reference(s): <br>
- [ClawHub Docker Skill Page](https://clawhub.ai/ivangdavila/skills/docker) <br>
- [Clawic Docker Skill Page](https://clawic.com/skills/docker) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code blocks and Docker, Compose, CI, or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Dockerfiles, Compose YAML, Docker CLI commands, CI snippets, troubleshooting steps, and local operational-note updates.] <br>

## Skill Version(s): <br>
1.0.10 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
