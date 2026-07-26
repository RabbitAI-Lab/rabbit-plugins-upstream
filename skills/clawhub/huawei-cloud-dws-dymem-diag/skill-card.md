## Description: <br>
Diagnoses high memory usage, memory alarms, and OOM scenarios in Huawei Cloud DWS clusters by collecting metrics through KooCLI or the DWS Autopilot MCP Server and producing a diagnosis report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations engineers use this skill to investigate Huawei Cloud DWS memory alarms, OOM conditions, and high memory usage by collecting cluster, host, metric, active session, database user, and SQL evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill needs read-only Huawei Cloud DWS access and inspects cluster metrics, hosts, users, active sessions, and SQL text. <br>
Mitigation: Use least-privilege or temporary credentials and grant only the documented DWS read permissions needed for diagnosis. <br>
Risk: Huawei Cloud AK/SK credentials or IAM tokens could be exposed if entered into chat, command lines, or unprotected configuration files. <br>
Mitigation: Configure credentials outside the conversation, avoid putting AK/SK values on command lines, and protect local configuration files. <br>
Risk: Generated HTML diagnosis reports may contain sensitive operational data, database user names, and SQL text. <br>
Mitigation: Review generated reports before sharing, store them according to internal data handling rules, and delete them when no longer needed. <br>


## Reference(s): <br>
- [CLI Installation Guide](artifact/references/cli-installation-guide.md) <br>
- [DWS Autopilot MCP Server Installation Guide](artifact/references/dws-mcp-installation-guide.md) <br>
- [IAM Policies](artifact/references/iam-policies.md) <br>
- [Memory Background Knowledge](artifact/references/memory-background.md) <br>
- [Metric Reference](artifact/references/metric-reference.md) <br>
- [Output Format](artifact/references/output-format.md) <br>
- [Huawei Cloud KooCLI Installation Guide](https://support.huaweicloud.com/cli/cli_hcloud_install.html) <br>
- [Huawei Cloud DWS API Reference](https://support.huaweicloud.com/api-dws/dws_02_0023.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, HTML, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and a generated HTML diagnosis report.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The generated report may include cluster metrics, database users, active session details, and SQL text.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
