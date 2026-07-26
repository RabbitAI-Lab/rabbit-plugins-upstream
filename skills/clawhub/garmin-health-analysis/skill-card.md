## Description: <br>
Garmin Health Analysis lets agents query Garmin Connect health, recovery, workout, and activity-file data, then return JSON metrics, natural-language trend analysis, and interactive HTML dashboards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eversonl](https://clawhub.ai/user/eversonl) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill with ClawHub or Clawdbot to answer natural-language questions about Garmin health metrics, workouts, recovery trends, and activity files. It supports personal health monitoring, scheduled reports, and dashboards; health interpretations should be treated as informational rather than medical advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Garmin credentials and session tokens can expose the user's account and health data. <br>
Mitigation: Install only on a trusted personal machine, prefer UI-managed secrets or a local secret store, avoid command-line passwords when possible, and protect or revoke local token files when access is no longer needed. <br>
Risk: Generated charts, stdout logs, and downloaded FIT/GPX/TCX files can reveal sensitive health metrics, routines, and precise locations. <br>
Mitigation: Keep generated outputs local, share them only intentionally, and delete downloaded activity files and temporary charts when they are no longer needed. <br>
Risk: The skill can access sensitive Garmin data if invoked outside the user's intended context. <br>
Mitigation: Configure the agent to use this skill only for explicit Garmin-related requests and review outputs before acting on health or training recommendations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/eversonl/skills/garmin-health-analysis) <br>
- [Garmin Connect API Reference (Unofficial)](references/api.md) <br>
- [Health Data Analysis Guide - Garmin Edition](references/health_analysis.md) <br>
- [Extended Garmin Capabilities](references/extended_capabilities.md) <br>
- [MCP Server for Standard Claude Desktop](references/mcp_setup.md) <br>
- [Garmin Connect](https://connect.garmin.com) <br>
- [python-garminconnect library](https://github.com/cyberjunky/python-garminconnect) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, HTML, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown responses with JSON command output and optional local HTML chart or FIT/GPX/TCX files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Garmin credentials and local Python dependencies; generated health, location, and activity data should be handled as sensitive.] <br>

## Skill Version(s): <br>
1.2.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
