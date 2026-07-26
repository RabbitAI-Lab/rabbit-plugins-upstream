## Description: <br>
AgentMetal helps agents rent a Linux VPS, pay by USDC over x402 or card, SSH in, run commands, and manage the server lifecycle. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luiscosio](https://clawhub.ai/user/luiscosio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use AgentMetal to provision short-lived Linux servers, deploy or run workloads, inspect status, extend leases, and tear servers down through CLI or API workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Billable provisioning or lease extension can create unintended spend. <br>
Mitigation: Require explicit approval before provisioning, extending, adding storage or bandwidth, and monitor billing and lease expiration. <br>
Risk: Raw remote command execution can make high-impact changes on a provisioned server. <br>
Mitigation: Require explicit approval and review command text before exec actions; limit account and API key access to intended servers. <br>
Risk: Destructive lifecycle actions can remove running infrastructure. <br>
Mitigation: Require explicit approval before destroy, pause, or other lifecycle actions. <br>


## Reference(s): <br>
- [AgentMetal homepage](https://agentmetal.dev) <br>
- [AgentMetal agent-facing manual](https://api.agentmetal.dev/llms.txt) <br>
- [ClawHub skill page](https://clawhub.ai/luiscosio/skills/agentmetal) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May output API request examples, CLI commands, server identifiers, SSH connection strings, status JSON, stdout, stderr, and error messages.] <br>

## Skill Version(s): <br>
0.3.2 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
