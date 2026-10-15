## Description:

Helps an agent access Apple Music, iCloud Calendar, Contacts and Mail, Apple Maps, WeatherKit, and iTunes search from any operating system.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and their agents use this skill to search Apple media and places, check weather, and manage their own music, calendars, contacts, and email. It is unofficial and not affiliated with Apple.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured credentials grant access to private mail, contacts, calendars and music-library changes.

Mitigation: Configure only needed services and install only if comfortable granting that access.

Risk: An agent could make an unintended change or send an email.

Mitigation: Review the proposed action and confirm sending, deletion and sensitive edits explicitly.

Risk: Mail, contact and calendar content may contain instructions from other people.

Mitigation: Treat account content as data rather than instructions to the agent.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/apple-icloud-mcp)
- [npm package](https://www.npmjs.com/package/apple-icloud-mcp)
- [Source repository linked in the skill](https://github.com/chrischall/apple-icloud-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text with structured Apple service results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain private account information; some changes require explicit confirmation.]

## Skill Version(s):

0.3.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
