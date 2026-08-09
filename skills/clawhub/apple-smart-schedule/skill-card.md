## Description: <br>
Turns natural-language schedule requests or ticket screenshots into macOS Apple Calendar events and Apple Reminders, using event-type rules to calculate advance reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cat-xierluo](https://clawhub.ai/user/cat-xierluo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External macOS users use this skill to convert flights, train trips, court dates, meetings, deadlines, social plans, and similar schedule inputs into Apple Calendar events and reminder sequences. It is intended for local Apple Calendar and Reminders workflows that sync through iCloud to the user's iPhone or iPad. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create entries in a user's personal Apple Calendar and Reminders. <br>
Mitigation: Install it only for macOS calendar and reminder workflows, and review the default calendar and reminder list before first use. <br>
Risk: Vague schedule requests can be interpreted with the wrong date, time, or destination calendar. <br>
Mitigation: Confirm interpreted dates, times, and target lists before creating entries when the request is ambiguous. <br>
Risk: Calendar and reminder contents may include personal information. <br>
Mitigation: Keep parsing local and avoid sending calendar or reminder details to network services or third parties. <br>


## Reference(s): <br>
- [Event Type and Lead-Time Rules](references/lead-times.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/cat-xierluo/skills/apple-smart-schedule) <br>
- [Project Homepage](https://github.com/cat-xierluo/legal-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell commands and concise status receipts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates Apple Calendar events and Apple Reminders on macOS after the agent parses user-provided schedule details.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter, changelog, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
