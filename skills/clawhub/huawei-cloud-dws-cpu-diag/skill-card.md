## Description:

DWS cluster CPU high root cause diagnosis skill that uses KooCLI v3.2.0+ or the DWS Autopilot MCP Server to collect CPU metrics, analyze customer-side or system-side causes, and produce a standardized diagnosis report for high CPU and CPU alarm scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operations engineers use this skill to investigate Huawei Cloud DWS high CPU alerts, collect cluster metrics, identify likely customer-side or system-side causes, and generate a standardized diagnosis report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supporting installation docs include unrelated OBS/obsutil setup and examples that can expose AK/SK credentials on command lines.

Mitigation: Install only the DWS-required hcloud or DWS MCP components, skip OBS/obsutil unless independently required, and configure credentials through interactive or managed secret mechanisms rather than command-line arguments.

Risk: The generated diagnosis report can contain sensitive operational details such as cluster identifiers, host details, database users, query IDs, SQL text, and CPU metrics.

Mitigation: Treat the HTML report as sensitive operational data, store it in approved locations, and redact or restrict access before sharing outside the operations context.

Risk: Overbroad cloud permissions or write-capable credentials increase blast radius for a diagnostic workflow.

Mitigation: Use least-privilege DWS read-only IAM permissions limited to cluster, metric, and host overview access.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [DWS Autopilot MCP Installation Guide](references/dws-mcp-installation-guide.md)
- [IAM Policies - DWS CPU High Diagnosis](references/iam-policies.md)
- [Metric Reference - DWS CPU High Diagnosis](references/metric-reference.md)
- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-dws-cpu-diag)

## Skill Output:

**Output Type(s):** [Text, HTML, Files, Shell commands, API calls, Configuration guidance]

**Output Format:** [Diagnosis summary string plus a complete browser-renderable HTML diagnosis report.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The HTML report is saved as dws_cpu_diagnosis_report_{timestamp}.html and should be handled as sensitive operational data.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
