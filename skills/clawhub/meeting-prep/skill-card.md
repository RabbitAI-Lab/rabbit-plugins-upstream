## Description: <br>
Automated meeting preparation and daily commit summaries. Use when checking Google Calendar for upcoming meetings, generating standup updates from GitHub commits, or sending daily development summaries. Pulls meeting schedules and commit history, then formats verbose developer-friendly updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hougangdev](https://clawhub.ai/user/hougangdev) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering teams use this skill to prepare for upcoming meetings from calendar events, generate commit-based standup updates, and produce end-of-day summaries across repositories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests access to sensitive calendar and repository data. <br>
Mitigation: Use read-only Google Calendar scopes where possible, fine-grained GitHub tokens limited to required repositories, and locked-down credential files or a secret manager. <br>
Risk: Scheduled sending can expose meeting or commit details to unintended destinations. <br>
Mitigation: Require explicit allowlists for repositories, calendars, developers, and message destinations, plus opt-in before scheduled summaries are sent. <br>
Risk: Broad token scopes can expand the impact of a leaked credential. <br>
Mitigation: Avoid classic broad GitHub tokens when narrower fine-grained tokens are available and rotate stored credentials regularly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hougangdev/skills/meeting-prep) <br>
- [Publisher profile](https://clawhub.ai/user/hougangdev) <br>
- [Google Calendar API calendar events endpoint](https://www.googleapis.com/calendar/v3/calendars/primary/events?timeMin=$NOW&timeMax=$LATER&singleEvents=true) <br>
- [Google OAuth token endpoint](https://oauth2.googleapis.com/token) <br>
- [GitHub organization repositories endpoint](https://api.github.com/orgs/ORG_NAME/repos?per_page=50&sort=pushed) <br>
- [GitHub commits endpoint](https://api.github.com/repos/ORG/REPO/commits?since=$SINCE&per_page=30) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Plain text summaries with shell command examples and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Meeting updates and daily summaries are grouped by repository and subdirectory and include author names.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
