## Description:

查询华为云CCE（云容器引擎）集群列表，支持表格化输出集群名称、状态、版本、节点数等关键字段

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to query Huawei Cloud CCE cluster inventory, review cluster status, versions, and node counts, and support routine inspection or troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs Huawei Cloud credentials to query CCE inventory.

Mitigation: Use least-privilege IAM credentials limited to cluster listing and provide them only through environment variables.

Risk: The artifact documents a Python script that is not included in the submitted files.

Mitigation: Confirm the runtime script exists and review it before deployment or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/test-skill-verify-02)
- [Huawei Cloud SDK Center - CCE](https://console.huaweicloud.com/apiexplorer/#/ssdkcenter)
- [CCE API Reference](https://support.huaweicloud.com/aipcecce/index.html)
- [CCE ListClusters API](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=CCE&api=ListClusters)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and tabular text output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for querying Huawei Cloud CCE cluster lists; the submitted artifact describes commands but does not include the referenced Python script.]

## Skill Version(s):

0.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
