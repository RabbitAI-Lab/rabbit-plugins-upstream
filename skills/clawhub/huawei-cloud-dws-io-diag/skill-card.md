## Description: <br>
DWS cluster I/O overload root cause diagnosis skill based on KooCLI v3.2.0+ and DWS Autopilot MCP Server that collects I/O metrics, analyzes customer-side or system-side root causes with a three-stage decision tree, and outputs a standardized diagnosis report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations engineers use this skill to investigate Huawei Cloud DWS cluster I/O alarms, high I/O usage, and disk I/O load anomalies. It guides metric collection through KooCLI or the DWS Autopilot MCP Server and produces a diagnosis summary and report grounded in returned monitoring data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run local hcloud and Python commands and use tools beyond the declared list. <br>
Mitigation: Review the skill before installation, run it in a scoped environment, and allow only the commands and DWS tools needed for the diagnostic workflow. <br>
Risk: The workflow handles cloud credential configuration in ways that can expose AK/SK values if used carelessly. <br>
Mitigation: Use interactive credential setup or a secret manager, avoid putting AK/SK values in command lines or committed YAML files, and restrict configuration file permissions. <br>
Risk: DWS monitoring data, active-query data, and generated HTML reports can contain sensitive operational information. <br>
Mitigation: Run the skill only for authorized clusters and treat generated reports as sensitive files with appropriate access controls and retention. <br>


## Reference(s): <br>
- [Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-dws-io-diag) <br>
- [CLI Installation Guide - Huawei Cloud DWS I/O Diagnosis](references/cli-installation-guide.md) <br>
- [DWS Autopilot MCP Server](references/dws-mcp-installation-guide.md) <br>
- [IAM Policies - DWS I/O Overload Diagnosis](references/iam-policies.md) <br>
- [Metric Reference - DWS I/O Overload Diagnosis](references/metric-reference.md) <br>
- [I/O Background Knowledge - DWS I/O Overload Diagnosis](references/io-background.md) <br>
- [Output Format - DWS I/O Overload Diagnosis](references/output-format.md) <br>
- [diagnosis_json Output Format Reference](references/diagnosis-json-format.md) <br>
- [DWS I/O Diagnosis - Scenario Routing and Full Investigation Direction Reference](references/IO_DIAGNOSIS_REF.md) <br>
- [hcloud Installation Guide](https://support.huaweicloud.com/cli/cli_hcloud_install.html) <br>
- [DWS API Reference](https://support.huaweicloud.com/api-dws/dws_02_0023.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Structured diagnosis summary plus HTML diagnosis report, with supporting command and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill requires conclusions to come from actual tool results and marks failed or empty metric queries as unavailable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
