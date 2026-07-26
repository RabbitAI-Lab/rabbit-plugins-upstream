## Description: <br>
N8n Monitor helps agents check n8n Docker container status, health, recent logs, and CPU and memory usage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smitti7971](https://clawhub.ai/user/smitti7971) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to monitor n8n containers from an agent session, reviewing status, recent logs, health, and resource usage before deciding on operational follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: n8n container logs can contain sensitive workflow payloads, URLs, tokens, or other operational details. <br>
Mitigation: Review log excerpts before sharing them and limit use to environments where agent Docker visibility into the n8n container is acceptable. <br>
Risk: Docker monitoring commands expose container status, health, and resource usage from the host environment. <br>
Mitigation: Run the skill only with the minimum Docker access needed for monitoring and review proposed commands before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smitti7971/skills/n8n-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with simple status tables and inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include recent n8n container logs, health status, and CPU/memory snapshots.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact skill.yaml lists 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
