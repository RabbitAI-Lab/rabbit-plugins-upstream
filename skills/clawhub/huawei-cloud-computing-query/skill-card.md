## Description:

Queries Huawei Cloud ECS, BMS, IMS, Auto Scaling, and CCE resources in read-only mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud developers and administrators use this skill to query existing Huawei Cloud compute resources, specifications, images, quotas, and relationships across ECS, BMS, IMS, Auto Scaling, and CCE. It returns information for inventory and verification without creating, changing, or deleting resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rates the release suspicious and reports insecure cloud connections, package-installation risks, and access to server password material beyond the stated query purpose.

Mitigation: Before installation, review the reported password-retrieval behavior, TLS settings, and package-install steps; use only the read-only permissions needed for the queries being run.

Risk: The security scan is incomplete: 114 of 118 components were fully inspected, and analysis of some referenced scripts was partial.

Mitigation: Review the remaining components and referenced-script behavior before relying on the scan as evidence that the release is safe.

## Reference(s):

- [ECS query guide](references/ecs/guide.md)
- [BMS query guide](references/bms/guide.md)
- [IMS query guide](references/ims/guide.md)
- [Auto Scaling query guide](references/as/guide.md)
- [CCE query guide](references/cce/guide.md)
- [IAM read-only permissions](references/iam-policies.md)
- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-computing-query)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON query results with concise Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only resource information; results depend on the selected region, permissions, and query parameters.]

## Skill Version(s):

1.0.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
