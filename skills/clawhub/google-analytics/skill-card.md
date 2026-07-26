## Description: <br>
Google Analytics API integration with managed OAuth for read-only reporting through the Data API and explicitly approved Admin API configuration changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and analytics operators use this skill to query GA4 reports and, when explicitly needed, manage Google Analytics accounts, properties, and data streams through Maton-managed OAuth. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub Google Analytics Skill](https://clawhub.ai/byungkyu/skills/google-analytics) <br>
- [Google Analytics Admin API Overview](https://developers.google.com/analytics/devguides/config/admin/v1) <br>
- [Google Analytics Data API Overview](https://developers.google.com/analytics/devguides/reporting/data/v1) <br>
- [Google Analytics Run Report](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/runReport) <br>
- [Maton API Key Settings](https://maton.ai/settings) <br>
- [Related ClawHub API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a Maton-managed Google Analytics OAuth connection; prefer the Data API for reporting and require explicit approval before Admin API write operations.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
