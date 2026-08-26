## Description:

Huawei Cloud SWR image governance skill using the hcloud CLI for permissions, retention policies, shared domains, image sharing, agency delegation, and repository references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to administer Huawei Cloud SWR image governance, including namespace and repository permissions, retention rules, shared download domains, sharing checks, and SWR agency delegation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact Huawei Cloud SWR administration, including permission grants, permission revocation, retention rules, shared domains, and agency creation.

Mitigation: Install only for SWR administration use cases, require explicit user review before side-effecting commands, and use least-privilege IAM credentials.

Risk: Retention rules can delete image tags automatically and the deleted tags may be unrecoverable.

Mitigation: Review retention conditions carefully, preview the exact hcloud command, and verify the repository and tag selectors before confirming create or update operations.

Risk: Permission revocation or downgrades can interrupt CI/CD pipelines or services that pull from affected namespaces or repositories.

Mitigation: Confirm affected users and workloads before changing access, then verify permissions with read-only SWR auth queries after the change.

Risk: Long-term AK/SK credentials increase exposure if they are leaked through commands, logs, or conversation history.

Mitigation: Prefer temporary credentials where possible, keep secrets in environment variables, avoid printing credential values, enable MFA for sensitive operations, and rotate AK/SK regularly.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-swr-image-governance)
- [SWR Governance API Reference Guide](references/swr-governance-api-guide.md)
- [Huawei Cloud SWR Documentation](https://support.huaweicloud.com/swr/index.html)
- [hcloud CLI Documentation](https://support.huaweicloud.com/cli/index.html)
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/)
- [IAM Permission Policies](references/iam-policies.md)
- [Huawei Cloud KooCLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [SWR Image Governance Output Format](references/output-format.md)
- [Common Pitfalls and Solutions](references/common-pitfalls.md)
- [Task: Namespace Permissions](references/task-namespace-permissions.md)
- [Task: Repository Permissions](references/task-repository-permissions.md)
- [Task: Retention Management](references/task-retention-management.md)
- [Task: Shared Domains](references/task-shared-domains.md)
- [Task: Image Sharing](references/task-image-sharing.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline hcloud CLI commands and structured JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may include cloud administration operations and should be reviewed before execution.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
