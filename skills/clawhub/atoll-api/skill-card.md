## Description: <br>
Legacy compatibility alias for the Atoll skill. Prefer installing the `atoll` skill for new OpenClaw / ClawHub setups. This alias still provides Atoll project management API and CLI guidance for tasks, projects, goals, KPIs, initiatives, milestones, comments, members, teams, labels, dependencies, automation, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[doubledipcode](https://clawhub.ai/user/doubledipcode) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate Atoll project-management workflows through the Atoll CLI, API, or MCP server. It supports task, project, goal, KPI, initiative, milestone, comment, member, team, label, dependency, automation, and webhook guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide broad project-management actions when supplied with powerful Atoll credentials. <br>
Mitigation: Use a narrowly scoped Atoll agent key and prefer project-scoped access for routine work. <br>
Risk: Delete, billing, webhook, member, and key-management actions can affect organization state or access. <br>
Mitigation: Review these actions before running them and use dry-run or confirmation flows where available. <br>
Risk: Secrets or sensitive business and customer data could be exposed through prompts, comments, feedback, or draft files. <br>
Mitigation: Keep API keys, bearer tokens, cookies, raw third-party responses, and sensitive data out of model-visible text and feedback reports. <br>


## Reference(s): <br>
- [Atoll API Endpoint Reference](artifact/references/api-endpoints.md) <br>
- [Atoll API Field Reference](artifact/references/api-fields.md) <br>
- [Atoll Base URL](https://atollhq.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with inline shell, JSON, and HTTP examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include Atoll CLI commands, API endpoint guidance, configuration snippets, and operational recommendations.] <br>

## Skill Version(s): <br>
1.0.17 (source: server release evidence, released 2026-08-03T05:42:51.939Z) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
