## Description: <br>
Manage n8n workflows and automations via API, including listing workflows, activating or deactivating workflows, checking execution status, manually triggering workflows, and debugging automation issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation operators use this skill to create, inspect, test, execute, monitor, and optimize n8n workflows through the n8n API. It is intended for workflow automation maintenance and deployment tasks that may affect live automations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires access to a real n8n API key and base URL. <br>
Mitigation: Use a staging n8n instance or a restricted API key whenever possible, and avoid granting broad production access by default. <br>
Risk: Workflow create, activate, deactivate, and execute operations can change or run live automations. <br>
Mitigation: Require explicit confirmation before these operations on production workflows and review the target workflow ID and payload before running commands. <br>
Risk: Dry-run and testing commands may still trigger live workflow executions. <br>
Mitigation: Treat dry-run and test commands as live executions, and run them against staging workflows or controlled test data. <br>


## Reference(s): <br>
- [n8n API Reference](artifact/references/api.md) <br>
- [n8n API Documentation](https://docs.n8n.io/api/) <br>
- [n8n Documentation](https://docs.n8n.io) <br>
- [n8n Community Forum](https://community.n8n.io) <br>
- [ClawHub skill page](https://clawhub.ai/seanford/skills/n8n) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples, Python API snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires N8N_API_KEY and N8N_BASE_URL; some commands can call a live n8n API when run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
