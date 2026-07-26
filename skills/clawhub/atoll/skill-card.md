## Description: <br>
Atoll helps agents interact with Atoll project management through CLI, API, and MCP guidance for tasks, projects, goals, KPIs, initiatives, milestones, comments, members, teams, labels, dependencies, automation, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[doubledipcode](https://clawhub.ai/user/doubledipcode) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, teams, and external agents use Atoll to orient on project state, manage tasks and comments, and keep goals, KPIs, initiatives, and milestones synchronized through the CLI, HTTP API, or MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents through creating, updating, commenting on, archiving, and in some roles deleting Atoll business data. <br>
Mitigation: Create least-privilege Atoll agent keys scoped to the intended org and project, and review admin, billing, webhook, automation, and permanent-delete actions before execution. <br>
Risk: Prompts, comments, issue descriptions, or draft files could accidentally expose API keys, bearer tokens, cookies, or other secret values. <br>
Mitigation: Keep secrets out of model-visible text, use secret references for integrations, and rotate any credential that was pasted into chat or generated artifacts. <br>
Risk: Direct CLI or API operations may change project-management records immediately when run with valid credentials. <br>
Mitigation: Start with read-only orientation commands, use dry-run options where available, and require explicit human review for bulk changes, admin-scoped operations, and permanent deletion. <br>


## Reference(s): <br>
- [Atoll Skill on ClawHub](https://clawhub.ai/doubledipcode/skills/atoll) <br>
- [Atoll API Endpoint Reference](references/api-endpoints.md) <br>
- [Atoll API Field Reference](references/api-fields.md) <br>
- [Atoll API Base URL](https://atollhq.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline bash, JSON, and HTTP examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Atoll API calls and CLI commands that affect project-management data when executed with credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
