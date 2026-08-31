## Description:

Converts natural-language schedule requests or itinerary screenshots into Apple Calendar events and Apple Reminders on macOS, with reminder lead times selected by event type.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT

## Use Case:

Mac users use this skill to turn flights, train trips, court dates, meetings, deadlines, social plans, medical appointments, and similar time-based requests into Apple Calendar events and reminder sequences that sync through iCloud. The skill is intended for environments where the user can grant macOS Automation access to Calendar and Reminders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write synced personal Calendar and Reminders data from broad natural-language triggers without an explicit built-in preview step.

Mitigation: Review the parsed title, time, location, notes, target calendar, and reminder list before allowing an agent to run the create scripts.

Risk: The scripts require macOS Automation access to Calendar and Reminders, which grants the calling terminal or agent environment permission to create entries.

Mitigation: Install only in environments where that access is acceptable, and run the setup check to confirm permissions and target list names.

Risk: Wrong calendar or reminder-list names can fall back to the first calendar or default reminder list.

Mitigation: Set the target calendar and reminder list explicitly in local configuration before use.

Risk: Screenshots or travel documents may contain sensitive personal details.

Mitigation: Avoid sending sensitive screenshots unless the environment's vision or OCR handling is acceptable, and omit passenger, ticket, and order identifiers from created notes.

## Reference(s):

- [Event Type and Lead-Time Rules](references/lead-times.md)
- [Project Homepage](https://github.com/cat-xierluo/legal-skills)
- [ClawHub Skill Page](https://clawhub.ai/cat-xierluo/skills/apple-smart-schedule)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown/text with bash command invocations and concise confirmation receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create Apple Calendar events and Apple Reminders on macOS via osascript or remindctl; event and reminder data can sync through iCloud.]

## Skill Version(s):

0.1.2 (source: frontmatter, CHANGELOG, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
