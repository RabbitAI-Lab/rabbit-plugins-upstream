## Description: <br>
Interact with Google Calendar via the Google Calendar API - list upcoming events, create new events, update or delete them. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adrianmiller99](https://clawhub.ai/user/adrianmiller99) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to list, create, update, and delete Google Calendar events from a command-line or headless environment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, and delete real Google Calendar events. <br>
Mitigation: Review event IDs and command arguments before running update or delete operations, and use a limited calendar where possible. <br>
Risk: The refresh helper writes and prints a Google access token. <br>
Mitigation: Avoid running the refresh helper on shared systems or logged sessions, and store credentials with restrictive local permissions or a secret manager. <br>
Risk: Calendar access may exceed the minimum needed for a workflow. <br>
Mitigation: Use the narrowest Google Calendar OAuth scope and limit access to the intended calendar. <br>


## Reference(s): <br>
- [Google Calendar API reference](https://developers.google.com/calendar/api/v3/reference) <br>
- [OAuth 2.0 for installed apps](https://developers.google.com/identity/protocols/oauth2/native-app) <br>
- [ClawHub skill page](https://clawhub.ai/adrianmiller99/skills/google-calendar) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [JSON responses printed to stdout, stderr error messages, and Markdown setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Google OAuth credentials and a configured Google Calendar ID or IDs.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
