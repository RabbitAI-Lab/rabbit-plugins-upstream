## Description:

Diagnoses Huawei Cloud DWS high-memory alarms by collecting cluster memory metrics through KooCLI or the DWS Autopilot MCP Server, analyzing likely customer-side or system-side causes, and producing a standardized diagnosis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support engineers use this skill to investigate DWS memory alarms, OOM scenarios, and user-initiated memory diagnosis requests with a structured report grounded in collected metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to Huawei DWS monitoring data, active SQL and session details, host or IP metadata, and local diagnostic reports.

Mitigation: Use least-privilege read-only IAM permissions and keep generated reports out of shared or version-controlled folders.

Risk: Credential handling can expose Huawei Cloud AK/SK secrets if users pass secrets in command lines or conversation.

Mitigation: Prefer interactive or managed-secret credential setup and avoid passing AK/SK values on the command line or in chat.

Risk: The authoritative scan marked the release suspicious because it handles cloud credentials and sensitive diagnostic data while under-disclosing local persistence and credential-handling risks.

Mitigation: Review credential setup, local report storage, and data-sharing paths before deployment.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [DWS Autopilot MCP Server Installation Guide](references/dws-mcp-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Memory Background Knowledge](references/memory-background.md)
- [Metric Reference](references/metric-reference.md)
- [Output Format](references/output-format.md)

## Skill Output:

**Output Type(s):** [Text, HTML, Shell commands, API calls, Files, Guidance]

**Output Format:** [HTML diagnosis report with a short text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a local dws_mem_diagnosis_report_<timestamp>.html report and relies on paginated metric collection.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
