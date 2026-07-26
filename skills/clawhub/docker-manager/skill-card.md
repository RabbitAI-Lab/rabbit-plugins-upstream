## Description: <br>
Docker Manager helps agents list, start, stop, restart, inspect, remove, and monitor Docker containers and images. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[SxLiuYu](https://clawhub.ai/user/SxLiuYu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to administer Docker containers and images, inspect status and logs, and monitor resource usage through agent-driven shell commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Docker control can stop, restart, delete, prune resources, or execute commands inside containers. <br>
Mitigation: Install only where the agent is trusted with Docker-level control, and confirm exact targets before using stop, restart, rm, rmi, prune, or exec. <br>
Risk: The skill can affect production or sensitive hosts if installed in those environments. <br>
Mitigation: Avoid production or sensitive hosts unless the agent is explicitly approved to administer Docker there. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/SxLiuYu/docker-manager) <br>
- [Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Terminal text, Docker command output, and Markdown command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and docker on the host.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter remains 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
