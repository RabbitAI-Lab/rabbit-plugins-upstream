## Description:

Shift Scheduler helps users generate, read, manually update, and export staff schedules using dates, shifts, employee availability, and labor constraints through the AI Skills platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External teams and operations staff use this skill to create, inspect, adjust, and export shift schedules while accounting for employee availability, shift definitions, staffing requirements, and labor constraints. Generated schedules should be reviewed before operational use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Staff names, availability, scheduling constraints, and schedule IDs are processed by the AI Skills platform.

Mitigation: Send only necessary scheduling data, avoid unnecessary personal details, and install only when the platform account and data handling are acceptable.

Risk: Generated schedules can be incomplete, partially successful, or unsuitable for labor, contract, or staffing requirements.

Mitigation: Review generated schedules before use, explicitly check partial and unfilled results, and have the appropriate operations or HR reviewer approve final schedules.

Risk: Generation, update, and export operations can deduct AI Skills platform wallet balance.

Mitigation: Confirm paid operations with the user before executing them and report billing response headers when available.

Risk: Uncertain network results can create duplicate scheduling actions if retried incorrectly.

Mitigation: Use the same Idempotency-Key to reconcile uncertain operations and avoid repeating generation with a changed payload.

## Reference(s):

- [ClawHub shift-scheduler skill page](https://clawhub.ai/youteacher/skills/shift-scheduler)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/API-KEY.md)
- [Operations contract](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/OPERATIONS.md)
- [HTTP requests and task polling](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/HTTP-REQUESTS.md)
- [Behavior and error rules](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request and response fields, and PDF/CSV artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SHIFT_SCHEDULER_API_KEY and curl; schedule generation, update, and export can incur AI Skills platform charges.]

## Skill Version(s):

1.2.0 (source: server release metadata and skill metadata.packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
