## Description:

Diagnoses abnormal Huawei Cloud CDN HTTP 4xx and 5xx status codes with read-only hcloud CLI queries, edge-versus-origin analysis, top-N correlation, and access-log forensics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site reliability engineers, and CDN operators use this skill to investigate abnormal Huawei Cloud CDN 4xx/5xx spikes, determine whether failures are generated at the edge or origin, and produce an evidence-backed incident report without changing CDN configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Huawei Cloud credentials and CDN tenant access.

Mitigation: Use a least-privilege read-only hcloud profile and do not paste AK/SK values into chat or generated reports.

Risk: Downloaded CDN logs can contain client IPs, URLs, user agents, and other operational data.

Mitigation: Keep log files and extracted rows local and access-controlled, then redact or delete them when they are no longer needed.

Risk: CDN configuration changes could affect production traffic if a user follows remediation outside the skill's read-only boundary.

Mitigation: Use the skill for diagnosis and evidence gathering only; review any proposed console or manual CLI remediation through the normal change process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cdn-abnormal-status-code-analysis)
- [Huawei Cloud CLI documentation](https://support.huaweicloud.com/hcloudcli/index.html)
- [Huawei Cloud CDN API reference](https://support.huaweicloud.com/api-cdn/cdn-api-pdf.pdf)
- [Task discovery](references/task-discovery.md)
- [Task localize](references/task-localize.md)
- [Task distribution](references/task-distribution.md)
- [Task root cause](references/task-rootcause.md)
- [Task forensics](references/task-forensics.md)
- [Task report](references/task-report.md)
- [IAM policies](references/iam-policies.md)
- [Prohibited operations](references/prohibited-operations.md)
- [Related APIs](references/related-apis.md)
- [Verification method](references/verification-method.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with inline hcloud commands, JSON log extracts, and a structured diagnosis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce read-only command plans, parsed abnormal-status log rows, and remediation boundaries that require human review before action.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
