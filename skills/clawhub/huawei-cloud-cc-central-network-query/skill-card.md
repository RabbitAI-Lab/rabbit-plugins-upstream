## Description:

Queries Huawei Cloud Cloud Connect (CC) Central Network instances, attachments, and connections through read-only hcloud CLI commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud engineers, and operators use this skill to inspect Huawei Cloud Cloud Connect Central Network topology, attachment configuration, and connection status without performing write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI installation guide includes a curl-and-bash installer flow for downloaded content.

Mitigation: Install hcloud from verified official Huawei Cloud instructions or a trusted package source, and verify signatures or checksums before running any installer.

Risk: The skill needs Huawei Cloud credentials and can expose network topology during read-only inspection.

Mitigation: Use a least-privilege IAM policy limited to cc:centralNetworks:list and cc:centralNetworks:get, inject credentials at runtime, and avoid hardcoding access keys.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [API Reference](references/api-reference.md)
- [Huawei Cloud hcloud CLI Installation Documentation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and parameter guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only command guidance for Huawei Cloud CC Central Network resources; requires hcloud authentication, domain ID, region, and resource identifiers.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
