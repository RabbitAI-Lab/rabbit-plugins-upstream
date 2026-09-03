## Description:

Queries Huawei Cloud Cloud Connect Central Network instances, attachments, and connections with the hcloud CLI for read-only topology and deployment inspection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and network engineers use this skill to inspect Huawei Cloud Cloud Connect Central Network topology, connection status, attachment configuration, and deployment state without creating, updating, or deleting resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI installation guidance includes downloading and running remote content without an integrity check.

Mitigation: Use Huawei's official installation source, verify checksums or signatures when available, and review the installer before execution.

Risk: The skill queries cloud network topology and may expose sensitive deployment details through command output.

Mitigation: Run commands with a narrowly scoped read-only Huawei Cloud identity and avoid sharing command output outside approved operational channels.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [API Reference](references/api-reference.md)
- [Huawei Cloud hcloud CLI Installation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cc-central-network-query)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and hcloud CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only command guidance; hcloud command results are expected as JSON from Huawei Cloud.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
