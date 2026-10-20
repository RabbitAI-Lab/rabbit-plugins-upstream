## Description:

Helps users generate, review, adjust, and export employee shift schedules using availability, staffing needs, and scheduling constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Managers and scheduling staff use this skill to create, inspect, adjust, and export employee shift schedules through the AI Skills platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Employee names, availability, and schedule details are sent to the configured scheduling endpoint.

Mitigation: Use only an approved platform or self-hosted endpoint, and avoid sharing schedules in public messages.

Risk: Successful schedule generation, updates, and exports may incur platform charges.

Mitigation: Review pricing and confirm the user understands charges before paid operations.

Risk: Exposed API keys could allow unauthorized access.

Mitigation: Store keys in environment configuration; never paste full keys into chat or logs.

Risk: Incomplete schedules or unreviewed constraints could lead to staffing or compliance errors.

Mitigation: Disclose unfilled shifts and partial results, and have a person review schedules against applicable rules before use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/youteacher/skills/shift-scheduler)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/API-KEY.md)
- [Scheduling operations](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/OPERATIONS.md)
- [HTTP requests and task polling](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/HTTP-REQUESTS.md)
- [Behavior and error rules](https://ai-skills.open-idea.net/skill-docs/shift-scheduler/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Schedule summaries and structured results; PDF and CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report unfilled shifts, partial results, and pending tasks.]

## Skill Version(s):

1.4.0 (source: server-resolved release and SKILL.md metadata.packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
