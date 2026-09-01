## Description:

查询华为云CCE（云容器引擎）集群列表，支持表格化输出集群名称、状态、版本、节点数等关键字段

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to list Huawei Cloud CCE clusters for routine checks, resource management, and troubleshooting. It returns key cluster details such as name, status, version, and node count in a table.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can query Huawei Cloud CCE inventory when credentials are available.

Mitigation: Use an IAM principal limited to cce:cluster:list and provide AK/SK only through environment variables.

Risk: The documented command references a script that is not included in the artifact.

Mitigation: Review or supply the missing script before relying on the documented commands.

## Reference(s):

- [SDK Center - CCE](https://console.huaweicloud.com/apiexplorer/#/ssdkcenter)
- [CCE API Reference](https://support.huaweicloud.com/aipcecce/index.html)
- [CCE ListClusters](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=CCE&api=ListClusters)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and tabular text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Huawei Cloud AK/SK credentials from environment variables and IAM permission for cce:cluster:list.]

## Skill Version(s):

0.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
