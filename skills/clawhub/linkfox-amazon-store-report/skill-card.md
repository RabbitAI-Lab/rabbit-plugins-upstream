## Description: <br>
Automates Amazon seller report retrieval for inventory, orders, sales traffic, FBA, financial settlement, returns, and Brand Analytics reports, including request, polling, download, extraction, and local access to the extracted file. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operators use this skill to request and download structured Amazon seller reports after authorization is handled by the companion auth skill. It is intended for report retrieval workflows, not for business interpretation of report contents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive Amazon seller or customer report data may be stored locally, previewed in logs, or exposed through the default temporary local HTTP endpoint. <br>
Mitigation: Use the skill only in trusted workspaces, disable HTTP serving for sensitive reports when possible, keep serving bound to loopback, and remove generated local report files after use. <br>
Risk: Report retrieval depends on a companion authorization skill and valid store tokens; incorrect setup can cause failed or unauthorized report requests. <br>
Mitigation: Confirm the auth dependency is installed and use only authorized stores and report types that match the seller account permissions. <br>
Risk: Automatic feedback telemetry can send operational context to LinkFox when the skill decides feedback is warranted. <br>
Mitigation: Review the feedback behavior before deployment and avoid entering unnecessary sensitive details into prompts or error reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-report) <br>
- [API reference](artifact/references/api.md) <br>
- [Report types reference](artifact/references/report-types.md) <br>
- [Report request reference index](artifact/references/report-requests/README.md) <br>
- [Amazon Selling Partner API report schemas](https://github.com/amzn/selling-partner-api-models/tree/main/schemas/reports) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON report-result fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce local file paths, file URIs, and short-lived local HTTP URLs for extracted Amazon report files.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence, created 2026-07-13T12:06:34Z) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
