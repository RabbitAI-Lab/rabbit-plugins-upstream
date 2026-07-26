## Description: <br>
Helps agents build, debug, harden, and ship Docker containers, images, and Compose stacks while avoiding common runtime, networking, storage, CI, registry, and security traps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to write Dockerfiles, Compose files, CI build steps, container commands, and Docker configuration, and to debug single-host Docker or Compose issues. It is not intended for Kubernetes manifests or cluster scheduling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can maintain persistent local Docker and server inventory, including infrastructure details and generated runbooks. <br>
Mitigation: Install only where that local memory behavior is acceptable, and review or require approval before saving, moving, or deleting persistent records on sensitive machines. <br>
Risk: Docker guidance can include destructive operations such as pruning, removing volumes, or changing daemon and deployment configuration. <br>
Mitigation: Review proposed commands before execution, keep destructive confirmations enabled, and verify affected volumes, images, networks, and deploy digests before applying changes. <br>
Risk: Docker access and registry configuration can expose powerful host or credential capabilities. <br>
Mitigation: Use credential helpers or secret references instead of storing secret values in skill memory, and avoid exposing the Docker socket or privileged container flags unless explicitly justified. <br>


## Reference(s): <br>
- [ClawHub Docker skill page](https://clawhub.ai/ivangdavila/skills/docker) <br>
- [Clawic Docker skill homepage](https://clawic.com/skills/docker) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code blocks, Docker CLI commands, Dockerfile and Compose snippets, and configuration examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose updates to local Docker memory files under ~/Clawic/data/docker/ and shared host inventory under ~/Clawic/data/servers/ when durable Docker facts should be recorded.] <br>

## Skill Version(s): <br>
1.0.9 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
