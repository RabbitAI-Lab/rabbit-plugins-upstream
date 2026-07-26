## Description: <br>
Track and analyze cycling performance from Strava for ride data, fitness trends, workout performance, and cycling training insights. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ericrosenberg](https://clawhub.ai/user/ericrosenberg) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Cyclists, coaches, and agents supporting fitness analysis use this skill to connect to Strava, fetch virtual rides, summarize power and heart-rate metrics, estimate training load, track personal records, and optionally monitor for new rides. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests Strava read access to private activity and profile data. <br>
Mitigation: Authorize it only for users who accept that access, and revoke the Strava application authorization when the skill is no longer needed. <br>
Risk: Strava client secrets and OAuth tokens are stored locally under ~/.config/strava. <br>
Mitigation: Use the skill only on trusted machines, keep the config file private, and delete ~/.config/strava when decommissioning or using shared systems. <br>
Risk: Activity data is cached locally under ~/.cache/strava. <br>
Mitigation: Treat cached ride data as personal data and remove ~/.cache/strava when stopping use or transferring the machine. <br>
Risk: Optional cron monitoring can repeatedly poll Strava and run ride analysis in the background. <br>
Mitigation: Enable cron monitoring only when continuous checks are wanted, and remove the crontab entry to stop background processing. <br>


## Reference(s): <br>
- [Strava API Reference](references/api.md) <br>
- [Strava Developers API Documentation](https://developers.strava.com/docs/reference/) <br>
- [ClawHub skill page](https://clawhub.ai/ericrosenberg/skills/strava-cycling-coach) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-style ride summaries, terminal text, optional JSON, and setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include power, heart-rate zones, TSS estimates, PR summaries, cached activity data, and optional notification text.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
