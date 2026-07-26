## Description: <br>
This skill helps agents suggest personalized activities using weather, local options, entertainment preferences, group profiles, calendar planning, invites, and RSVP tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scottfo](https://clawhub.ai/user/scottfo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and their agents use this skill to choose nights out, stay-home entertainment, date nights, game nights, and group events. The skill can personalize suggestions from stored preferences and help coordinate plans through calendars, reminders, messages, and RSVP tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can store personal preferences, group details, and contact information. <br>
Mitigation: Require the agent to show the exact stored data before saving it, and periodically review or delete data/whatdo/preferences.json and data/whatdo/history.json. <br>
Risk: The skill can propose calendar events, reminders, Telegram messages, and other invitations. <br>
Mitigation: Require the agent to show the event details, recipients, message text, and reminder schedule before taking action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/scottfo/skills/whatdo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown-style conversational recommendations with optional structured preference and history files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include proposed calendar events, reminder schedules, invitation text, RSVP updates, and preference or history updates for user review.] <br>

## Skill Version(s): <br>
2.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
