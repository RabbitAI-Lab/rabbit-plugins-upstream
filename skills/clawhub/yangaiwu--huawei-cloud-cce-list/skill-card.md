## Description:

Lists Huawei Cloud CCE clusters for a selected region and formats key fields such as name, status, cluster version, and platform version in a table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and SREs use this skill to inspect Huawei Cloud CCE cluster inventory during routine checks, resource management, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Huawei Cloud AK/SK credentials are required to query CCE inventory.

Mitigation: Use least-privilege credentials limited to cce:cluster:list and avoid exposing credential values in shared terminals or logs.

Risk: Cluster inventory output can reveal sensitive resource names, versions, and operational state.

Mitigation: Run the skill only in intended accounts and treat generated inventory output as sensitive operational data.

Risk: Runtime dependencies are declared with lower bounds rather than exact pins.

Mitigation: Pin huaweicloudsdk-cce and huaweicloudsdk-core versions before operational deployment.

## Reference(s):

- [Huawei Cloud SDK Center - CCE](https://console.huaweicloud.com/apiexplorer/#/ssdkcenter)
- [Huawei Cloud CCE API Reference](https://support.huaweicloud.com/aipcecce/index.html)
- [Huawei Cloud CCE ListClusters API](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=CCE&api=ListClusters)
- [IAM Policy Requirements](artifact/iam-policies.md)
- [Verification Method](artifact/verification-method.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Plain text table or status/error message, with Markdown documentation for setup and verification]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Huawei Cloud AK/SK credentials from environment variables and a region parameter that defaults to cn-north-4.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
