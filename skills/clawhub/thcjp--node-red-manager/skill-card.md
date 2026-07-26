## Description: <br>
Node Red Manager helps an agent administer Node-RED instances through Admin API, CLI, and Docker-oriented workflows for flows, nodes, backups, runtime diagnostics, and context values. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when an agent needs to inspect or operate a specific Node-RED deployment, including listing flows, deploying or updating flow JSON, backing up and restoring flows, installing or managing nodes, reading diagnostics, changing context values, or restarting the related Docker service. <br>

### Deployment Geography for Use: <br>
Deploy only in regions and environments where the user is authorized to administer the target Node-RED instance and handle its credentials, flow data, logs, and backups. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable high-impact Node-RED changes such as deploy, delete, restore, install, disable, remove, context updates, and Docker restarts. <br>
Mitigation: Require explicit approval before any mutating operation and preview the target flow, node, context key, backup file, or Docker service before execution. <br>
Risk: Broad activation terms and embedded instance details can cause the agent to act on the wrong Node-RED deployment. <br>
Mitigation: Narrow trigger phrases for local use and confirm the Node-RED URL, Docker service, and ownership of the instance before running commands. <br>
Risk: Node-RED credentials, logs, flow definitions, backups, and context values may contain sensitive operational data. <br>
Mitigation: Protect admin credentials, avoid exposing secrets in logs or generated output, and store backups only in approved locations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/node-red-manager) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, command proposals, environment-variable guidance, and JSON file references for Node-RED flows, backups, and context values.] <br>
**Output Parameters:** [Node-RED URL, admin username and password, flow IDs, node package names, backup file paths, context scopes and keys, Docker service name, and requested operation.] <br>
**Other Properties Related to Output:** [Outputs can lead to Admin API calls, CLI operations, Docker restarts, flow deployment, node installation or removal, and context changes; review proposed operations before applying them.] <br>

## Skill Version(s): <br>
1.0.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
