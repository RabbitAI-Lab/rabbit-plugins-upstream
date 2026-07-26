## Description: <br>
Helps agents query Garmin Connect health and activity data, analyze metrics such as sleep, Body Battery, HRV, heart rate, workouts, routes, and generate dashboards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bolinches](https://clawhub.ai/user/bolinches) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
ClawHub users and agents use this skill to answer natural language questions about Garmin health and workout history, retrieve Garmin Connect data, and produce summaries or charts for personal fitness review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Garmin credentials, session tokens, and health or route data are sensitive personal information. <br>
Mitigation: Use the Clawdbot UI, environment variables, or protected local config instead of exposing credentials in prompts, and remove ~/.clawdbot/garmin/ to revoke saved local session tokens. <br>
Risk: Passing a Garmin password on the command line can expose it through local shell history or process inspection. <br>
Mitigation: Prefer UI, environment, or config-file setup and avoid the documented command-line password option unless the local environment is controlled. <br>
Risk: Health and recovery interpretations can be incomplete or misleading if treated as medical advice. <br>
Mitigation: Present analyses as informational personal fitness summaries and encourage users to seek professional medical guidance for health decisions. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/bolinches/garmin-health-analysis) <br>
- [ClawHub skill page](https://clawhub.ai/bolinches/skills/garmin-health-analysis-2) <br>
- [MCP setup guide](references/mcp_setup.md) <br>
- [python-garminconnect library](https://github.com/cyberjunky/python-garminconnect) <br>
- [Garmin Connect](https://connect.garmin.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, HTML files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON data summaries, and optional HTML chart files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Garmin Connect credentials and Python dependencies; may create local session tokens and dashboard files.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter states 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
