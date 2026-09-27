## Description:

Helps agents manage Sunsama tasks, daily plans, calendars, time tracking, and connected email threads through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sunsama users and their agents can find and organize tasks, plan calendar time, track work, and manage email threads in connected accounts. The skill also describes optional functions and triggers for approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved actions can change or delete Sunsama tasks, calendar events, and connected email data.

Mitigation: Default to reading first and confirm each write or deletion with the exact target and intended change.

Risk: API keys and connected personal data may be exposed if handled carelessly.

Mitigation: Prefer OAuth, limit connection access, and avoid displaying or storing credentials and unnecessary response data.

Risk: Functions, triggers, and destinations may continue acting or forwarding data after creation.

Mitigation: Review their behavior and destinations, obtain specific approval, and remove them when no longer needed.

## Reference(s):

- [Sunsama skill release](https://clawhub.ai/byungkyu/skills/sunsama)
- [Maton](https://maton.ai)
- [Sunsama](https://sunsama.com)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command, code, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions require an authorized Sunsama connection; responses may include connected email and calendar data.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
