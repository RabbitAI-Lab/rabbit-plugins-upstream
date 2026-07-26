## Description: <br>
Legacy compatibility alias for the Atoll skill that provides Atoll project management API and CLI guidance for tasks, projects, goals, KPIs, initiatives, milestones, comments, members, teams, labels, dependencies, automation, and webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[doubledipcode](https://clawhub.ai/user/doubledipcode) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to work with Atoll project-management workflows through CLI commands, REST API examples, and configuration guidance. It is intended for managing Atoll work items, strategy objects, comments, dependencies, automation, and related operational context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Atoll API keys grant access according to the key's Atoll role and project scope. <br>
Mitigation: Treat keys as sensitive, prefer skill-scoped configuration or auth profiles, and grant only the Atoll role and project access needed. <br>
Risk: The documented workflows can create, update, archive, delete, comment on, and otherwise manage Atoll work items. <br>
Mitigation: Review proposed write actions before execution, use dry-run or archive paths where available, and avoid broad owner/admin credentials unless required. <br>
Risk: KPI sync and integration examples may involve third-party endpoints and secrets. <br>
Mitigation: Use allowlisted HTTPS JSON endpoints, secret references instead of inline secret values, and human-admin review for sync drafts. <br>


## Reference(s): <br>
- [Atoll API Endpoint Reference](references/api-endpoints.md) <br>
- [Atoll API Field Reference](references/api-fields.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/doubledipcode/skills/atoll-api) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON/JSON5 configuration examples, and REST API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Markdown-only skill; no runtime scripts are included.] <br>

## Skill Version(s): <br>
1.0.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
