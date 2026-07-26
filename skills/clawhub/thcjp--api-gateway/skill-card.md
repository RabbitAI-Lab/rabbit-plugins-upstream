## Description: <br>
Routes agent requests through Maton's hosted API gateway to connect approved third-party services such as Slack, Gmail, HubSpot, Salesforce, Stripe, Airtable, and Notion with connection management, trigger handling, event replay, and approval guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation builders use this skill to manage third-party API connections, inspect accounts and resources with read-first flows, and prepare approved write or trigger actions through Maton's hosted gateway. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connected service requests and results pass through Maton's hosted gateway. <br>
Mitigation: Install only when that routing is acceptable for the connected services and data, and remove connections or triggers when no longer needed. <br>
Risk: Write, delete, messaging, billing, sharing, scheduling, and webhook actions can create external side effects. <br>
Mitigation: Use read-only checks first, show the target connection, endpoint, request body, and expected result, and require explicit approval before non-GET or high-impact actions. <br>
Risk: API keys and OAuth tokens can be exposed through logs, repositories, or echoed command output. <br>
Mitigation: Use least-privilege OAuth scopes and keep MATON_API_KEY and service tokens out of logs, command transcripts, and source control. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/api-gateway) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>
- [Maton API gateway](https://api.maton.ai/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, HTTP examples, and JSON response shapes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API endpoints, CLI commands, code snippets, and approval checklists; does not create a hosted proxy or credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter says 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
