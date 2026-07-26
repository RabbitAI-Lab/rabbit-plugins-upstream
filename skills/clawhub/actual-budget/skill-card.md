## Description: <br>
Query and manage personal finances for self-hosted Actual Budget instances via the official Actual Budget Node.js API, including budget queries, transaction imports and exports, account management, categorization, rules, schedules, and bank sync with credentials supplied through environment variables. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thisisjeron](https://clawhub.ai/user/thisisjeron) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technically capable Actual Budget users use this skill to query and manage a self-hosted Actual Budget instance, including transactions, accounts, categories, rules, schedules, and bank sync. It is intended for workflows where credentials are supplied from the runtime environment and sensitive financial output is minimized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Actual Budget credentials, sync IDs, encryption passwords, or financial records could be exposed through chat output or repositories. <br>
Mitigation: Load credentials from environment variables or a private local credentials file, keep them out of public repositories, and redact secrets and sensitive financial details in responses. <br>
Risk: Imports, account changes, rules, schedules, bank sync, or api.sync() can change financial records. <br>
Mitigation: Require explicit user confirmation before mutating operations and summarize intended changes before applying them unless approval was already given. <br>
Risk: Using an incorrect package or weakening TLS could expose budget data or credentials. <br>
Mitigation: Install only the official @actual-app/api package and use trusted CA configuration for self-signed certificates rather than disabling TLS verification. <br>


## Reference(s): <br>
- [Actual Budget Skill on ClawHub](https://clawhub.ai/thisisjeron/skills/actual-budget) <br>
- [Publisher Profile](https://clawhub.ai/user/thisisjeron) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JavaScript and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Final responses should redact secrets and minimize sensitive financial details; mutating operations should be summarized before execution unless the user has already approved them.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
