## Description: <br>
DWS cluster memory high root cause diagnosis skill, based on KooCLI v3.2.0+ and DWS Autopilot MCP Server, that collects memory metrics, analyzes customer-side and system-side causes, and outputs a standardized diagnosis report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations engineers use this skill to investigate Huawei Cloud DWS cluster high-memory alarms, OOM scenarios, and user-initiated memory diagnosis requests. It collects DWS memory metrics through KooCLI or the DWS Autopilot MCP Server and returns a structured diagnosis report based on tool results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires read-only DWS monitoring access and may expose sensitive cloud credential handling paths during setup. <br>
Mitigation: Use least-privilege temporary credentials, avoid placing AK/SK values on command lines, and verify credential status without exposing secrets. <br>
Risk: Generated HTML reports may contain sensitive operational data about clusters, users, SQL statements, and memory behavior. <br>
Mitigation: Protect report files as sensitive artifacts and delete them when they are no longer needed. <br>
Risk: The authoritative security review marks the release suspicious because setup and output handling can expose credentials or report data without enough user control. <br>
Mitigation: Install only when the required monitoring access and report-handling practices are acceptable for the deployment environment. <br>


## Reference(s): <br>
- [CLI Installation Guide - Huawei Cloud DWS Memory Diagnosis](references/cli-installation-guide.md) <br>
- [DWS Autopilot MCP Server](references/dws-mcp-installation-guide.md) <br>
- [IAM Policies - DWS Memory High Diagnosis](references/iam-policies.md) <br>
- [Memory Background Knowledge - DWS Memory High Diagnosis](references/memory-background.md) <br>
- [Metric Reference - DWS Memory High Diagnosis](references/metric-reference.md) <br>
- [Output Format - DWS Memory High Diagnosis](references/output-format.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, shell commands, configuration, HTML, guidance] <br>
**Output Format:** [HTML diagnosis report plus concise text status or error messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The report is saved as dws_mem_diagnosis_report_{timestamp}.html and conclusions must come from tool results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
