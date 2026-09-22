## Description:

Huawei Cloud SWR image governance skill using the hcloud CLI for namespace and repository permissions, retention rules, shared download domains, image sharing checks, agency delegation, and related repository references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud platform engineers use this skill to manage Huawei Cloud SWR governance tasks, including permissions, retention cleanup, shared access, feature checks, and agency delegation. It helps prepare hcloud commands, review parameters, and format SWR results for operational workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad SWR write and delegation actions, including permission changes, retention rules, shared domains, and agency creation.

Mitigation: Use least-privilege IAM permissions, prefer temporary credentials, and require a human to review the exact command and target resource before any write action.

Risk: The CLI installation guidance may involve downloaded installer code.

Mitigation: Avoid non-interactive installation flows and verify the hcloud installer before running it.

Risk: Retention rules can delete image tags and shared-domain or permission revocation can immediately interrupt access.

Mitigation: Confirm business impact, verify target namespaces and repositories, and run read-only checks before applying destructive or access-changing operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-swr-image-governance)
- [SWR Governance API Guide](references/swr-governance-api-guide.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Output Format](references/output-format.md)
- [Verification Method](references/verification-method.md)
- [Common Pitfalls](references/common-pitfalls.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Task: Namespace Permissions](references/task-namespace-permissions.md)
- [Task: Repository Permissions](references/task-repository-permissions.md)
- [Task: Retention Management](references/task-retention-management.md)
- [Task: Shared Domains](references/task-shared-domains.md)
- [Task: Image Sharing](references/task-image-sharing.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline hcloud shell commands and structured summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are intended for human review before execution; read operations may return JSON from hcloud.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
