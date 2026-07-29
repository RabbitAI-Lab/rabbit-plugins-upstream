## Description: <br>
Dokploy (dokploy.com). Use this skill for ANY Dokploy request - reading, creating, updating, and deleting data. Whenever a task involves Dokploy, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Dokploy projects, environments, servers, applications, compose services, databases, domains, deployments, and logs through an OOMOL-connected Dokploy account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write and destructive Dokploy actions can change deployment state or remove configuration and history. <br>
Mitigation: Confirm the exact target, payload, and expected effect before approving state-changing or destructive actions. <br>
Risk: Read actions can expose Dokploy configuration, logs, repositories, deployment information, and other data visible to the connected API key. <br>
Mitigation: Use the skill only with the intended Dokploy account and review retrieved information before sharing it outside the authorized context. <br>
Risk: The skill grants an agent powerful account actions through the OOMOL-connected oo CLI. <br>
Mitigation: Install it only when agent-managed Dokploy operations are intended, and keep connector access scoped to the permissions needed for the task. <br>


## Reference(s): <br>
- [Dokploy homepage](https://dokploy.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dokploy) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON when commands are run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
