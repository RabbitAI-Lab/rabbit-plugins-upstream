## Description:

UCloud CLI helps agents inspect, create, update, and delete UCloud resources with the official ucloud CLI, including deployment-oriented cloud setup for web applications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ucloud](https://clawhub.ai/user/ucloud)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to manage UCloud resources, initialize CLI profiles, inspect account scope, and prepare infrastructure for application deployment through the official UCloud CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, delete, bind, or publicly expose UCloud resources, including billable resources.

Mitigation: Require explicit user confirmation before mutating resources, binding EIPs, or exposing services publicly; use a non-production project where possible.

Risk: The skill may use local UCloud profiles with broad account permissions.

Mitigation: Run it with a least-privilege UCloud profile and confirm the intended profile before executing resource-changing operations.

Risk: The skill can install or upgrade the UCloud CLI.

Mitigation: Verify the UCloud CLI release source and version before installation or upgrade.

Risk: Cloud host passwords or other login credentials could be exposed in chat summaries or command previews.

Mitigation: Do not print secrets in user-facing summaries; rotate any credential that has already been displayed.

Risk: Fixed shared temporary files for API payloads can leak or collide with other processes.

Mitigation: Use unique temporary files for API payloads and remove them immediately after use.

## Reference(s):

- [UCloud CLI quick start](https://docs.ucloud.cn/cli/intro)
- [UCloud CLI repository](https://github.com/ucloud/ucloud-cli)
- [UCloud OpenAPI documentation repository](https://github.com/UCloudDoc-Team/api)
- [UCloud product documentation](https://docs.ucloud.cn/)
- [Artifact CLI usage reference](artifact/references/cli-usage.md)
- [Artifact documentation sources reference](artifact/references/doc-sources.md)
- [Artifact product rules reference](artifact/references/product-rules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with concise summaries, tables, shell commands, and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Masks credentials and summarizes raw cloud API responses unless raw output is explicitly requested.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
