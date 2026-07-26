## Description: <br>
Teamcamp lets agents read, create, and update Teamcamp workspace data through the OOMOL oo CLI connector instead of direct API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users who manage Teamcamp workspaces use this skill to list projects, tasks, customers, and users, inspect project or task details, and post task comments with explicit confirmation for write actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Teamcamp trigger wording could cause the skill to be invoked for requests where Teamcamp access was not intended. <br>
Mitigation: Install only when Teamcamp access is intended and be explicit when a request should remain read-only. <br>
Risk: The post_task_comment action changes Teamcamp state. <br>
Mitigation: Confirm the exact task, comment payload, and expected effect with the user before running write actions. <br>


## Reference(s): <br>
- [Teamcamp ClawHub Skill](https://clawhub.ai/oomol/skills/oo-teamcamp) <br>
- [Teamcamp Homepage](https://www.teamcamp.app) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
