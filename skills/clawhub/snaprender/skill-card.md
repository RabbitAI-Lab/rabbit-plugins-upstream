## Description:

SnapRender lets agents capture web pages as screenshots, read them as markdown, and watch for changes through its API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[user0856](https://clawhub.ai/user/user0856)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use SnapRender to capture and compare website screenshots, extract page text, and monitor a page for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target URLs, screenshots, and extracted page content are sent to SnapRender.

Mitigation: Avoid internal, authenticated, confidential, regulated, or non-consensual targets unless the user explicitly approves.

Risk: Page watching can persist remotely and send email alerts.

Mitigation: Confirm the exact URL, notification settings, and how to disable the schedule before creating one.

## Reference(s):

- [SnapRender skill on ClawHub](https://clawhub.ai/user0856/skills/snaprender)
- [SnapRender agent integration](https://snap-render.com/ai-agents)
- [SnapRender documentation](https://snap-render.com/docs)

## Skill Output:

**Output Type(s):** [Files, Markdown, Text, Shell commands, Configuration guidance]

**Output Format:** [Screenshot image or PDF files, extracted text or markdown, and API command examples]

**Output Parameters:** [1D text; 2D screenshots]

**Other Properties Related to Output:** [Scheduled page monitoring can send email notifications.]

## Skill Version(s):

1.6.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
