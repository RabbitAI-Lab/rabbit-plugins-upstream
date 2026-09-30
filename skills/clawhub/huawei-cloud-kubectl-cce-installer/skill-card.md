## Description:

Helps developers inspect specifically scoped Kubernetes resources in Huawei Cloud CCE clusters through read-only kubectl cce commands, installing missing local prerequisites only with approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect a named or namespace-scoped CCE resource and, when needed, prepare or approve installation of local kubectl prerequisites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An authenticated command retried with TLS verification disabled can expose credentials or resource data to interception.

Mitigation: Do not accept the insecure retry unless the endpoint is independently verified and the interception risk is understood.

Risk: Installing downloaded or source-built executables changes the local machine and may require elevated access.

Mitigation: Review the installation plan, require explicit approval, prefer a user-writable directory, and avoid sudo unless a system-wide installation is intentional.

## Reference(s):

- [Plugin Usage](references/plugin-usage.md)
- [Installation](references/installation.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [kubectl-cce v0.2.1 release](https://gitee.com/pancake0001/kubectl-cce-plugin/releases/tag/v0.2.1)
- [Kubernetes downloads](https://kubernetes.io/releases/download/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with resource details and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports cluster, region, resource kind, namespace and name when applicable, and requested fields or errors.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; skill frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
