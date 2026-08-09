## Description: <br>
Diagnoses Huawei Cloud DWS cluster I/O overload alarms by collecting telemetry through KooCLI or the DWS Autopilot MCP Server, classifying root causes, and producing a standardized report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cloud operations engineers and database reliability teams use this skill to investigate Huawei Cloud DWS high I/O alarms, collect cluster and query telemetry, and distinguish customer-side workload causes from system-side or hardware-layer anomalies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs local KooCLI/Python commands and calls Huawei Cloud DWS telemetry APIs. <br>
Mitigation: Install and run it only in environments where the agent is authorized to execute local commands and access DWS operational telemetry. <br>
Risk: Generated reports may contain sensitive operational details such as cluster IDs, node names or IPs, usernames, query IDs, and SQL snippets. <br>
Mitigation: Treat reports as sensitive operational artifacts, restrict sharing, and prefer explicit export handling before using the skill on production data. <br>
Risk: Huawei Cloud AK/SK credentials can be exposed if entered in chat or embedded directly in command history. <br>
Mitigation: Use configured credential stores, masked status checks, temporary credentials where available, and never provide AK/SK values directly in conversation. <br>
Risk: Broad cloud permissions would increase blast radius for a diagnostic workflow. <br>
Mitigation: Grant only the documented read-only DWS permissions: dws:clusters:get, dws:clusters:list, dws:metricData:get, and dws:hostOverview:get. <br>


## Reference(s): <br>
- [I/O Background Knowledge](references/io-background.md) <br>
- [Metric Reference](references/metric-reference.md) <br>
- [I/O Diagnosis Reference](references/IO_DIAGNOSIS_REF.md) <br>
- [Output Format](references/output-format.md) <br>
- [diagnosis_json Output Format Reference](references/diagnosis-json-format.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [DWS Autopilot MCP Server Installation Guide](references/dws-mcp-installation-guide.md) <br>
- [Huawei Cloud hcloud Installation Guide](https://support.huaweicloud.com/cli/cli_hcloud_install.html) <br>
- [Huawei Cloud DWS API Reference](https://support.huaweicloud.com/api-dws/dws_02_0023.html) <br>
- [DWS Autopilot MCP Server Repository](https://github.com/huaweicloud/dws_ai_native/tree/dws_autopilot_mcp_server/hwcloud_dws_mcp_mag) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, Shell commands, Files, HTML, JSON, Guidance] <br>
**Output Format:** [HTML diagnosis report and diagnosis_json object, with intermediate Markdown and shell-command guidance for setup and data collection] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes dws_io_diagnosis_report_{timestamp}.html in the current workspace and returns a structured diagnosis_json summary.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
