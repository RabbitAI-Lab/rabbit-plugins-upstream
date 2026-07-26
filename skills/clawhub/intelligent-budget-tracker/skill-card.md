## Description: <br>
A TypeScript library for AI agents to track expenses, income, budgets, savings goals, recurring transactions, reports, and LLM-powered insights. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[enjuguna](https://clawhub.ai/user/enjuguna) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and AI agent builders use this skill to integrate programmatic budget tracking, income tracking, savings goals, recurring transactions, analytics, reports, exports, and backups into agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive financial information. <br>
Mitigation: Use a private storage path with appropriate filesystem permissions, protect exports and backups, and avoid entering account numbers, credentials, or unnecessary identifiers. <br>
Risk: The skill requires installing an external npm package. <br>
Mitigation: Verify the npm package publisher and version before installation. <br>
Risk: Agent actions can add transactions, process recurring entries, generate insights, export data, or create backups. <br>
Mitigation: Keep explicit control over when these actions run and review financial outputs before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/enjuguna/skills/intelligent-budget-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with TypeScript examples, bash installation commands, and JSON-like result structures.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces or manages local financial records, reports, exports, and backups through the agent-money-tracker library.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
