## Description:

DWS cluster I/O overload root cause diagnosis skill that uses KooCLI and DWS Autopilot MCP Server telemetry to collect metrics, analyze customer-side or system-side root causes with a three-stage decision tree, and output a standardized diagnosis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Database operators, support engineers, and developers use this skill to investigate Huawei Cloud DWS high I/O alarms, disk I/O load anomalies, and user-initiated I/O diagnosis requests. It gathers DWS metrics, checks host and business activity signals, and produces a tool-grounded diagnosis report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles cloud credentials and detailed DWS production telemetry, including SQL text and operational reports.

Mitigation: Install only where the operator is authorized to view DWS production telemetry and SQL text, and treat generated HTML reports as sensitive operational records.

Risk: Credential exposure can occur if AK/SK values are placed in command lines, conversations, plaintext files, or readable configuration files.

Mitigation: Use interactive or secret-manager credential setup where possible, avoid putting AK/SK values in command lines or plaintext files, and restrict file permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-dws-io-diag)
- [I/O Background Knowledge - DWS I/O Overload Diagnosis](references/io-background.md)
- [Metric Reference - DWS I/O Overload Diagnosis](references/metric-reference.md)
- [DWS I/O Diagnosis - Scenario Routing and Full Investigation Direction Reference](references/IO_DIAGNOSIS_REF.md)
- [Output Format - DWS I/O Overload Diagnosis](references/output-format.md)
- [diagnosis_json Output Format Reference](references/diagnosis-json-format.md)
- [IAM Policies - DWS I/O Overload Diagnosis](references/iam-policies.md)
- [CLI Installation Guide - Huawei Cloud DWS I/O Diagnosis](references/cli-installation-guide.md)
- [DWS Autopilot MCP Server](references/dws-mcp-installation-guide.md)
- [hcloud Installation Guide](https://support.huaweicloud.com/cli/cli_hcloud_install.html)
- [DWS API Reference](https://support.huaweicloud.com/api-dws/dws_02_0023.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [HTML diagnosis report plus diagnosis_json summary data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report is generated from live tool results and may include sensitive operational telemetry, SQL text, host details, and timing data.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
