## Description: <br>
Threshold-based alerting on Scrapfly account metrics with guidance for setting up and managing alerts through REST API, MCP tools, and the Scrapfly CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scrapfly](https://clawhub.ai/user/scrapfly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operations teams use this skill to create, preview, update, snooze, test, and delete Scrapfly alert rules for account, project, or domain metrics while grounding thresholds in monitoring data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incorrect alert thresholds or notification channels could create noisy, misleading, or costly alert behavior. <br>
Mitigation: Review thresholds, notification channels, and any update or delete action before confirmation, and preview alert rules against historical data before creating them. <br>
Risk: Broad Scrapfly API credentials could expose more account capability than alert management requires. <br>
Mitigation: Use a Scrapfly API key with only the access needed for alert management. <br>


## Reference(s): <br>
- [Scrapfly Alerting Concept Guide](https://scrapfly.io/docs/alerting/getting-started) <br>
- [Scrapfly Alerting Metric Registry](https://scrapfly.io/docs/alerting/metric-reference) <br>
- [Scrapfly Alerting State Machine](https://scrapfly.io/docs/alerting/state-machine) <br>
- [Scrapfly Alerting Webhook Payload and Signing](https://scrapfly.io/docs/alerting/webhook-payload) <br>
- [Scrapfly Alerting Error Reference](https://scrapfly.io/docs/alerting/error-reference) <br>
- [Scrapfly Alerting Anti-Spam](https://scrapfly.io/docs/alerting/anti-spam) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON, HTTP, and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent guidance for Scrapfly alerting workflows; no hidden code or installer behavior was found in security evidence.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
