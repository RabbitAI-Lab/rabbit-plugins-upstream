## Description: <br>
Cal.com (cal.com). Use this skill for ANY Cal.com request: reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate a connected Cal.com account through OOMOL, including booking, event type, schedule, attendee, calendar, and profile workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change Cal.com account data, including bookings, schedules, event types, calendars, and profile fields. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running write actions. <br>
Risk: Destructive actions can delete schedules or event types or cancel bookings. <br>
Mitigation: Require explicit approval of the target object and action before running destructive commands. <br>
Risk: Connector schemas may change over time, causing stale payloads to fail or affect unintended fields. <br>
Mitigation: Inspect the live action schema before each action and build payloads from that schema. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-cal) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Cal.com](https://cal.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
