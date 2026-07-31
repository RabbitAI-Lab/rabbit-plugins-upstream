## Description: <br>
Railway (railway.com). Use this skill for ANY Railway request — reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Railway projects, services, deployments, logs, and environment variables through an OOMOL-connected Railway account. They can also trigger deployments, update variables, and request rollbacks when those state-changing actions have been reviewed and approved. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change Railway resources by triggering deployments, updating variables, or rolling back deployments through the connected OOMOL account. <br>
Mitigation: Review the exact action, target project or service, environment, and payload before approving write or destructive commands. <br>
Risk: Rollback actions can overwrite the currently running service state. <br>
Mitigation: Require explicit user approval for the rollback target and use Railway-provided rollback-capability information before execution. <br>


## Reference(s): <br>
- [ClawHub Railway skill page](https://clawhub.ai/oomol/skills/oo-railway) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Railway homepage](https://railway.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces oo CLI commands and guidance for Railway connector actions; command responses may include JSON returned by the connector.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
