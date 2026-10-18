## Description:

Prepares Slack meeting briefs for newly booked external meetings using calendar, account, deal and activity information, and threads material updates or cancellations beneath each brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales representatives and sales leaders use this skill to receive a timely Slack brief about external meeting attendees, open opportunities, previous interactions and a suggested conversation opener. It can also guide developers adapting the example to their organization's calendars, sales data and Slack channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad calendar monitoring can include external meetings outside the intended sales team.

Mitigation: Prefer a selected user scope unless monitoring every calendar is intentional; notify affected users.

Risk: Automatically posted briefs can expose sensitive meeting and deal information to Slack channel members.

Mitigation: Use a tightly controlled internal Slack channel and review access before deployment.

Risk: Unescaped content in Slack posts can alter how meeting details are displayed.

Mitigation: Escape Slack output or use plain-text Block Kit fields before production deployment.

## Reference(s):

- [Meeting Prep on ClawHub](https://clawhub.ai/cargo-ai/skills/meeting-prep)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Meeting card format](references/card.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration guidance]

**Output Format:** [Slack-formatted meeting briefs and threaded updates; Markdown setup guidance and adaptable TypeScript code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One brief per external meeting; reschedules and cancellations appear as replies to the original brief.]

## Skill Version(s):

0.2.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
