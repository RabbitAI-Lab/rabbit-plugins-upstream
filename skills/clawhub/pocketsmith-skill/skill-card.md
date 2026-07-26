## Description: <br>
Manage PocketSmith transactions, categories, and financial data via the API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lextoumbourou](https://clawhub.ai/user/lextoumbourou) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to inspect PocketSmith financial data, manage transactions and categories, review budgets, and optionally perform write actions when explicitly enabled. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read sensitive PocketSmith financial data through a developer key. <br>
Mitigation: Install only when the agent is trusted with that data, and provide POCKETSMITH_DEVELOPER_KEY through the host environment or secret mechanism. <br>
Risk: Optional create, update, delete, and forecast-cache operations can change real financial records. <br>
Mitigation: Keep POCKETSMITH_ALLOW_WRITES unset unless intentionally making changes, and verify transaction, category, user, and scenario IDs before write commands. <br>


## Reference(s): <br>
- [PocketSmith API Reference](https://developers.pocketsmith.com/reference) <br>
- [PocketSmith API Base URL](https://api.pocketsmith.com/v2) <br>
- [ClawHub Skill Page](https://clawhub.ai/lextoumbourou/skills/pocketsmith-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; CLI commands output JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires POCKETSMITH_DEVELOPER_KEY. Write operations require POCKETSMITH_ALLOW_WRITES=true.] <br>

## Skill Version(s): <br>
v1.0.0 (source: server release and pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
