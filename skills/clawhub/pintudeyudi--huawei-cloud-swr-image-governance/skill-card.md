## Description:

Provides Huawei Cloud SWR image governance guidance and hcloud CLI commands for permissions, retention policies, shared download domains, image sharing, agency delegation, and repository references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pintudeyudi](https://clawhub.ai/user/pintudeyudi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and cloud administrators use this skill to audit and manage Huawei Cloud SWR repository access, retention cleanup rules, shared domains, image sharing, and agency delegation through hcloud CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can steer users toward broad account-wide write permissions for sensitive registry administration tasks.

Mitigation: Prefer read-only or task-specific IAM policies, and avoid granting the full wildcard governance policy for narrow tasks.

Risk: Commands may change permissions, retention rules, shared domains, or agency delegation.

Mitigation: Manually review write commands before execution and confirm that the target namespace, repository, user, domain, or retention rule is correct.

Risk: Huawei Cloud AK/SK credentials are required for live operations.

Mitigation: Use environment variables, avoid printing or embedding credential values, and rotate credentials according to the user's cloud security policy.

## Reference(s):

- [SWR Governance API Guide](references/swr-governance-api-guide.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Output Format](references/output-format.md)
- [Verification Method](references/verification-method.md)
- [Common Pitfalls](references/common-pitfalls.md)
- [Task: Namespace Permissions](references/task-namespace-permissions.md)
- [Task: Repository Permissions](references/task-repository-permissions.md)
- [Task: Retention Management](references/task-retention-management.md)
- [Task: Shared Domains](references/task-shared-domains.md)
- [Task: Image Sharing](references/task-image-sharing.md)
- [ClawHub Skill Page](https://clawhub.ai/pintudeyudi/skills/huawei-cloud-swr-image-governance)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include hcloud CLI operations that require Huawei Cloud credentials and IAM authorization.]

## Skill Version(s):

0.1.0 (source: evidence release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
