## Description:

Queries Huawei Cloud computing resources across ECS, BMS, IMS, and AS for read-only inventory, details, quotas, available specifications, images, console URLs, and scaling status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and infrastructure engineers use this skill to query Huawei Cloud compute inventory and supporting resource metadata without creating, modifying, or deleting resources. It helps collect reusable IDs, names, flavors, images, network attachments, quotas, and scaling configuration details for verification, automation planning, and environment inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup behavior disables TLS verification and may fall back to a remote installer download.

Mitigation: Fix TLS verification before routine use, install dependencies from trusted sources, and run setup only on trusted networks.

Risk: Some query scripts can return server passwords or console access URLs.

Mitigation: Invoke password and console scripts only when explicitly needed, redact outputs before sharing, and use least-privilege Huawei Cloud credentials.

Risk: The skill relies on Huawei Cloud access keys and secret keys supplied through environment variables.

Mitigation: Use scoped or temporary credentials where possible and avoid logging or displaying credential environment variable values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-computing-query)
- [ECS Python Script Usage Guide](artifact/references/ecs/guide.md)
- [BMS Query Guide](artifact/references/bms/guide.md)
- [IMS Python Script Usage Guide](artifact/references/ims/guide.md)
- [Huawei Cloud Auto Scaling Query Guide](artifact/references/as/guide.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only query outputs may include cloud resource identifiers, metadata, passwords, or console URLs depending on the selected script.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
