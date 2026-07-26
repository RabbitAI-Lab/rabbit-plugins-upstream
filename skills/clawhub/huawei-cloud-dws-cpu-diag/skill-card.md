## Description: <br>
Diagnoses high CPU conditions in Huawei Cloud DWS clusters by collecting CPU and related metrics through KooCLI or DWS Autopilot MCP Server, analyzing likely customer-side or system-side causes, and producing a standardized report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cloud operations engineers and database administrators use this skill to investigate Huawei Cloud DWS high CPU alarms, CPU overload events, and CPU load anomalies. It collects DWS metrics, identifies likely customer-side or system-side causes, and returns a standardized diagnosis report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credential exposure through AK/SK setup or configuration steps. <br>
Mitigation: Use tightly scoped read-only DWS credentials, avoid placing AK/SK values in chat or command lines, and secure any local configuration files that contain secrets. <br>
Risk: Unrelated OBS/obsutil setup may introduce unnecessary credentials or tools for a DWS CPU diagnosis workflow. <br>
Mitigation: Do not follow OBS or obsutil setup unless it is independently required for the user's environment. <br>
Risk: Generated diagnosis reports may contain sensitive cluster, host, database user, and SQL details. <br>
Mitigation: Store generated reports in a controlled workspace and redact sensitive operational details before sharing outside the authorized team. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-dws-cpu-diag) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [DWS Autopilot MCP Server Installation Guide](references/dws-mcp-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Metric Reference](references/metric-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, HTML, files, shell commands, guidance] <br>
**Output Format:** [Diagnosis summary text plus a complete HTML diagnosis report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes reports using the dws_cpu_diagnosis_report_{timestamp}.html filename pattern; conclusions are expected to be grounded in tool results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
