## Description: <br>
Analytics Dashboard guides agents in creating and operating data visualization dashboards with custom widgets, trend and anomaly analysis, alerts, report exports, team sharing, custom data sources, themes, and real-time updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, analysts, SREs, product managers, and developers use this skill to generate dashboard plans, widget configurations, analytics summaries, report export steps, alerting guidance, and data-source setup guidance for operational monitoring and business reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Operational dashboards, reports, recipients, or webhook destinations may expose sensitive business data if sharing is configured too broadly. <br>
Mitigation: Require explicit approval for report recipients, webhook destinations, and scheduled sharing; keep credentials in environment variables. <br>
Risk: The skill may propose command execution and dependency installation for dashboard services, exports, analytics, or real-time updates. <br>
Mitigation: Review commands before execution, run with least privilege, and install only the dependencies required for the chosen workflow. <br>
Risk: Non-local API, WebSocket, or webhook endpoints can expose operational data if transport security or endpoint ownership is not verified. <br>
Mitigation: Use HTTPS or WSS for non-local endpoints and verify the destination before sending dashboard, alert, or report data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/analytics-dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured JSON snippets with shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dashboard configuration, widget definitions, report export commands, alert setup guidance, dependency installation commands, and security handling notes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
