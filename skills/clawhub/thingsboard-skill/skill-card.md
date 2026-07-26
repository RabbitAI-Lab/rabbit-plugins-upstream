## Description: <br>
Manage ThingsBoard devices, dashboards, telemetry, and users via the ThingsBoard REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hoangnv170752](https://clawhub.ai/user/hoangnv170752) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and ThingsBoard administrators use this skill to generate REST API commands and guidance for managing devices, telemetry, attributes, assets, dashboards, users, and customers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can delete ThingsBoard telemetry or otherwise make high-impact changes to managed resources. <br>
Mitigation: Require explicit confirmation for telemetry deletion, verify tenant, device, dashboard IDs and keys, and back up important telemetry before running destructive commands. <br>
Risk: Dashboard publication commands can expose dashboard contents publicly. <br>
Mitigation: Review dashboard contents for sensitive data before publication and revoke public dashboard access when it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hoangnv170752/skills/thingsboard-skill) <br>
- [ThingsBoard homepage](https://thingsboard.io) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, TB_URL, TB_USERNAME, and TB_PASSWORD; generated commands may read or change ThingsBoard resources.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
