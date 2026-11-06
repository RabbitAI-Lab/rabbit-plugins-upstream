## Description:

Queries Huawei Cloud ECS, BMS, IMS, Auto Scaling, and CCE resources and returns read-only inventories and details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to inspect Huawei Cloud server, image, scaling, and container-cluster resources, check quotas, and gather current details for troubleshooting or planning. It is limited to read-only queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's setup disables connection-security checks, and installing dependencies before supplying cloud credentials can expose those credentials to untrusted sources.

Mitigation: Require verified HTTPS connections and authenticated dependency installation before providing cloud credentials.

Risk: Cloud queries use credentials, and password recovery queries can return sensitive values.

Mitigation: Use narrowly scoped temporary credentials. Request password information only when needed and deliver it through a protected channel.

Risk: Large inventory results may be cached locally.

Mitigation: Keep inventory caches private and temporary, and remove them when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-computing-query)
- [ECS query guide](references/ecs/guide.md)
- [BMS query guide](references/bms/guide.md)
- [IMS query guide](references/ims/guide.md)
- [Auto Scaling query guide](references/as/guide.md)
- [CCE query guide](references/cce/guide.md)
- [IAM permissions guide](references/iam-policies.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [JSON query data with concise Markdown or text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only resource information; available fields depend on service and query scope.]

## Skill Version(s):

1.0.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
