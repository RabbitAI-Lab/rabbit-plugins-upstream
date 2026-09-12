## Description:

Manages Huawei Cloud CloudDeploy (CodeArts Deploy) applications and deployment tasks through the KooCLI hcloud client, including listing, detail lookup, creation, start and delete workflows, failure analysis, and OBS artifact checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DevOps engineers use this skill to inspect and operate Huawei Cloud CloudDeploy applications and deployment tasks, troubleshoot failed deployments, and verify OBS artifacts before deployment. It supports read-only query and analysis flows plus guarded create, start, and delete workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide create, start, and delete operations for cloud deployment tasks when granted broad Huawei Cloud permissions.

Mitigation: Use a dedicated least-privilege Huawei identity, prefer read-only permissions for query and analysis, and require explicit confirmation before any create, start, or delete action.

Risk: Default quality reporting can send runtime data and an IAM token to an outbound reporting endpoint.

Mitigation: Review the reporting behavior before installation, disable reporting unless explicitly needed, and avoid overriding reporting endpoints.

Risk: Installer source or TLS weakening could undermine trust in hcloud command execution.

Mitigation: Install hcloud from an official pinned and checksummed source and keep TLS certificate verification enabled.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-deployment-task-management)
- [Publisher Profile](https://clawhub.ai/user/huaweiclouddev)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Test Report](references/test-report.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-shaped result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Masks AK/SK-like secrets in output guidance and requires preview or explicit confirmation before write operations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
