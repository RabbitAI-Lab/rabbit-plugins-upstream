## Description: <br>
Luma Event Manager for Clawdbot discovers Luma events by topic or location, supports RSVP and guest-list workflows with user cookies, and can sync events to Google Calendar. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mariovallereyes](https://clawhub.ai/user/mariovallereyes) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and event operators use this skill to search Luma events, review hosted or RSVP'd events, inspect authorized guest lists, submit RSVP responses, and add selected events to Google Calendar. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Luma session cookies grant access to private account data. <br>
Mitigation: Store cookies only in pass, treat them like passwords, and remove or rotate them if the skill is no longer trusted. <br>
Risk: RSVP and calendar-sync commands can change Luma or Google account data. <br>
Mitigation: Run these commands only when the user explicitly intends to RSVP or create a calendar entry. <br>
Risk: Guest-list access may expose private attendee information. <br>
Mitigation: Use guest-list features only for events the user is authorized to manage. <br>
Risk: Web scraping can fail if Luma changes page structure or applies rate limits. <br>
Mitigation: Review returned warnings or errors before relying on results, and avoid heavy automated use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mariovallereyes/skills/luma-event-manager) <br>
- [Luma](https://lu.ma) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown and structured text responses, with shell commands for setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return event lists, event details, RSVP status, guest-list summaries, calendar-sync status, or setup instructions.] <br>

## Skill Version(s): <br>
2.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
