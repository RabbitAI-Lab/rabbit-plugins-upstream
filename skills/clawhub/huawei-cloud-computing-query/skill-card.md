## Description:

Queries Huawei Cloud ECS, BMS, IMS, Auto Scaling, and CCE resources in read-only mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect Huawei Cloud compute resources, compare available options, and inventory scaling groups and CCE clusters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud and package connections may run without certificate verification.

Mitigation: Use a corrected release with certificate verification enabled before supplying cloud credentials.

Risk: Password payloads and remote console URLs can expose sensitive server access information.

Mitigation: Handle these details only when explicitly requested, and keep them out of routine logs and caches.

Risk: Broad IAM enumeration and unverified dependency versions or hashes can increase exposure.

Mitigation: Use narrowly scoped temporary credentials, verify dependencies, and replace IAM-user enumeration with a scoped service check.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-computing-query)
- [ECS query guide](references/ecs/guide.md)
- [BMS query guide](references/bms/guide.md)
- [IMS query guide](references/ims/guide.md)
- [Auto Scaling query guide](references/as/guide.md)
- [CCE query guide](references/cce/guide.md)
- [IAM permissions guide](references/iam-policies.md)
- [Verification method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [text, JSON]

**Output Format:** [Concise text and JSON query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only resource queries; results depend on the selected resource and cloud environment.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
