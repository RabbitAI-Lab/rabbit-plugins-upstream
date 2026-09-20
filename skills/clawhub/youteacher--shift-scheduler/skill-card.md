## Description:

Generates, reads, manually updates, and exports shift schedules based on dates, shifts, employee availability, and labor constraints through the AI Skills platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Operations managers, store managers, and scheduling staff use this skill to create and review staff rosters, handle unavailable dates and constraint conflicts, and export private PDF or CSV schedules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Employee scheduling data may contain personal or operationally sensitive information sent to the AI Skills platform or a configured self-hosted endpoint.

Mitigation: Confirm the user is allowed to send the data, minimize unnecessary personal data, keep generated artifacts private, and never expose API keys.

Risk: Generate, update, and export operations can charge the user's AI Skills platform wallet balance.

Mitigation: Explain paid operations before execution and use the product page and billing response headers to confirm actual charges.

Risk: Schedule constraints may produce partial results, unfilled slots, or conflicts that are unsuitable for direct operational use.

Mitigation: Report partial and unfilled states clearly, show manual update changes before applying them, and require user review for labor, contract, and HR compliance.

Risk: Network uncertainty during asynchronous operations can cause confusion about whether a paid action completed.

Mitigation: Poll until a terminal state when possible, reuse the original idempotency key for reconciliation, and avoid creating duplicate schedules when status is unknown.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/shift-scheduler)
- [Publisher profile](https://clawhub.ai/user/youteacher)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [Shift Scheduler product page](https://ai-skills.open-idea.net/skills/shift-scheduler)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/API-KEY.md)
- [Operations contract](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/OPERATIONS.md)
- [HTTP requests and task polling](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/HTTP-REQUESTS.md)
- [Behavior and error rules](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON request details, curl examples, structured schedule summaries, and PDF or CSV artifact references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SHIFT_SCHEDULER_API_KEY and curl; schedule requests are capped at 31 days, 50 employees, 10 shifts, and 1000 slots.]

## Skill Version(s):

1.2.1 (source: server release metadata and skill metadata packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
