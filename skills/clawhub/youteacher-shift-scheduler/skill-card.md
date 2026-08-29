## Description:

Shift Scheduler helps agents generate, read, manually update, and export staff schedules using dates, shifts, employee availability, and labor constraints through the AI Skills Platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create and manage staffing schedules, reconcile manual changes, and export reviewed schedules as structured results, PDF, or CSV files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Employee names, availability, shift rules, and schedule changes are sent to the configured AI Skills API.

Mitigation: Use only the official or otherwise trusted platform endpoint, keep API keys out of chats and logs, and confirm that users are comfortable sharing scheduling data with the service.

Risk: Generated or updated schedules may not satisfy all real-world labor, contract, or staffing requirements.

Mitigation: Review schedules, unfilled slots, partial results, and manual changes before using them for staffing decisions.

Risk: Successful generate, update, and export operations can charge the user's AI Skills Platform balance.

Mitigation: Tell the user before paid actions and check billing response headers for charged amount, currency, and remaining balance.

## Reference(s):

- [AI Skills Platform](https://ai-skills.open-idea.net)
- [Shift Scheduler Product Page](https://ai-skills.open-idea.net/skills/shift-scheduler)
- [API Key Configuration](references/API-KEY.md)
- [Operations Contract](references/OPERATIONS.md)
- [HTTP Requests and Task Polling](references/HTTP-REQUESTS.md)
- [Behavior, Safety, and Error Rules](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request bodies, curl commands, and links to structured schedules, PDF, and CSV artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SHIFT_SCHEDULER_API_KEY and may use AI_SKILLS_API_URL for a trusted platform endpoint.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
