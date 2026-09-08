## Description:

Queries Huawei Cloud Cloud Connect resources through the hcloud CLI for read-only inspection of cloud connections, bandwidth packages, inter-region bandwidth, network instances, routes, and cross-account authorisations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud engineers, and operators use this skill to inspect Huawei Cloud Cloud Connect topology, bandwidth allocation, routes, network attachments, and cross-account authorisation relationships without performing write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud Connect query results can expose sensitive topology, route, bandwidth, and cross-account authorisation information.

Mitigation: Use a least-privilege Huawei Cloud IAM identity with CC ReadOnlyAccess and limit access to returned query output.

Risk: Omitting or mis-setting domain_id can cause queries to run against the wrong Huawei Cloud account.

Mitigation: Specify domain_id explicitly for every query and verify it against the intended account before running commands.

Risk: Setup requires hcloud CLI installation and AK/SK credential handling.

Mitigation: Review the hcloud installer before running it, protect AK/SK credentials, and avoid sharing credential-bearing command history or logs.

## Reference(s):

- [API Reference - Cloud Connect Query Endpoints](artifact/references/api-reference.md)
- [CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [IAM Policies for CC Query Skill](artifact/references/iam-policies.md)
- [Verification Method](artifact/references/verification-method.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [Data Flow Diagram](artifact/references/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline hcloud CLI commands and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only query guidance; command execution depends on the user's authenticated Huawei Cloud CLI environment.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
