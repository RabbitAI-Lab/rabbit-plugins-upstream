## Description:

Turns school or work timetable files into a shareable HTTPS ICS calendar subscription with one travel alarm per day and a WeChat, iOS, and Android landing page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eggyrooch-blip](https://clawhub.ai/user/eggyrooch-blip)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and calendar maintainers use this skill to convert school, class, office-hour, or work timetables into HTTPS ICS subscriptions and landing pages that subscribers can add once and refresh later.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A hosted ICS URL can expose timetable names, room details, notes, and recurring-location information to anyone with the link.

Mitigation: Remove unnecessary personal or location details, and use access-controlled or hard-to-guess HTTPS hosting for private schedules.

Risk: Calendar subscriptions may fail or refresh incorrectly if the hosted path, MIME type, or landing-page links are misconfigured.

Mitigation: Verify the slash redirect, landing page, text/calendar response, event count, and alarm count before telling users the subscription works.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eggyrooch-blip/skills/calendar-subscribe)
- [Landing page template](references/landing.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands, generated ICS text, HTML, and hosting configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses python3; CSV input is supported directly and XLSX input requires openpyxl in the runtime environment.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
