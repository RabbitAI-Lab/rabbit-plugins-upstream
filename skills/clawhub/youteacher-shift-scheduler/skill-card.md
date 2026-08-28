## Description:

Generates, reads, manually adjusts, and exports employee shift schedules using dates, shifts, member availability, and labor constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operations teams use this skill through ClawHub or OpenClaw to create, inspect, revise, and export workforce schedules. It is useful when schedule data must account for employee availability, staffing needs, rest rules, and unresolved coverage gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Employee names, availability, constraints, and schedule exports may contain staffing data.

Mitigation: Confirm organizational approval before use, prefer employee IDs where practical, avoid unnecessary personal details, and keep exported artifacts private.

Risk: Generate, update, and export operations may charge the AI Skills platform wallet.

Mitigation: Review pricing and billing headers, and tell the user before starting a paid operation.

Risk: A generated schedule can be partial or contain unfilled slots when constraints cannot be satisfied.

Mitigation: Surface partial status and unfilled reasons clearly, do not fabricate assignments, and require user review before operational use.

## Reference(s):

- [API Key Configuration](artifact/references/API-KEY.md)
- [Operations Contract](artifact/references/OPERATIONS.md)
- [HTTP Requests and Task Polling](artifact/references/HTTP-REQUESTS.md)
- [Behavior and Error Rules](artifact/references/BEHAVIOR-RULES.md)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [Shift Scheduler Product Page](https://ai-skills.open-idea.net/skills/shift-scheduler)
- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/youteacher-shift-scheduler)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with inline shell commands, JSON API payloads, structured schedule results, and PDF/CSV artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SHIFT_SCHEDULER_API_KEY; schedule operations may return partial results, unfilled staffing slots, billing headers, and private export artifacts.]

## Skill Version(s):

1.0.0 (source: release metadata and SKILL.md packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
