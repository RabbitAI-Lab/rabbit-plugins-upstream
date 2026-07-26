## Description: <br>
Garmin Connect integration for Clawdbot: sync fitness data (steps, HR, calories, workouts, sleep) every 5 minutes using OAuth. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rayleigh3105](https://clawhub.ai/user/rayleigh3105) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to authenticate with Garmin Connect, sync personal fitness data, cache it locally, and format activity, sleep, and workout metrics for Clawdbot workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Garmin credentials may be passed directly on the command line during authentication. <br>
Mitigation: Avoid putting the Garmin password directly in shell commands; prefer an interactive or browser-based authentication flow where available. <br>
Risk: OAuth session files and cached Garmin fitness data are sensitive local data. <br>
Mitigation: Protect ~/.garth/session.json and Garmin cache files with restrictive local permissions on a trusted single-user machine. <br>
Risk: The cron setup can collect health data continuously every five minutes. <br>
Mitigation: Enable the cron job only when continuous collection is intended, and adjust or disable the schedule when it is no longer needed. <br>
Risk: Temporary logging or cache paths can expose sensitive sync output. <br>
Mitigation: Adjust or remove /tmp logging and cache paths, and store logs only in protected user-owned locations. <br>


## Reference(s): <br>
- [ClawHub Garmin Connect Skill](https://clawhub.ai/rayleigh3105/skills/garmin-connect) <br>
- [Garmin SSO Sign-In](https://sso.garmin.com/sso/signin) <br>
- [Clawdbot](https://clawd.bot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [JSON cache files, formatted Markdown text, Python API calls, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local Garmin OAuth session and writes local cache files containing fitness data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
