## Description: <br>
Generates exec-support outputs (plan, prioritized tasks, comms drafts, meeting prep/follow-ups). USE WHEN you want a personal assistant to triage requests and produce ready-to-send drafts and schedules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kowl64](https://clawhub.ai/user/kowl64) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Employees and external users use this skill to turn messages, calendar availability, task lists, and meeting notes into prioritized plans, scheduling proposals, meeting prep, follow-ups, and ready-to-send communication drafts. It supports administrative coordination only and does not send messages, book meetings, or provide legal, medical, or financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduling proposals may be unsuitable if timezone, working hours, date range, participants, meeting length, or exceptions are missing or wrong. <br>
Mitigation: Provide explicit scheduling constraints and review proposed times before using them; the skill should stop and ask when critical scheduling details are missing or conflicting. <br>
Risk: Draft communications may contain incorrect assumptions, missing facts, or commitments the user has not approved. <br>
Mitigation: Review every draft before sending and provide missing pricing, policy, decision, attachment, or stakeholder details when requested. <br>
Risk: Pasted admin context can include sensitive personal or business information. <br>
Mitigation: Provide only the messages, notes, calendar details, and task context needed for the requested administrative output. <br>


## Reference(s): <br>
- [PA Output JSON Schema](references/pa-output-json-schema.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kowl64/skills/pa-admin-exec) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown pack plus a JSON object matching the PA output schema] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces drafts and proposals only; scheduling suggestions must respect weekday working hours, an 08:00-17:00 workday, and a latest meeting end time of 16:30.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
