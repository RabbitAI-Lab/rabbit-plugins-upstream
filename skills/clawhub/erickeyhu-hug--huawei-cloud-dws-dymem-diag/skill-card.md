## Description: <br>
Diagnoses high memory, memory alarm, and OOM scenarios in Huawei Cloud DWS clusters by collecting metrics through KooCLI or the DWS Autopilot MCP Server and producing a standardized report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and support engineers use this skill to investigate Huawei Cloud DWS cluster high-memory alarms or OOM symptoms, distinguish customer workload from system-side contributors, and produce a standardized diagnosis report from observed metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses read-only access to DWS monitoring data and generated reports may contain sensitive cluster, SQL, session, or user details. <br>
Mitigation: Use least-privilege IAM credentials, keep generated HTML reports in controlled workspaces, and handle reports as sensitive operational artifacts. <br>
Risk: The security evidence flags unsafe cloud-secret setup examples for review. <br>
Mitigation: Prefer interactive or environment-variable credential setup, avoid placing AK/SK values in command history or chat, and verify credential handling before installation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-dws-dymem-diag) <br>
- [CLI Installation Guide](artifact/references/cli-installation-guide.md) <br>
- [DWS Autopilot MCP Server Installation Guide](artifact/references/dws-mcp-installation-guide.md) <br>
- [IAM Policies](artifact/references/iam-policies.md) <br>
- [Metric Reference](artifact/references/metric-reference.md) <br>
- [Memory Background Knowledge](artifact/references/memory-background.md) <br>
- [Output Format](artifact/references/output-format.md) <br>
- [Huawei Cloud hcloud Installation Guide](https://support.huaweicloud.com/cli/cli_hcloud_install.html) <br>
- [Huawei Cloud DWS API Reference](https://support.huaweicloud.com/api-dws/dws_02_0023.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, API calls, Files, Guidance] <br>
**Output Format:** [HTML diagnosis report file with concise text summary and command/tool-call guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes generated diagnosis reports to the workspace and may include sensitive operational details from DWS monitoring data.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
