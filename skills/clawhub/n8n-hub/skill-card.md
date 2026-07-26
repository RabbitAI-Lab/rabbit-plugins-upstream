## Description: <br>
n8n Hub helps agents design reliable n8n workflows and operate workflows or executions through the public REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codedao12](https://clawhub.ai/user/codedao12) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to plan idempotent n8n workflows, produce workflow JSON and runbooks on request, and prepare API lifecycle actions such as listing, activation, deactivation, debugging, and retrying executions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A powerful n8n API key can affect live workflows and expose sensitive tenant data. <br>
Mitigation: Use the least-privilege n8n API key available, prefer a test workspace for changes, and keep secrets outside generated files. <br>
Risk: State-changing API actions such as activation, deactivation, retries, deletes, credential changes, role changes, or project transfers can impact production operations. <br>
Mitigation: Require explicit human confirmation before executing state-changing actions and review generated commands before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/codedao12/skills/n8n-hub) <br>
- [n8n Public API Endpoint Index](assets/endpoints-api.md) <br>
- [n8n Workflow Operations Runbook Template](assets/workflow-lab.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional workflow JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference N8N_API_BASE_URL and N8N_API_KEY environment variables; secrets should remain external.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
