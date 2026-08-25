## Description:

Install, upgrade, verify, or troubleshoot local kubectl and the Huawei Cloud kubectl-cce plugin for CCE Kubernetes resource access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect, install, and verify local kubectl and kubectl-cce prerequisites for Huawei Cloud CCE access. It supports a plan-and-confirm workflow for local executable installation while keeping cloud and Kubernetes resources unchanged.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloading or building kubectl and kubectl-cce from public sources can introduce supply-chain exposure.

Mitigation: Review the displayed plan and documented sources before approving --execute.

Risk: Installing into a protected bin directory can require elevated local permissions.

Mitigation: Prefer a user-writable bin directory, and use sudo only when a system-wide installation is intentional.

Risk: Cluster access after installation may require sensitive Huawei Cloud or kubeconfig credentials.

Mitigation: Keep installation separate from cluster access, and configure credentials only through approved protected local mechanisms.

## Reference(s):

- [Plugin Usage](references/plugin-usage.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [kubectl-cce Plugin Release v0.1.0](https://gitee.com/pancake0001/kubectl-cce-plugin/releases/tag/v0.1.0)
- [kubectl-cce Plugin Repository](https://gitee.com/pancake0001/kubectl-cce-plugin)
- [Kubernetes Release Downloads](https://kubernetes.io/releases/download/)
- [Huawei Cloud OBS kubectl Package Repository](https://cce-north-4.obs.cn-north-4.myhuaweicloud.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and human-readable shell output with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Installer output reports detected platform, architecture, kubectl presence, kubectl-cce presence, selected bin directory, planned changes, and clear nonzero errors.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
