## Description: <br>
Analytics Dashboard helps agents design data visualization dashboards, configure widgets and data sources, run analytics, set alerts, export reports, and support team sharing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, SREs, operations teams, and business users can use this skill to build dashboards, generate recurring reports, monitor KPIs and SLA status, configure alerts, and share data views across teams. It is not intended for real-time stream processing beyond the documented dashboard update and WebSocket-style monitoring workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dashboard automation may use local files, databases, APIs, webhooks, scheduled emails, report recipients, and tokens. <br>
Mitigation: Confirm data sources, recipients, report contents, and token handling before enabling automation. <br>
Risk: Non-local deployments may expose credentials or dashboard data if transport, permissions, or auditing are weak. <br>
Mitigation: Use environment variables, least-privilege credentials, HTTPS/WSS, audit logging, and token rotation. <br>
Risk: Automated alerts and scheduled reports can send sensitive or incorrect information to unintended recipients. <br>
Mitigation: Review alert channels, report schedules, recipient lists, and generated content before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/analytics-dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON examples, code snippets, shell commands, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe dashboard/report exports such as PDF, CSV, Excel, and JSON when supported by the user's environment.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
