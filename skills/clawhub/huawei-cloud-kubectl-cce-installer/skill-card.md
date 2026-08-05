## Description: <br>
Install, upgrade, verify, or troubleshoot local kubectl and the Huawei Cloud kubectl-cce plugin. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect, install, or repair local kubectl and Huawei Cloud kubectl-cce prerequisites for CCE Kubernetes access without changing cloud or cluster resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install local executables or build binaries from downloaded source after user approval. <br>
Mitigation: Review the no-change plan, confirm the target --bin-dir, and approve --execute only after accepting the local system change. <br>
Risk: Protected installation directories such as /usr/local/bin may require elevated permissions. <br>
Mitigation: Use a writable directory when possible and approve sudo explicitly only for the confirmed target path. <br>
Risk: Source-build fallback depends on external Kubernetes, Huawei OBS, and Gitee sources plus a local Go toolchain. <br>
Mitigation: Use the documented pinned versions and approve source-build fallback only when the trusted download path is unavailable. <br>
Risk: Huawei Cloud credentials are needed later for cluster access but not for installation. <br>
Mitigation: Do not provide credentials during installation; configure credentials separately only when intentionally using kubectl-cce against a CCE cluster. <br>


## Reference(s): <br>
- [Plugin Usage](references/plugin-usage.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Gitee kubectl-cce Plugin Release v0.1.0](https://gitee.com/pancake0001/kubectl-cce-plugin/releases/tag/v0.1.0) <br>
- [Gitee kubectl-cce Plugin Repository](https://gitee.com/pancake0001/kubectl-cce-plugin) <br>
- [Kubernetes Release Downloads](https://kubernetes.io/releases/download/) <br>
- [Kubernetes Source Repository](https://github.com/kubernetes/kubernetes.git) <br>
- [Huawei Cloud CCE OBS kubectl Package Endpoint](https://cce-north-4.obs.cn-north-4.myhuaweicloud.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash and PowerShell commands plus human-readable installer output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The installer reports local platform state, no-change plans, installation status, verification output, and clear nonzero errors for missing dependencies or failed downloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
