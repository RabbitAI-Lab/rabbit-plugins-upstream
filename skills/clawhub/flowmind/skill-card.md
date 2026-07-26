## Description: <br>
Manage productivity with FlowMind: goals, tasks with subtasks, notes, people, and tags via REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fancygobot](https://clawhub.ai/user/fancygobot) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and productivity-focused agents use this skill to manage a FlowMind workspace through natural language, including goals, tasks, notes, people, and tags. The skill supports creating, listing, updating, and deleting account data through FlowMind's REST API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access and modify FlowMind productivity data, including goals, tasks, notes, people, and tags. <br>
Mitigation: Store the API key securely, use a revocable or least-privilege key when available, and require explicit confirmation before deleting or bulk-changing workspace data. <br>
Risk: External API access may expose or change account data if credentials are mishandled. <br>
Mitigation: Keep FLOWMIND_API_KEY out of shared logs and files, rotate it if exposed, and review account-changing requests before execution. <br>


## Reference(s): <br>
- [FlowMind API Reference](references/api.md) <br>
- [FlowMind](https://flowmind.life/) <br>
- [FlowMind API v1](https://flowmind.life/api/v1) <br>
- [FlowMind Skill Page](https://clawhub.ai/fancygobot/skills/flowmind) <br>
- [fancygobot Publisher Profile](https://clawhub.ai/user/fancygobot) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with REST request details and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires FLOWMIND_API_KEY for authenticated FlowMind API access.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
