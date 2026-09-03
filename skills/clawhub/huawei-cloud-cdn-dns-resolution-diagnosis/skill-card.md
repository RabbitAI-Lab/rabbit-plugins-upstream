## Description:

Diagnose Huawei Cloud CDN domain DNS resolution by comparing the expected CNAME with actual DNS A-record results and Huawei Cloud CDN IP attribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operations teams, and support engineers use this skill to diagnose why a CDN domain is not resolving to Huawei Cloud CDN. It validates CLI credentials and domain access, retrieves the expected CNAME, probes DNS A records, checks IP attribution, and returns a structured diagnosis with remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Huawei Cloud credentials or AK/SK values could be exposed if pasted into chat or logs.

Mitigation: Use configured CLI credentials or environment-based credentials only; do not ask users to paste AK/SK values, and do not echo credential material.

Risk: Live DNS queries may be visible to DNS providers or enterprise monitoring systems.

Mitigation: Run probes only for domains the user is authorized to diagnose and disclose that DNS lookups may be observed by network infrastructure.

Risk: Changing the system DNS resolver for regional checks can affect other applications on shared or managed hosts.

Mitigation: Avoid resolver changes on shared machines unless there is a clear rollback path; prefer controlled environments for multi-region or alternate-resolver verification.

Risk: Configuration changes to CDN or DNS could affect production traffic or billing if performed outside the skill scope.

Mitigation: Keep execution read-only, refuse write/delete/modify requests, and route configuration changes to the Huawei Cloud console or separately authorized manual operations.

## Reference(s):

- [Skill Overview](artifact/SKILL.md)
- [Data Flow Diagram](artifact/references/dataflow-diagram.md)
- [CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [IAM Permission Policies](artifact/references/iam-policies.md)
- [API and CLI Command Reference](artifact/references/related-apis.md)
- [DNS Resolution Probe](artifact/references/task-dns-resolve.md)
- [IP Attribution Check](artifact/references/task-ip-attribution.md)
- [Permission Check and CNAME Retrieval](artifact/references/task-permission-check.md)
- [Report Generation](artifact/references/task-report-generation.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [Verification Method](artifact/references/verification-method.md)
- [Prohibited Operations](artifact/references/prohibited-operations.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration guidance]

**Output Format:** [Markdown diagnosis report with JSON probe results and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflow; DNS probe emits a JSON envelope; IP attribution checks are limited to 20 resolved IPs.]

## Skill Version(s):

1.0.0 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
