## Description: <br>
MILKEE Swiss Accounting lets agents manage MILKEE projects, customers, tasks, products, and billable time for Swiss businesses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xenofex7](https://clawhub.ai/user/xenofex7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Employees and operators at Swiss businesses can use this skill through an agent to list and update MILKEE customers, projects, tasks, products, and daily time entries, including starting and stopping billable timers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and modify MILKEE business accounting data, including customer, project, task, product, and time-entry records. <br>
Mitigation: Install only from a trusted publisher and review create, update, and stop_timer actions before execution. <br>
Risk: The security review notes realistic API-token examples and plaintext credential setup guidance. <br>
Mitigation: Do not reuse example tokens; keep real credentials outside source control, restrict access to any config file containing them, and rotate any token pasted into docs, chat, logs, or screenshots. <br>
Risk: Timer state is persisted locally in the user's home directory and may contain project and work-description metadata. <br>
Mitigation: Protect the local user profile and remove stale timer state when the skill is no longer in use. <br>


## Reference(s): <br>
- [MILKEE API documentation](https://apidocs.milkee.ch/api) <br>
- [MILKEE authentication documentation](https://apidocs.milkee.ch/api/authentifizierung.html) <br>
- [API endpoints reference](references/api-endpoints.md) <br>
- [Configuration guide](references/configuration.md) <br>
- [ClawHub skill listing](https://clawhub.ai/xenofex7/skills/milkee) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Plain text CLI status and results, with shell command examples and configuration snippets in documentation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MILKEE_API_TOKEN and MILKEE_COMPANY_ID; commands can read or modify MILKEE business records.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
