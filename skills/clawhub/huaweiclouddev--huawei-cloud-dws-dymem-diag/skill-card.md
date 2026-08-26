## Description:

Diagnoses high memory, memory alarm, and OOM scenarios for Huawei Cloud DWS clusters by collecting DWS metrics through KooCLI or DWS Autopilot MCP Server and producing an HTML diagnosis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to investigate Huawei Cloud DWS cluster memory alarms, high-memory conditions, insufficient memory, and OOM incidents. It gathers cluster, host, instance, session, SQL, and memory-pool metrics and returns a standardized diagnosis report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated diagnosis reports may persist sensitive cluster, IP, user, and SQL details locally.

Mitigation: Treat report files as sensitive, restrict file access, keep them out of version control, and delete them when no longer needed.

Risk: Cloud credential setup can expose AK/SK values when secrets are placed on command lines or in local configuration files.

Mitigation: Use a least-privileged IAM identity, avoid putting AK/SK values on command lines, keep configuration files out of version control, and prefer interactive, environment, temporary, or secret-manager based credential handling.

Risk: Security evidence marks the release for review before installation.

Mitigation: Review and scan the skill before deployment, then run it only with the minimum DWS permissions required for read-only diagnosis.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [DWS Autopilot MCP Server Installation Guide](references/dws-mcp-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Metric Reference](references/metric-reference.md)
- [Memory Background Knowledge](references/memory-background.md)
- [Output Format](references/output-format.md)
- [Huawei Cloud hcloud Installation Guide](https://support.huaweicloud.com/cli/cli_hcloud_install.html)
- [Huawei Cloud DWS API Reference](https://support.huaweicloud.com/api-dws/dws_02_0023.html)
- [DWS Autopilot MCP Server Repository](https://github.com/huaweicloud/dws_ai_native/tree/dws_autopilot_mcp_server/hwcloud_dws_mcp_mag)

## Skill Output:

**Output Type(s):** [Analysis, Files, Shell commands, Configuration instructions]

**Output Format:** [HTML report with a text diagnosis summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes dws_mem_diagnosis_report_{timestamp}.html to the workspace; reports may contain cluster, IP, user, and SQL details.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
