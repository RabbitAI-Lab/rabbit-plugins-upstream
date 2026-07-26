## Description: <br>
Manage n8n workflows and automations via API. Use when working with n8n workflows, executions, or automation tasks - listing workflows, activating/deactivating, checking execution status, manually triggering workflows, or debugging automation issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thomasansems](https://clawhub.ai/user/thomasansems) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operations teams use this skill to create, validate, execute, monitor, debug, and optimize n8n workflows through the n8n API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can exercise API-level control over a live n8n instance and may change or trigger business workflows. <br>
Mitigation: Use a staging instance or least-privileged API key where possible, and review create, execute, activate, deactivate, and delete actions before running them. <br>
Risk: Dry-run testing performs real workflow execution and may trigger external services or expose sensitive test data. <br>
Mitigation: Use non-sensitive sample data and staging workflows for tests before applying workflows to production data or integrations. <br>
Risk: Workflow modifications can disrupt existing automation state or downstream systems. <br>
Mitigation: Deploy new workflows inactive first, keep backups or exports, and monitor initial executions before broad rollout. <br>


## Reference(s): <br>
- [n8n API Reference](references/api.md) <br>
- [n8n Official Docs](https://docs.n8n.io) <br>
- [n8n API Docs](https://docs.n8n.io/api/) <br>
- [n8n Community Forum](https://community.n8n.io) <br>
- [ClawHub Skill Page](https://clawhub.ai/thomasansems/skills/n8n) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API Calls] <br>
**Output Format:** [Markdown guidance with inline shell and Python examples; helper scripts may return JSON responses and text reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires N8N_API_KEY and N8N_BASE_URL; live operations can create, execute, activate, deactivate, and delete workflows.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and changelog, released 2026-02-10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
