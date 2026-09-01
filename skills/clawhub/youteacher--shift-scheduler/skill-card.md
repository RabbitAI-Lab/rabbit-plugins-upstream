## Description:

Generates, reads, manually updates, and exports employee shift schedules through the AI Skills platform API using dates, shifts, employee availability, and labor constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to create and manage shift schedules, review unfilled slots, apply manual changes, and export schedules as structured data, PDF, or CSV.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Employee scheduling inputs and outputs may include sensitive personnel details.

Mitigation: Confirm the organization is allowed to send scheduling data to the AI Skills platform or configure an approved self-hosted API URL, and avoid unnecessary sensitive personnel data.

Risk: Paid schedule generation, update, or export actions can consume platform wallet balance.

Mitigation: Explain paid actions before execution and preserve billing headers such as charged amount, currency, and remaining balance.

Risk: Generated schedules can be partial or contain unfilled slots under the provided constraints.

Mitigation: Clearly report partial status and unfilled entries, and require user review before operational use.

Risk: Manual updates may conflict with a newer schedule version or violate declared constraints.

Mitigation: Show the proposed changes before applying them, use expected_version, and reread the schedule after conflicts instead of silently overwriting.

Risk: Uncertain network status can lead to duplicate scheduling actions.

Mitigation: Use a new idempotency key for each new business action and reconcile uncertain results with the same operation, body, and key.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/shift-scheduler)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API Key configuration](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/API-KEY.md)
- [Operations contract](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/OPERATIONS.md)
- [HTTP requests and task polling](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/HTTP-REQUESTS.md)
- [Behavior and error rules](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/BEHAVIOR-RULES.md)
- [API-KEY.md](references/API-KEY.md)
- [OPERATIONS.md](references/OPERATIONS.md)
- [HTTP-REQUESTS.md](references/HTTP-REQUESTS.md)
- [BEHAVIOR-RULES.md](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown, Files]

**Output Format:** [Markdown guidance with shell commands, JSON API payloads, and links to generated PDF and CSV artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SHIFT_SCHEDULER_API_KEY; optional AI_SKILLS_API_URL can point to an approved self-hosted API root.]

## Skill Version(s):

1.1.1 (source: server release metadata and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
