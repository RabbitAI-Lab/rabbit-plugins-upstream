## Description: <br>
Analytics Dashboard helps teams build configurable data dashboards with widgets, advanced analytics, alerts, report exports, collaboration, custom data sources, theming, and real-time updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operations, SRE, data analysis, and product teams use this skill to configure dashboards, monitor KPIs and SLAs, detect anomalies, export reports, and share controlled views across teams. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduled exports and shared dashboards could distribute business data to unintended recipients. <br>
Mitigation: Verify recipients, roles, shared-dashboard permissions, and export schedules before enabling automatic distribution. <br>
Risk: Dashboard tokens, database connections, external API tokens, webhook URLs, and OAuth credentials can expose sensitive access if configured casually. <br>
Mitigation: Use approved secret storage or environment variables, restrict credentials to approved data sources, and rotate credentials when access changes. <br>
Risk: Misconfigured data sources, alert thresholds, or analysis windows can create misleading dashboard results or noisy alerts. <br>
Mitigation: Validate source schemas and data quality, test alert conditions with representative data, and review anomaly or forecast outputs before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/analytics-dashboard) <br>
- [Project homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce dashboard configuration guidance, export commands, report structures, and operational troubleshooting steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
