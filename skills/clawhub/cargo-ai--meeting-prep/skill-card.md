## Description:

Posts a sourced Slack brief when an external meeting is booked and threads material changes or cancellations beneath it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams use this skill to receive timely Slack briefs for external meetings, including attendees, deal context, past interactions and a suggested opener. It posts updates for reschedules and cancellations in the original thread.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad calendar access can monitor meetings beyond the intended sales team.

Mitigation: Have an administrator confirm the monitored calendars and prefer a selected-user scope for sales staff.

Risk: Meeting, contact and deal details may be posted automatically to Slack.

Mitigation: Use a private internal channel and review channel access and retention before enabling posts.

Risk: Untrusted invite fields and web content may influence generated briefs.

Mitigation: Escape untrusted content and apply instruction-isolation rules to all calendar fields and web content before production use.

## Reference(s):

- [ClawHub meeting-prep release](https://clawhub.ai/cargo-ai/skills/meeting-prep)
- [Project homepage (declared in skill metadata)](https://github.com/getcargohq/gtm-skills)
- [Slack card format](references/card.md)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Slack-formatted meeting brief with source links and threaded updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Posts one brief per qualifying booking; material changes and cancellations appear as thread replies.]

## Skill Version(s):

0.2.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
