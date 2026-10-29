## Description:

查询华为云CCE（云容器引擎）集群列表，支持表格化输出集群名称、状态、版本、节点数等关键字段

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to list Huawei Cloud CCE clusters in a selected region, check cluster status and Kubernetes versions, and support routine inspection or troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential lookup can pick unintended Huawei Cloud keys from the execution environment.

Mitigation: Run the skill in an environment containing only the intended HUAWEICLOUD_SDK_AK and HUAWEICLOUD_SDK_SK values.

Risk: Cloud account exposure depends on the permissions attached to the supplied Huawei Cloud credentials.

Mitigation: Use a dedicated low-privilege Huawei IAM user limited to cce:cluster:list.

Risk: Dependency behavior may change if packages are resolved loosely before production use.

Mitigation: Pin or lock huaweicloudsdk-cce and huaweicloudsdk-core dependencies before production deployment.

## Reference(s):

- [Huawei Cloud SDK Center - CCE](https://console.huaweicloud.com/apiexplorer/#/ssdkcenter)
- [Huawei Cloud CCE API Reference](https://support.huaweicloud.com/aipcecce/index.html)
- [Huawei Cloud CCE ListClusters API](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=CCE&api=ListClusters)
- [IAM Permissions](artifact/iam-policies.md)
- [Verification Method](artifact/verification-method.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and plain-text table output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Huawei Cloud AK/SK environment variables and read-only cce:cluster:list IAM permission.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
