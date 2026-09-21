## Description:

Installs, upgrades, verifies, and troubleshoots local kubectl and Huawei Cloud kubectl-cce prerequisites for CCE Kubernetes access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform engineers use this skill to inspect, install, and verify local kubectl and kubectl-cce tools before accessing Huawei Cloud CCE clusters. It keeps local installation separate from credential setup and cluster operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network-backed installation may place downloaded or source-built executables in a local bin directory, sometimes with elevated privileges.

Mitigation: Review the plan output, confirm the target bin directory, prefer a user-writable directory when possible, and use sudo only after explicit user approval.

Risk: Installation activity could be confused with Huawei Cloud credential or cluster access setup.

Mitigation: Do not provide Huawei Cloud credentials during installation; configure credentials separately through an approved local credential provider or protected environment only when cluster access is needed.

Risk: Local executable state could be changed unexpectedly if installation is run without previewing the plan.

Mitigation: Run the read-only check and no-change plan first; execute installation only after confirmation, and preserve existing kubectl and kubectl-cce binaries.

## Reference(s):

- [Plugin Usage](references/plugin-usage.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-kubectl-cce-installer)
- [kubectl-cce Plugin Repository](https://gitee.com/pancake0001/kubectl-cce-plugin)
- [kubectl-cce v0.1.0 Release](https://gitee.com/pancake0001/kubectl-cce-plugin/releases/tag/v0.1.0)
- [Kubernetes Release Downloads](https://kubernetes.io/releases/download/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes read-only checks, installation plans, confirmation gates, verification steps, and troubleshooting guidance.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
