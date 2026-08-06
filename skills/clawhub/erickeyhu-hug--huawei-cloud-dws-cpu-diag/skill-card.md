## Description: <br>
DWS cluster CPU high root cause diagnosis skill, based on KooCLI v3.2.0+ and DWS Autopilot MCP Server, that collects CPU metrics, analyzes customer-side and system-side causes, and outputs a standardized diagnosis report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to investigate Huawei Cloud DWS cluster CPU alarms, CPU load anomalies, and user-initiated high CPU diagnosis requests. It queries DWS metrics through KooCLI or the DWS Autopilot MCP Server and produces a structured diagnostic report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence flags unrelated OBS/obsutil credential setup for a skill whose primary purpose is DWS CPU diagnosis. <br>
Mitigation: Install and configure only the DWS diagnosis prerequisites unless the publisher separately justifies the need for OBS access. <br>
Risk: Credential setup can expose Huawei Cloud AK/SK values through command history, MCP configuration files, or conversations. <br>
Mitigation: Use least-privilege DWS IAM credentials, avoid placing AK/SK values on command lines, never share secrets in chat, and protect MCP configuration files. <br>
Risk: Generated HTML reports may contain operational data and SQL text. <br>
Mitigation: Store reports only in approved locations, restrict access, and delete or secure generated report files after review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-dws-cpu-diag) <br>
- [Publisher profile](https://clawhub.ai/user/erickeyhu-hug) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [DWS Autopilot MCP Server Installation Guide](references/dws-mcp-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Metric Reference](references/metric-reference.md) <br>
- [Huawei Cloud hcloud installation guide](https://support.huaweicloud.com/cli/cli_hcloud_install.html) <br>
- [Huawei Cloud obsutil installation guide](https://support.huaweicloud.com/utiltg-obs/obs_11_0003.html) <br>
- [Huawei Cloud obsutil configuration guide](https://support.huaweicloud.com/utiltg-obs/obs_11_0005.html) <br>
- [Huawei Cloud OBS regions and endpoints](https://support.huaweicloud.com/devg-obs/obs_03_0110.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, configuration, guidance] <br>
**Output Format:** [HTML diagnosis report with a text diagnosis summary and generated report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes dws_cpu_diagnosis_report_{timestamp}.html to the workspace root; report contents may include operational data and SQL text.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
