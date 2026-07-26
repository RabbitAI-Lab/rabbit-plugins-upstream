## Description: <br>
Access Garmin Connect health, fitness, and activity data via a non-interactive CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[voydz](https://clawhub.ai/user/voydz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to query Garmin Connect health, fitness, device, activity, workout, and training data through the `gc` command-line tool. It can also guide authenticated commands that download activity files, upload activities, create or modify workouts, and call Garmin Connect API endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose sensitive Garmin health, fitness, activity, and account data through authenticated CLI commands and file outputs. <br>
Mitigation: Install only if the user trusts the external garmin-cli package; avoid putting Garmin passwords, MFA codes, or sensitive data in prompts, shell history, scripts, logs, or transcripts. <br>
Risk: Some commands can change remote Garmin account state, including uploads, workout create/update/delete operations, and raw API POST requests. <br>
Mitigation: Require explicit user approval before uploads, workout mutations, file outputs containing sensitive data, or raw API POST commands. <br>


## Reference(s): <br>
- [Garmin Cli on ClawHub](https://clawhub.ai/voydz/skills/garmin-cli) <br>
- [Publisher profile: voydz](https://clawhub.ai/user/voydz) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with bash examples and optional JSON or table command output from `gc`.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [`gc` binary required; commands may access Garmin account data, write output files, upload activities, modify workouts, or call raw API endpoints.] <br>

## Skill Version(s): <br>
1.0.5 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
