## Description: <br>
Retrieve and summarize health, sleep, activity, readiness, and biometric data from the Oura Ring API through a command-line interface. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruhrpotter](https://clawhub.ai/user/ruhrpotter) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to authenticate an Oura CLI, run date-scoped Oura API queries, parse returned JSON, and answer user questions about sleep, activity, readiness, heart rate, workouts, and related biometric data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can query and summarize sensitive Oura health and biometric data, and local OAuth tokens are stored on disk. <br>
Mitigation: Install only when this access is acceptable, keep Oura tokens private, restrict local token/config permissions, avoid sharing raw health outputs, and revoke or rotate tokens after machine or log exposure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruhrpotter/skills/oura) <br>
- [Oura Developer Portal](https://cloud.ouraring.com/oauth/developer) <br>
- [Oura CLI repository listed in artifact](https://github.com/ruhrpotter/oura-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and natural-language summaries of JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires absolute YYYY-MM-DD dates for time-series queries and treats CLI JSON data as the source for user-facing summaries.] <br>

## Skill Version(s): <br>
1.0.2 (source: release evidence, released 2026-01-08) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
